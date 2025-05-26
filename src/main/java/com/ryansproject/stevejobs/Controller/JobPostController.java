package com.ryansproject.stevejobs.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.ryansproject.stevejobs.Model.JobPost;
import com.ryansproject.stevejobs.Repository.JobPostRepository;

@RestController
@RequestMapping("/api/jobs")
public class JobPostController {

    @Autowired
    private JobPostRepository jobPostRepository;

    @GetMapping
            public List<JobPost> getAllJobs() {
        return jobPostRepository.findAll();
    }

     @GetMapping("/search/{title}")
    public List<JobPost> getJobsByTitle(@PathVariable String title) {
        return jobPostRepository.findByTitleContainingIgnoreCase(title);}

    @PostMapping
    public JobPost createJob(@RequestBody JobPost jobPost) {
        return jobPostRepository.save(jobPost);
    }

    @PutMapping("/{id}")
    public JobPost updateJob(@PathVariable String id, @RequestBody JobPost updatedJob) {
        updatedJob.setId(id);
        return jobPostRepository.save(updatedJob);
    }

    @DeleteMapping("/{id}")
    public void deleteJob(@PathVariable String id) {
        jobPostRepository.deleteById(id);
    }
}

