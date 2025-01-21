import streamlit as st
import pandas as pd

class Acheivements:
    def __init__(self):
        pass
    def display(self):
        st.title("Achievements")
        col1, col2 = st.columns([1, 2])
        with col1:
            choice = st.radio("Select Category Of Achievement To See Acheivements Certififcation", ["apptitude & Talent Tests", "Co circuler activities", "Language Fluency", "Academic Acheivements","Sports"])
        with col2:
            if choice == "apptitude & Talent Tests":
                with st.form("Acheivements In Apptitute & Other Talent Tests"):
                    st.subheader("National Analytical Aptitude Test")
                    st.image("./aptitude5.jpg", caption="NAtional Analytical Aptitude Test", use_container_width=True)
                    st.subheader("Science - Indian Talent Test")
                    st.image("./aptitude1.jpg", caption="Science - Indian Talent Test", use_container_width=True)
                    st.subheader("vedic maths")
                    st.image("./aptitude2.jpg", caption="vedic maths", use_container_width=True)
                    st.subheader("Unified English Olympiad 2017")
                    st.image("./aptitude3.jpg", caption="Unified English Olympiad 2017", use_container_width=True)
                    st.subheader("Unified English Olympiad 2018")
                    st.image("./aptitude4.jpg", caption="Unified English Olympiad 2018", use_container_width=True)
                    st.subheader("Sucher India Talent Test")
                    st.image("./aptitude6.jpg", caption="Sucher India",use_container_width=True)
                    submitted = st.form_submit_button("completed")
                    if submitted:
                        pass
            if choice == "Co circuler activities":
                with st.form("Co circuler activities"):
                    st.subheader("Essay Competetions")
                    st.image("ca2.jpg", use_container_width=True)
                    submitButton = st.form_submit_button("Completed")
            if choice == "Language Fluency":
                with st.form("Language Fluency"):
                    st.subheader("Telugu Language Proficiency Test")
                    st.image("lp1.jpg", use_container_width=True)
                    st.image("lp2.jpg", use_container_width=True)
                    st.subheader("Hindi Language Proficiency Test")
                    st.image("lp3.jpg", use_container_width=True)
                    st.image("lp4.jpg", use_container_width=True)
                    st.image("lp5.jpg", use_container_width=True)
                    st.image("lp6.jpg", use_container_width=True)
                    st.image("lp7.jpg", use_container_width=True)
                    submitbutton = st.form_submit_button("Completed")
            if choice == "Academic Acheivements":
                with st.form("Academic Acheivements"):
                    st.subheader("10th Marks Sheet")
                    st.image("aa1.jpg", use_container_width=True)
                    st.subheader("Inter Mark sheet")
                    st.image("aa2.jpg", use_container_width=True)
                    sbtn = st.form_submit_button("Then")
            if choice == "Sports":
                with st.form("Sports"):
                    st.subheader("Chess")
                    st.image("ca1.jpg", use_container_width=True)
                    st.subheader("Martial Arts")
                    st.image("games1.jpg", use_container_width=True)
                    sBUTTON=st.form_submit_button("Prev")


                    