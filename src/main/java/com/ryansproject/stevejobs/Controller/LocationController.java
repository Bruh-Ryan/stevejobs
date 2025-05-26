package com.ryansproject.stevejobs.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.ryansproject.stevejobs.Model.LocationPost;
import com.ryansproject.stevejobs.Repository.LocationRepository;

@RestController
@RequestMapping("/api/locations")
public class LocationController{
    @Autowired
    private LocationRepository locationRepository;

     @GetMapping
    public List<LocationPost> getAllJobs() {
        return locationRepository.findAll();
    }
}
