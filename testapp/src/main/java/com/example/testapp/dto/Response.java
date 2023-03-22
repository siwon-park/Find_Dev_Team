package com.example.testapp.dto;

import lombok.Getter;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.lang.Nullable;

@Getter
public class Response {

    public static <T> ResponseEntity sucess(HttpStatus status, @Nullable T body) {
        return ResponseEntity.status(status).body(new SuccessDto<T>(body));
    }
}
