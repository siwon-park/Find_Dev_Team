package com.example.testapp.dto;

import lombok.Getter;

@Getter
public class SuccessDto<T> {
    private String status;
    private T data;

    public SuccessDto(T data) {
        this.status = "success";
        this.data = data;
    }
}
