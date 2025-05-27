import streamlit as st
import requests
import uuid

BASE_URL = "http://localhost:8080/api/jobs"

st.title("SteveJobs Job Posts Dashboard")

# ----- Show latest 5 job posts -----
# st.header("🆕 Latest 5 Job Posts")
# try:
#     res_latest = requests.get(BASE_URL)
#     res_latest.raise_for_status()
#     all_jobs = res_latest.json()
#     latest_jobs = all_jobs[-5:] if len(all_jobs) > 5 else all_jobs

#     for job in reversed(latest_jobs):
#         st.subheader(f"🧾 {job.get('title', 'Untitled')}")
#         st.write(f"**Description:** {job.get('description', 'No description')}")
#         st.write(f"🏢 {job.get('company', '')} — 📍 {job.get('location', '')}")
#         st.markdown("---")
# except Exception as e:
#     st.error(f"Failed to load latest job posts: {e}")


# ----- List all jobs -----
st.header("📄 All Job Posts")
try:
    res_latest = requests.get(BASE_URL)
    res_latest.raise_for_status()
    all_jobs = res_latest.json()
    latest_jobs = all_jobs[-5:] if len(all_jobs) > 5 else all_jobs

    for job in reversed(all_jobs):
        st.subheader(f"🧾 {job.get('title', 'Untitled')}")
        st.write(f"**Company:** {job.get('company', 'N/A')}")
        st.write(f"🏢 {job.get('company', '')} — 📍 {job.get('location', '')}")
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

# ----- Search job posts by title -----
st.header("🔍 Search Job Posts by Title")
search_title = st.text_input("Enter title keyword to search")
if st.button("Search Jobs"):
    res = requests.get(f"{BASE_URL}/search/{search_title}")
    if res.status_code == 200:
        results = res.json()
        if results:
            for job in results:
                st.subheader(job.get("title", "Untitled"))
                st.write(f"📄 {job.get('description', 'No description')}")
                st.markdown("---")
        else:
            st.info("No matching jobs found.")
    else:
        st.error("❌ Failed to search jobs.")

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
delete_title = st.text_input("Enter Job Title to Delete")
if 'search_results' not in st.session_state:
    st.session_state.search_results = []

if st.button("Delete Job(s)"):
    search_response = requests.get(f"{BASE_URL}/search/{delete_title}")
    if search_response.status_code == 200:
        st.session_state.search_results = search_response.json()
    else:
        st.error("❌ Failed to search jobs.")
        st.session_state.search_results = []
if st.session_state.search_results:
    for i, job in enumerate(st.session_state.search_results):
        st.subheader(job.get('title', 'Untitled'))
        st.write(f"**Company:** {job.get('company', 'N/A')}")
        st.write(f"**Location:** {job.get('location', 'N/A')}")
        st.write(f"**Description:** {job.get('description', 'No description')}")
        
        if st.button(f"Delete This Job", key=f"delete_job_{i}"):
            try:
                delete_response = requests.delete(f"{BASE_URL}/{job.get('id')}")
                if delete_response.status_code == 200:
                    st.success(f"✅ Deleted: {job.get('title')}")
                    st.session_state.search_results.pop(i)
                    st.rerun()
                else:
                    st.error(f"❌ Failed to delete job")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
        st.markdown("---")
else:
    if delete_title:  # Only show this if user has searched
        st.info("No matching jobs found.")