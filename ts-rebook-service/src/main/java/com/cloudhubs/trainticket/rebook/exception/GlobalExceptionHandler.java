package com.cloudhubs.trainticket.rebook.exception;

import com.cloudhubs.trainticket.rebook.util.Response;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class GlobalExceptionHandler {

    private static final Logger LOGGER = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<Response> handleHttpMessageNotReadable(HttpMessageNotReadableException ex) {
        LOGGER.error("[GlobalExceptionHandler][JSON parse error: {}]", ex.getMessage());
        return ResponseEntity
                .status(HttpStatus.BAD_REQUEST)
                .body(new Response<>(0, "Invalid request body: " + ex.getMostSpecificCause().getMessage(), null));
    }

    @ExceptionHandler(TokenException.class)
    public ResponseEntity<Response> handleTokenException(TokenException ex) {
        LOGGER.error("[GlobalExceptionHandler][Token error: {}]", ex.getMessage());
        return ResponseEntity
                .status(HttpStatus.UNAUTHORIZED)
                .body(new Response<>(0, ex.getMessage(), null));
    }
}
