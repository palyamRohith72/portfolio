import streamlit as st
import pandas as pd

class Family:
    def __init__(self):
        pass

    def display(self):
        # Family data
        data = {
            "Family Member": ["Sambaiah", "Jyothi", "Rohith"],
            "Relation": ["Father", "Mother", "Brother"],
            "Occupation": ["Teacher", "Housewife", "Graduate"]
        }
        df = pd.DataFrame(data)

        # Row 1: Family Data Table
        st.markdown("### Family Overview")
        st.table(df)

        # Row 2: Father Information
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("./family/sambaiah.jpg", caption="Sambaiah", width=150)
        with col2:
            st.markdown("""
            #### Sambaiah - Teacher
            With years of experience shaping young minds, Sambaiah believes in the transformative power of education. His principles of discipline and lifelong learning serve as an inspiration for the entire family.
            """)

        st.markdown("---")

        # Row 3: Mother Information
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            #### Jyothi - Homemaker
            Jyothi, the cornerstone of the family, exemplifies selflessness and dedication. Her nurturing nature and ability to manage everything seamlessly reflect her strength and resilience.
            """)
        with col2:
            st.image("./family/mohanajyothi.jpg", caption="Jyothi", width=150)

        st.markdown("---")

        # Row 4: Brother Information
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("./family/rohith.jpg", caption="Rohith", width=150)
        with col2:
            st.markdown("""
            #### Rohith - Graduate
            A recent graduate brimming with enthusiasm and ambition, Rohith is charting his path toward a promising future. His dedication to learning and growth inspires everyone around him.
            """)
      