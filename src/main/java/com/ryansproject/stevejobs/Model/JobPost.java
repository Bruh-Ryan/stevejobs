package com.ryansproject.stevejobs.Model;
// the JobPost model is the Java class that represents a single document
// inside the JobPosts collection in your MongoDB Jobs database.
 
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "JobPosts")
public class JobPost {

    @Id
    private String id;
    private String title;
    private String description;
    private String company;
    private String location;

    // Constructors
    public JobPost() {}

    public JobPost(String title, String description, String company, String location) {
        this.title = title;
        this.description = description;
        this.company = company;
        this.location = location;
    }

    // Getters and Setters
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public String getCompany() { return company; }
    public void setCompany(String company) { this.company = company; }

    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
}
