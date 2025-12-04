package com.cloudhubs.trainticket.route.config;

import com.cloudhubs.trainticket.route.config.jwt.JWTFilter;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.context.properties.EnableConfigurationProperties;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import org.springframework.http.HttpMethod;

import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configurers.AuthorizeHttpRequestsConfigurer;
import org.springframework.security.config.http.SessionCreationPolicy;

import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

import org.springframework.util.StringUtils;

import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.util.List;

import static org.springframework.web.cors.CorsConfiguration.ALL;

/**
 * @author fdse
 */
@Configuration
@EnableWebSecurity
@EnableMethodSecurity(prePostEnabled = true)
@EnableConfigurationProperties(SecurityProperties.class)
public class SecurityConfig {

    @Autowired
    private SecurityProperties securityProperties;

    /**
     * load password encoder
     *
     * @return PasswordEncoder
     */
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public WebMvcConfigurer corsConfigurer() {
        // Use the interface directly, not the deprecated adapter
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("/**")
                        .allowedOrigins(ALL)
                        .allowedMethods(ALL)
                        .allowedHeaders(ALL)
                        .allowCredentials(false)
                        .maxAge(3600);
            }
        };
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {

        http.httpBasic(t -> t.disable())
                .csrf(t -> t.disable())
                .sessionManagement(t -> t.sessionCreationPolicy(SessionCreationPolicy.STATELESS));

        http.authorizeHttpRequests((authorize) -> {
            for (SecurityProperties.AuthorizationRule rule : securityProperties.getAuthorizationRules()) {

                String[] paths = rule.getPaths().toArray(new String[0]);
                String method = rule.getMethod();
                List<String> authorities = rule.getAuthorities();

                AuthorizeHttpRequestsConfigurer.AuthorizedUrl authorizedUrl;

                if (StringUtils.hasText(method)) {
                    authorizedUrl = authorize.requestMatchers(HttpMethod.valueOf(method.toUpperCase()), paths);
                } else {
                    authorizedUrl = authorize.requestMatchers(paths);
                }

                if (authorities == null || authorities.isEmpty()) {
                    authorizedUrl.denyAll();
                } else if (authorities.contains("permitAll")) {
                    authorizedUrl.permitAll();
                } else if (authorities.contains("authenticated")) {
                    authorizedUrl.authenticated();
                } else {
                    String[] roles = authorities.stream()
                            .map(auth -> auth.startsWith("ROLE_") ? auth.substring(5) : auth)
                            .toArray(String[]::new);
                    authorizedUrl.hasAnyRole(roles);
                }
            }
            authorize.anyRequest().authenticated();
        });

        http.addFilterBefore(new JWTFilter(), UsernamePasswordAuthenticationFilter.class);
        http.headers(headers -> headers.cacheControl(cache -> cache.disable()));

        return http.build();
    }
}