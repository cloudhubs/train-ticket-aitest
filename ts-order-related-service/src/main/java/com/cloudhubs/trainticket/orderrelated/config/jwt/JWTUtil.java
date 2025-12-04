package com.cloudhubs.trainticket.orderrelated.config.jwt;

import com.cloudhubs.trainticket.orderrelated.exception.TokenException;
import io.jsonwebtoken.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import jakarta.servlet.ServletRequest;
import jakarta.servlet.http.HttpServletRequest;
import java.util.Base64;
import java.util.Collection;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;

public class JWTUtil {
    private JWTUtil() { throw new IllegalStateException("Utility class"); }
    private static final Logger LOGGER = LoggerFactory.getLogger(JWTUtil.class);
    private static String secretKey = Base64.getEncoder().encodeToString("super_secret_used_to_sing_with_32_bits".getBytes());

    public static Authentication getJWTAuthentication(ServletRequest request) {
        String token = getTokenFromHeader((HttpServletRequest) request);
        if (token != null && validateToken(token)) {
            UserDetails userDetails = new UserDetails() {
                @Override public Collection<? extends GrantedAuthority> getAuthorities() { return getRole(token).stream().map(SimpleGrantedAuthority::new).collect(Collectors.toList()); }
                @Override public String getPassword() { return ""; }
                @Override public String getUsername() { return getUserName(token); }
                @Override public boolean isAccountNonExpired() { return true; }
                @Override public boolean isAccountNonLocked() { return true; }
                @Override public boolean isCredentialsNonExpired() { return true; }
                @Override public boolean isEnabled() { return true; }
            };
            return new UsernamePasswordAuthenticationToken(userDetails, "", userDetails.getAuthorities());
        }
        return null;
    }

    private static String getUserName(String token) { return getClaims(token).getBody().getSubject(); }
    private static List<String> getRole(String token) { return (List<String>) getClaims(token).getBody().get("roles", List.class); }
    private static String getTokenFromHeader(HttpServletRequest request) {
        String bearerToken = request.getHeader("Authorization");
        return (bearerToken != null && bearerToken.startsWith("Bearer ")) ? bearerToken.substring(7) : null;
    }

    private static boolean validateToken(String token) {
        try { return !getClaims(token).getBody().getExpiration().before(new Date()); }
        catch (ExpiredJwtException e) { throw new TokenException("Token expired"); }
        catch (UnsupportedJwtException e) { throw new TokenException("Token format error"); }
        catch (MalformedJwtException e) { throw new TokenException("Token is not properly constructed"); }
        catch (SignatureException e) { throw new TokenException("Signature failure"); }
        catch (IllegalArgumentException e) { throw new TokenException("Illegal parameter exception"); }
    }

    private static Jws<Claims> getClaims(String token) { return Jwts.parser().setSigningKey(secretKey).parseClaimsJws(token); }
}
