package com.cloudhubs.trainticket.auth.config;

//import edu.fudanselab.trainticket.common.*;
import com.cloudhubs.trainticket.auth.config.jwt.JWTFilter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;

import org.springframework.security.authentication.ProviderManager;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.dao.DaoAuthenticationProvider;

import org.springframework.security.config.Customizer;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configurers.AuthorizeHttpRequestsConfigurer;
//import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
//import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;

import org.springframework.util.StringUtils;
import java.util.List;

import static org.springframework.web.cors.CorsConfiguration.ALL;

/**
 * @author fdse
 */
@Configuration
@EnableWebSecurity
@EnableMethodSecurity(prePostEnabled = true)
@EnableConfigurationProperties(SecurityProperties.class)
public class WebSecurityConfig {

    @Autowired
    @Qualifier("userDetailServiceImpl")
    private UserDetailsService userDetailsService;

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
    public AuthenticationManager authenticationManager(
            UserDetailsService userDetailsService,
            PasswordEncoder passwordEncoder) {
        DaoAuthenticationProvider authenticationProvider = new DaoAuthenticationProvider();
        authenticationProvider.setUserDetailsService(userDetailsService);
        authenticationProvider.setPasswordEncoder(passwordEncoder);

        return new ProviderManager(authenticationProvider);
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.httpBasic(t -> t.disable())
                .csrf(t -> t.disable())
                .sessionManagement(t -> t.sessionCreationPolicy(SessionCreationPolicy.STATELESS));

        // Fetching the RABC from configurations and dynamically applying them.
        http.authorizeHttpRequests((authorize) -> {
            for (SecurityProperties.AuthorizationRule rule : securityProperties.getAuthorizationRules()) {
                // Retreiving the paths and methods
                String[] paths = rule.getPaths().toArray(new String[0]);
                String method = rule.getMethod();

                AuthorizeHttpRequestsConfigurer.AuthorizedUrl authorizedUrl;

                // Apply method if it exists in the service.
                if (StringUtils.hasText(method)) {
                    authorizedUrl = authorize.requestMatchers(HttpMethod.valueOf(method.toUpperCase()), paths);
                } else {
                    authorizedUrl = authorize.requestMatchers(paths);
                }

                // Applying the authorization policy.
                List<String> authorities = rule.getAuthorities();
                if (authorities == null || authorities.isEmpty()) {
                    // It is assumed here that if no authorities are set to a path,
                    // the endpoint is blocked and hence, no request is permitted.
                    authorizedUrl.denyAll();
                } else if (authorities.contains("permitAll")) {
                    // Allows any user (a public API).
                    authorizedUrl.permitAll();
                } else if (authorities.contains("authenticated")) {
                    // Allows only the authenticated users (no role checked)
                    authorizedUrl.authenticated();
                } else {
                    // Allows only the users with specific roles.
                    String[] roles = authorities.stream()
                            .map(auth -> auth.startsWith("ROLE_") ? auth.substring(5) : auth)
                            .toArray(String[]::new);
                    authorizedUrl.hasAnyRole(roles);
                }
            }
            authorize.anyRequest().authenticated();
        });

        http.addFilterBefore(new JWTFilter(), UsernamePasswordAuthenticationFilter.class);
        return http.build();

    }
}
