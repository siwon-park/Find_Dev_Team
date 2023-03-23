FROM openjdk:11-jdk-slim AS build

COPY gradlew .

COPY gradle gradle

COPY build.gradle .

COPY settings.gradle .

COPY src src

RUN chmod +x gradlew

RUN ["./gradlew", "bootJar"]

FROM openjdk:11-jdk-slim

COPY --from=build build/libs/*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/app.jar"]