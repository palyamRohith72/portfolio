import streamlit as st
import pandas as pd

class Internship:
    def __init__(self):
        pass

    def display(self):
        st.title("Internship Opportunities")
        st.info("The Internships That I Have Done")
        
        # Internship details table
        dataFrame = pd.DataFrame({
            "Company": ["EdVedha"], 
            "Location": ["Remote"], 
            "Organization": ["AICTE, Private Limited, StartUpIndia"], 
            "Duration": ["1 Month"]
        })
        st.dataframe(dataFrame, use_container_width=True)
        
        # Internship selection
        col1, col2 = st.columns([1, 2],border=True)
        with col1:
            internshipSelected = st.pills("Select the Internship That You Want To Know", ["Full Stack Web Development"])
        
        with col2:
            if internshipSelected == "Full Stack Web Development":
                # Internship Image
                st.image("./images/aicteInternship.jpg", use_container_width=True, caption="Full Stack Web Development from EdVedha - A Rising StartUp")
                
                # Internship Description
                st.markdown("""
                ### Internship Overview:
                The **Full Stack Web Development** internship with **EdVedha** provided an excellent opportunity to gain hands-on experience in the development of both the frontend and backend of web applications. The internship, lasting **1 Month**, was designed to expose me to the full spectrum of web development practices, from HTML to server-side scripting, and equipped me with the skills necessary to build dynamic, interactive websites. 

                During this internship, I had the chance to work on a variety of projects that required the use of essential web technologies like **HTML**, **CSS**, **TailwindCSS**, **JavaScript**, **React**, and **Node.js**. I learned how to create responsive, visually appealing user interfaces and handle complex server-side logic, database management, and user authentication. This comprehensive experience allowed me to understand how various web development technologies work together to create functional, user-friendly applications.

                ### Roles and Responsibilities:
                As an intern, my primary role was to learn and implement what i learnt like  building scalable and responsive web applications. My tasks involved:
                - Learning how to Design intuitive and interactive user interfaces with **React** and **TailwindCSS**, ensuring that they were mobile-friendly and accessible across various platforms.
                - Learning how to Develop backend services and APIs using **Node.js** and **Express.js**, handling data flow, and managing databases with **MongoDB** and **MySQL**.
                - Learning how to Implement real-time features, such as chat functionalities and live updates, using **JavaScript** and **Socket.io**.
                - Learning how to Collaborate with a team of developers and designers to ensure the smooth integration of frontend and backend components.
                - Learning how to Test and debug code to ensure high-quality, error-free performance.

                ### Skills Gained:
                - **Frontend Development**: Gained extensive knowledge in **HTML**, **CSS**, **JavaScript**, **React**, and **TailwindCSS**, enabling the creation of visually appealing and responsive websites.
                - **Backend Development**: Built expertise in **Node.js**, **Express.js**, and **MongoDB**, as well as **MySQL**, to develop server-side logic and database management.
                - **Version Control**: Used **Git** and **GitHub** to manage project code, collaborate with team members, and ensure smooth version control.
                - **Problem Solving**: Developed strong problem-solving abilities through real-world coding challenges, debugging sessions, and system design.
                - **Agile Methodology**: Worked in an Agile environment, participating in daily standups, sprint planning, and code reviews, gaining exposure to industry-standard project management tools like **JIRA**.

                ### Learning Outcomes:
                By the end of this internship, I was proficient in building full-stack web applications from scratch. I gained a deep understanding of both the client-side and server-side development processes, including API creation, database management, and deploying applications on cloud platforms. The internship provided a comprehensive understanding of the lifecycle of a web development project, from initial design to deployment, giving me valuable skills that I will carry forward into future projects and career opportunities.
                """)
