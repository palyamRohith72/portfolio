import streamlit as st
import pandas as pd

class Skills:
    def __init__(self):
        pass

    def display(self):
        # Skills data
        skills = {
            "Skill": [
                "HTML", "CSS", "TailwindCSS", "MaterializeCSS", "JavaScript",
                "Python", "Streamlit", "Flask", "Django", "MySQL",
                "MongoDB", "React", "ExpressJs"
            ],
            "Details": [
                "HTML forms the backbone of web development, allowing me to create well-structured, semantic, and accessible web pages. I have in-depth knowledge of tags, attributes, and best practices for ensuring a strong foundation for any web application.",
                "CSS empowers me to bring designs to life by styling web pages with precision. From crafting responsive layouts to implementing animations and transitions, I excel at creating visually appealing and user-friendly interfaces.",
                "TailwindCSS has enhanced my ability to design modern and responsive UIs efficiently. With its utility-first approach, I can rapidly prototype and build scalable designs that adhere to current industry standards.",
                "MaterializeCSS allows me to create sleek, professional, and consistent designs based on Google’s Material Design principles. It enables me to deliver high-quality, user-centric web applications effortlessly.",
                "JavaScript is my go-to language for adding dynamic and interactive behavior to web pages. My expertise includes DOM manipulation, event handling, and integrating APIs to create feature-rich web experiences.",
                "Python is my versatile programming tool for solving complex problems, automating tasks, and developing robust applications. From data analysis to web development, I leverage Python to its full potential.",
                "Streamlit allows me to transform Python scripts into interactive web applications quickly. I excel at building data visualization dashboards and AI-powered tools to deliver insights effectively.",
                "Flask is my framework of choice for building lightweight and fast web applications. With Flask, I can create APIs and backends that integrate seamlessly with various frontend technologies.",
                "Django provides me with a powerful platform for building secure and scalable web applications. I utilize its ORM, admin interface, and authentication features to streamline development.",
                "MySQL enables me to design, implement, and manage relational databases effectively. I have a strong understanding of SQL queries, database normalization, and performance optimization.",
                "MongoDB helps me handle NoSQL databases for modern applications. I leverage its flexibility to store and retrieve unstructured data, ensuring scalability and efficiency.",
                "React empowers me to build dynamic and reusable UI components. With a deep understanding of its virtual DOM and hooks, I create responsive and high-performance web applications.",
                "ExpressJs is my framework for building server-side applications with Node.js. I utilize its robust middleware system to develop scalable APIs and microservices with ease."
            ]
        }
        df = pd.DataFrame(skills)
        imagesList=[f"./images/skills{x+1}.png" for x in range(0,13)]

        # Display skills with alternating column layout
        for i in range(len(df)):
            if i % 2 == 0:
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.markdown(f"""
                    #### {df['Skill'][i]}
                    {df['Details'][i]}
                    """)
                with col2:
                    st.image(imagesList[i], width=150)
            else:
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.markdown(f"""
                    #### {df['Skill'][i]}
                    {df['Details'][i]}
                    """)
                with col2:
                    st.image(imagesList[i], width=150)

            st.markdown("---")
