import streamlit as st
from streamlit_option_menu import option_menu
from ABOUT import *
from EDUCATION import *
from FAMILY import *
from SKILLS import *
from INTERNSHIPS import *
from ACHEIVEMENTS import *

#declaring the instances
aboutme = AboutMe()
education = Education()
family = Family()
skills = Skills()
internships = Internship()
acheivements = Acheivements()




# Sidebar with option menu
with st.sidebar:
    st.subheader("Profile Photo")
    st.image("./family/usha.jpg",use_container_width=True,caption="Usha Sree")
    selected = option_menu(
        "Main Menu",
        ["About", "Education", "Family", "Skills", "Internships", "Participations", "Achievements"],
        icons=["person-circle", "book", "house", "code-slash", "briefcase", "trophy", "award"],
        menu_icon="menu-button-wide",
        default_index=0,
    )

# Main content based on selected option
if selected == "About":
    aboutme.display()

elif selected == "Education":
    education.display()

elif selected == "Family":
    family.display()

elif selected == "Skills":
    skills.display()

elif selected == "Internships":
    internships.display()

elif selected == "Participations":
    with st.expander("My Participation"):
        st.warning("I havent participated in any type of hackathons related to computer field untill now. I hope i will update this section in very soon")

elif selected == "Achievements":
    acheivements.display()
