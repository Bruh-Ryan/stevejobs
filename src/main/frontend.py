import streamlit as st
import requests

BASE_URL = "http://localhost:8080/api/jobs"

st.title("SteveJobs Job Posts Dashboard")

# ----- List all jobs -----
st.header("📄 All Job Posts")
try:
    res = requests.get(BASE_URL)
    res.raise_for_status()
    jobs = res.json()

    for job in jobs:
        st.subheader(f"🧾 {job.get('title', 'Untitled')}")
        st.write(f"**Company:** {job.get('company', 'N/A')}")
        st.write(f"**Location:** {job.get('location', 'N/A')}")
        st.write(f"**Description:** {job.get('description', 'No description')}")
        st.write(f"**ID:** `{job.get('id')}`")
        st.markdown("---")
except Exception as e:
    st.error(f"Failed to load job posts: {e}")

# ----- Create a new job -----
st.header("🆕 Create a New Job Post")
with st.form("create_job_form"):
    title = st.text_input("Title")
    description = st.text_area("Description")
    company = st.text_input("Company")
    location = st.text_input("Location")
    submitted = st.form_submit_button("Create Job")

    if submitted:
        response = requests.post(BASE_URL, json={
            "title": title,
            "description": description,
            "company": company,
            "location": location
        })
        if response.status_code == 200:
            st.success("✅ Job created successfully!")
        else:
            st.error("❌ Failed to create job.")

# ----- Get a job by ID -----
st.header("🔍 Get Job by ID")
job_id = st.text_input("Enter Job ID to Fetch")
if st.button("Fetch Job"):
    r = requests.get(f"{BASE_URL}/{job_id}")
    if r.status_code == 200:
        job = r.json()
        st.json(job)
    else:
        st.error("❌ Job not found.")

# ----- Update a job -----
st.header("✏️ Update Job")
update_id = st.text_input("Enter Job ID to Update")
with st.form("update_form"):
    new_title = st.text_input("New Title")
    new_description = st.text_area("New Description")
    update_button = st.form_submit_button("Update Job")

    if update_button:
        result = requests.put(f"{BASE_URL}/{update_id}", json={
            "title": new_title,
            "description": new_description
        })
        if result.status_code == 200:
            st.success("✅ Job updated successfully!")
        else:
            st.error("❌ Failed to update job.")

# ----- Delete a job -----
st.header("🗑️ Delete Job")
delete_id = st.text_input("Enter Job ID to Delete")
if st.button("Delete Job"):
    d = requests.delete(f"{BASE_URL}/{delete_id}")
    if d.status_code == 200:
        st.success("🧹 Job deleted successfully!")
    else:
        st.error("❌ Failed to delete job.")