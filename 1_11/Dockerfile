FROM amazoncorretto:8-jdk AS build
EXPOSE 8080
WORKDIR /usr/src/app
COPY pom.xml .
COPY mvnw .
COPY .mvn .mvn
COPY src ./src

RUN chmod +x mvnw
RUN sed -i 's/\r$//' mvnw
RUN ./mvnw package


CMD ["java", "-jar", "./target/docker-example-1.1.3.jar"]
