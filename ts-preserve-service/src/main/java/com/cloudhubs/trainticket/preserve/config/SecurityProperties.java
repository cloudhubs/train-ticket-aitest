package com.cloudhubs.trainticket.preserve.config;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;
import java.util.ArrayList;
import java.util.List;

@Configuration
@ConfigurationProperties(prefix = "security")
public class SecurityProperties {

    private List<AuthorizationRule> authorizationRules = new ArrayList<>();

    public List<AuthorizationRule> getAuthorizationRules() {
        return authorizationRules;
    }

    public void setAuthorizationRules(List<AuthorizationRule> authorizationRules) {
        this.authorizationRules = authorizationRules;
    }
}