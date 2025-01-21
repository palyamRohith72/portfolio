import streamlit as st
from pymongo import MongoClient
from bson.binary import Binary
from streamlit_extras.metric_cards import style_metric_cards

class DataBase:
    def __init__(self):
        self.client = MongoClient(st.secrets["database"]["clientLink"])
        self.db = self.client["UshaDB"]
        self.collection = self.db["UshaCollection"]
        self.db1 = self.client["RohithDB"]
        self.collection1 = self.db1["RohithCollection"]

    def __del__(self):
        self.client.close()

    def add_info(self, purpose, company, name, designation, linkedin_url, photo):
        result = self.collection.insert_one({
            "purpose": purpose,
            "company": company,
            "name": name,
            "designation": designation,
            "linkedin_url": linkedin_url,
            "photo": Binary(photo.getvalue())
        })
        return result.acknowledged

    def get_data(self, filters):
        return self.collection.find(filters, {"_id": 1, "purpose": 1, "company": 1, "name": 1, "designation": 1, "linkedin_url": 1, "photo": 1})

    def update_schedule(self, document_id, schedule_type, date, start_time, end_time, location, google_map_link, company_photo):
        update_fields = {
            "schedule_type": schedule_type,
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
            "location": location,
            "google_map_link": google_map_link,
            "company_photo": company_photo
        }
        result = self.collection.update_one({"_id": document_id}, {"$set": update_fields})
        return result.modified_count > 0

    def display(self):
        st.subheader("Create Your Account", divider='blue')
        st.warning("Note: Your data won't be stored for more than 2 days in the database. We are taking your info to contact you regarding internships and job opportunities.")

        tab1, tab2, tab3 = st.tabs(["Create Your Account Here", "Your Data Is Displayed Here", "Schedule Interview or Job"])

        with tab1:
            col1,col2=st.columns([1,2],border=True)
            with col2:
                self.purpose = st.selectbox("Please specify the purpose of viewing my portfolio", ["Just for fun", "For Providing An Internship", "For Providing Job Opportunity"])
                if self.purpose == "For Providing An Internship":
                    if "internship" not in st.session_state:
                        st.session_state["internship"] = None
                if self.purpose == "For Providing Job Opportunity":
                    if "job" not in st.session_state:
                        st.session_state['job'] = None
    
                self.company = st.text_input("In Which Company Do You Work")
                self.name = st.text_input("Your Name")
                self.designation = st.text_input("Enter Your Designation In Company")
                self.linkedin_url = st.text_input("Enter Your LinkedIn URL")
    
                if self.purpose and self.company and self.name and self.designation and self.linkedin_url:
                    self.photo = st.camera_input("Please Share Your Photo")
                    if self.photo:
                        if st.button("Take this information", use_container_width=True, type='primary'):
                            success = self.add_info(self.purpose, self.company, self.name, self.designation, self.linkedin_url, self.photo)
                            if success:
                                st.success("Added your data. You can view it in the 'Your Data Is Displayed Here' tab.")
            with col1:
                style_metric_cards()
                st.metric("Total Views",value= self.collection.count_documents({}))
                

        with tab2:
            filters = {"purpose": self.purpose, "company": self.company, "name": self.name, "designation": self.designation, "linkedin_url": self.linkedin_url}
            result = self.get_data(filters)
            if self.purpose!="Just for fun":
                st.subheader("Your Details", divider='green')
                for data in result:
                    col1, col2 = st.columns([1, 2], gap='small',border=True)
                    col1.image(data["photo"])
                    col2.text(f"Name: {data['name']}")
                    col2.text(f"Designation: {data['designation']}")
                    col2.text(f"Company: {data['company']}")
                    col2.text(f"LinkedIn URL: {data['linkedin_url']}")
                    col2.text(f"Purpose of Visiting: {data['purpose']}")
            else:
                st.warning("You Not Yet Registered.\nRegister First")

        with tab3:
            filters = {"purpose": self.purpose, "company": self.company, "name": self.name, "designation": self.designation, "linkedin_url": self.linkedin_url}
            result = self.get_data(filters)
            if self.purpose != "Just for fun":
                for data in result:
                    st.subheader("Schedule An Interview/Job", divider='blue')
                    col1, col2 = st.columns([1, 2], gap='small',border=True)
                    schedule_type = col2.selectbox("Schedule For", ["Interview", "Job"])
                    date = col2.text_input("Date for Schedule")
                    start_time = col2.text_input("Start Time")
                    end_time = col2.text_input("End Time")
                    location_type = col2.selectbox(f"{schedule_type} Type", ["Virtual", "From Office"])
    
                    location = google_map_link = company_photo = None
                    if location_type != "Virtual":
                        location = col2.text_area("Enter Location")
                        google_map_link = col2.text_input("Enter Google Map Link")
                        company_photo = col2.file_uploader("Upload Company Building Photo For Reference", type=["jpeg", "jpg", "png"])
    
                    if col2.button("Confirm Schedule", use_container_width=True, type='primary'):
                        company_photo_binary = Binary(company_photo.read()) if company_photo else None
                        success = self.update_schedule(data["_id"], schedule_type, date, start_time, end_time, location, google_map_link, company_photo_binary)
                        if success:
                            col2.success("Schedule confirmed. I will contact you on the date and time you specified.")
                            st.link_button("/main.py",use_container_width=True,type='primary')
            else:
                st.info("You not yet registered.\nRegister First")

DataBase().display()
