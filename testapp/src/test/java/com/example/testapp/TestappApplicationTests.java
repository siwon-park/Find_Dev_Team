package com.example.testapp;

import com.example.testapp.dto.Response;
import com.example.testapp.dto.SuccessDto;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

@SpringBootTest
class TestappApplicationTests {

	@Test
	@DisplayName("success 메서드 테스트")
	void successTest() {
		ResponseEntity responseEntity = Response.sucess(HttpStatus.OK, "TEST");


		Assertions.assertThat(responseEntity.getStatusCode()).isEqualTo(HttpStatus.OK);
		System.out.println("yes");
	}

}
