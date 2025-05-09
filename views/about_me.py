import streamlit as st
import forms.contact as contact



@st.dialog("Contact Me")
def show_contact_form():
   contact.contact_form()

col1,col2=st.columns(2,gap="small",vertical_alignment="center")
with col1:
    st.image("assets/profile.jpg",width=350)
with col2:
    st.title("Amir Hossein Shamsi",anchor='false')
    st.write(
        """
        A Back-End Programmer with several years of experience in developing and optimizing software systems.
        Possesses high proficiency in programming languages such as Golang, python and JavaScript (TS as a superset).
        Familiar with database systems (SQL and NoSQL) and microservices architecture, and acquainted with Large Language Models (LLM).
        Helped improve the scalability and performance of systems by tailoring them to meet the collection's needs.
        Played a role in the completion and development of several web crawlers for governmental organizations.
        Problem-solving and data analysis skills have enabled me to successfully work on challenging projects and meet client needs in the best possible way."""
    )
    if st.button("📧 Contact Me",key="contact"):
        show_contact_form()
    
# --- EXPERIENCE & QUALIFICATIONS ---
st.markdown("---")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
   - Several years of experience as a Back-End Programmer, focused on developing and optimizing software systems.
   - High proficiency in programming languages including Golang, Python, and JavaScript (TypeScript).
   - Familiarity with Microservices architecture, SQL and NoSQL database systems, and Large Language Models (LLM), including experience implementing Retrieval-Augmented Generation (RAG) systems.
   - Proven ability to improve system scalability and performance through tailored development.
   - Experience in developing and completing web crawlers, including projects for governmental organizations.
   - Strong problem-solving and data analysis skills, enabling successful navigation of challenging projects and effective client needs fulfillment.
    """
)

# --- SKILLS ---
st.markdown("###")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
      -  Python (Django, Flask, FastAPI, PySide6, Pandas, NumPy, Selenium, PyQT)
      -  Go (Fiber, Gin)
      -  Docker and Docker Compose
      -  Retrieval-Augmented Generation (RAG)
      -  LangChain
      -  Typescript (NestJS, Express, Fastify)
      -  SQL-based and NoSQL-based Databases
      -  LPIC-1 & LPIC-2  
    """
)       