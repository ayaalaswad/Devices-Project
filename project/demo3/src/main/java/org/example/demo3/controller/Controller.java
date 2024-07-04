package org.example.demo3.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
@RequestMapping("/")
public class Controller {

    private final RestTemplate restTemplate;

    public Controller(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    @GetMapping("/api/devices/")
    public String get1() {
        String url = "http://127.0.0.1:5000";
        return restTemplate.getForObject(url, String.class);
    }

    @GetMapping("/api/devices/{id}")
    public String get2() {
        String url = "http://127.0.0.1:5000";
        return restTemplate.getForObject(url, String.class);
    }

    @PostMapping("/api/devices")
    public String post1() {
        String url = "http://127.0.0.1:5000";
        return restTemplate.postForObject(url, null, String.class);
    }

    @PostMapping("/api/predict/{deviceId}")
    public String post2() {
        String url = "http://127.0.0.1:5000";
        return restTemplate.postForObject(url, null, String.class);
    }
}

