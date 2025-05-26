package com.ryansproject.stevejobs.Repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.ryansproject.stevejobs.Model.LocationPost;

public interface LocationRepository extends MongoRepository<LocationPost, String>{
   
}
