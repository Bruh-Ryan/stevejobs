package com.ryansproject.stevejobs.Model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "JobPosts")
public class LocationPost {
    @Id
    private String id;
    private String location;
    private String title;

    public LocationPost(String id, String location, String title) {
        this.id = id;
        this.location = location;
        this.title = title;
    }

    public String getId() {
        return id;
    }
    public void setId(String id) {
        this.id = id;
    }
    public String getLocation() {
        return location;
    }
    public void setLocation(String location) {
        this.location = location;
    }
    public String getTitle() {
        return title;
    }
    public void setTitle(String title) {
        this.title = title;
    }
    
}

 





