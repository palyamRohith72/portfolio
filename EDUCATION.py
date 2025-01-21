import streamlit as st
import pandas as pd

class Education: 
    def __init__(self):
        pass

    def display(self):
       
        # Education data
        data = {
            "Education Level": [
                "10th Grade at Vijayam The School",
                "Intermediate at Vijayam Junior College",
                "BTech in AI and Data Science"
            ],
            "Details": [
                "Secured a perfect GPA of 10/10. This milestone marks the foundational years of dedication, hard work, and a passion for learning that shaped the journey ahead. The strong emphasis on academic excellence was coupled with active participation in extracurricular activities, creating a holistic educational experience.",
                "Specialized in MPC and achieved 84%. These two years were not just about academic rigor but also about mastering analytical and problem-solving skills. The choice of MPC reflects a deep interest in Mathematics and Science, laying a solid groundwork for a career in technology.",
                "Currently in the first semester, focusing on cutting-edge technologies. Embarking on this BTech journey in AI and Data Science signifies a commitment to exploring innovative solutions and staying ahead in the ever-evolving tech landscape. The curriculum combines theoretical knowledge with practical applications, ensuring a robust understanding of modern advancements."
            ],
            "Images": [
                "./edu_image1.jpg",  # Replace with actual image links
                "./edu_image2.jpg",
                "./edu_image3.jpg"
            ]
        }

        df = pd.DataFrame(data)

        # Row 1: Education information about 10th grade
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"""
            <div class="section-content">
                <strong>{df['Education Level'][0]}</strong><br>
                <span style="font-size:18px; color:#2196F3;">{df['Details'][0]}</span>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.image(df['Images'][0], width=150)

        st.markdown("---")

        # Row 2: Education information about Intermediate
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(df['Images'][1], width=150)
        with col2:
            st.markdown(f"""
            <div class="section-content">
                <strong>{df['Education Level'][1]}</strong><br>
                <span style="font-size:18px; color:#2196F3;">{df['Details'][1]}</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # Row 3: Education information about BTech
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"""
            <div class="section-content">
                <strong>{df['Education Level'][2]}</strong><br>
                <span style="font-size:18px; color:#2196F3;">{df['Details'][2]}</span>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.image(df['Images'][2], width=150)

        st.markdown("---")

        # Row 4: Summary of schools and percentages
        summary_data = {
            "Course":["10th Class","Intermediate-MPC","CAD"],
            "Institution": ["Vijayam The School", "Vijayam Junior College", "Siddartha Institue Of Technology And Science"],
            "Location":["Chittoor","Chittoor","Puttur"],
            "Percentage": ["10/10 GPA", "84%", "Ongoing"]
        }
        summary_df = pd.DataFrame(summary_data)
        st.table(summary_df)

        # Additional Insights Section
        st.markdown("""
        ### Highlights of the Journey
        - **10th Grade:** A shining example of perseverance and excellence, achieving a perfect GPA while actively engaging in science exhibitions and debates.
        - **Intermediate Education:** Developed a strong analytical mindset through MPC, excelling in both academics and practical applications.
        - **BTech:** A transformative phase focusing on innovation, critical thinking, and the pursuit of excellence in Artificial Intelligence and Data Science.

        Education is not just about grades but the journey of discovery, growth, and transformation. These milestones are a testament to the determination and vision for a bright future.
        """, unsafe_allow_html=True)
