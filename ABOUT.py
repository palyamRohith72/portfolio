import streamlit as st
import pandas as pd

class AboutMe:
    def __init__(self):
        pass

    def display(self):
        # Header section
        st.markdown("""
        <style>
        .header {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 20px;
            font-family: 'Arial', sans-serif;
        }
        .sub-header {
            text-align: center;
            font-size: 20px;
            color: #555555;
            margin-bottom: 30px;
            font-family: 'Arial', sans-serif;
        }
        </style>
        <div class="header">About Me</div>
        <div class="sub-header">A glimpse into my journey, passions, and aspirations</div>
        """, unsafe_allow_html=True)

        # Introduction section
        st.markdown("""
        <style>
        .section-title {
            font-size: 28px;
            color: #2196F3;
            margin-top: 30px;
            font-family: 'Arial', sans-serif;
        }
        .section-content {
            font-size: 18px;
            color: #333333;
            line-height: 1.6;
            font-family: 'Arial', sans-serif;
        }
        </style>
        <div class="section-title">Introduction</div>
        <div class="section-content">
            Hello! I am, Usha sree studying BTECH 1st Year, a passionate and driven individual currently embarking on an exciting journey in the world of technology. 
            With a love for learning and exploring, I am constantly seeking opportunities to grow both personally and professionally. 
            Welcome to my portfolio, where I share my story, achievements, and aspirations.
        </div>
        """, unsafe_allow_html=True)

        # Education section
        st.markdown("""
        <div class="section-title">Education</div>
        <div class="section-content">
            I completed my 10th grade at Vijayam The School, achieving a perfect GPA of 10/10. 
            Continuing my academic journey, I pursued my intermediate education at Vijayam Junior College, specializing in MPC, 
            where I secured an impressive 84%. Currently, I am in the first semester of my BTech in Artificial Intelligence 
            and Data Science at Siddartha Engineering college(Puttur), where I am building a strong foundation in cutting-edge technologies.
        </div>
        """, unsafe_allow_html=True)

        # Skills section
        st.markdown("""
        <div class="section-title">Skills</div>
        <div class="section-content">
            My skill set includes strong communication abilities in Telugu, Hindi, and English, alongside technical expertise 
            in programming languages like C, Java, and Python. I have a keen interest in domains such as full-stack web development, 
            data science, machine learning, and artificial intelligence, and I am continuously working on enhancing these skills.
        </div>
        """, unsafe_allow_html=True)

        # Hobbies and Interests section
        st.markdown("""
        <div class="section-title">Hobbies and Interests</div>
        <div class="section-content">
            Outside academics, I enjoy writing stories, reading books, and solving puzzles. These activities fuel my creativity 
            and enhance my problem-solving abilities, making them an integral part of my personal and professional growth.
        </div>
        """, unsafe_allow_html=True)

        # Achievements section
        st.markdown("""
        <div class="section-title">Achievements</div>
        <div class="section-content">
            I take pride in completing the TTD exams and Hindi Prachara Sabha exams, showcasing my dedication to learning. 
            Additionally, I have participated in elocutions and completed a full-stack web development course, which have 
            significantly contributed to my personal and professional development.
        </div>
        """, unsafe_allow_html=True)

        # Footer section
        st.markdown("""
        <style>
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 16px;
            color: #888888;
            font-family: 'Arial', sans-serif;
        }
        </style>
        <div class="footer">Thank you for visiting my profile! Feel free to connect with me to learn more.</div>
        """, unsafe_allow_html=True)
