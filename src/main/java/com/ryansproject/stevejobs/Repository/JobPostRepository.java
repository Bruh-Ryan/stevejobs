package com.ryansproject.stevejobs.Repository;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import com.ryansproject.stevejobs.Model.JobPost; 

@Repository
public interface JobPostRepository extends MongoRepository<JobPost, String> {
    // You can add custom query methods here (e.g., findByTitle, findByLocation)
    
}

