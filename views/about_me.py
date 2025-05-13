import streamlit as st
import forms.contact as contact
from utils import *


b_profile=get_image_base64("assets/profile.jpg")

@st.dialog("Contact Me")
def show_contact_form():
   contact.contact_form()

col1,col2=st.columns(2,gap="small",vertical_alignment="center")
with col1:
    # Use custom HTML to display the image without the zoom icon
  st.markdown(
    f"""
    <style>
    .no-zoom img {{
        display: block;
        margin: auto;
        width: 450px;
        height: auto;
        border-left: 5px solid #630313;
        border-radius: 5px;
    }}
    </style>
    <div class="no-zoom">
        <img src="data:image/png;base64,{b_profile}" alt="Profile Picture">
    </div>
    """,
    unsafe_allow_html=True,
)
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

# --- HARD SKILLS ---
st.markdown("###")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
      ⚪  Python (Flask, FastAPI, Django)\n
      ⚪  LLM (Hugging Face, OpenAI, LangChain)\n
      ⚪  Retrieval-Augmented Generation (RAG) and Fine-tuning\n
      ⚪  Tesseract OCR and EasyOCR\n
      ⚪  Machine Learning (Scikit-learn, TensorFlow, Keras)\n
      ⚪  Web Scraping (BeautifulSoup, Scrapy, Selenium)\n
      ⚪  PyQt6\n
      ⚪  Go (Fiber, Gin)\n
      ⚪  Docker and Docker Compose\n
      ⚪  Typescript (NestJS, Express, Fastify)\n
      ⚪  SQL-based and NoSQL-based Databases\n
      ⚪  LPIC-1 & LPIC-2\n
    """
)   

# --- SOFT SKILLS ---
st.markdown("###")
st.subheader("Soft Skills", anchor=False)
st.write(
    """
      💠 Effective communication and collaboration in team environments\n
      💠 Strong problem-solving and critical thinking abilities\n
      💠 Adaptability to new technologies and methodologies\n
      💠 Time management and ability to meet deadlines\n
      💠 Attention to detail and commitment to quality\n
      💠 Creativity and innovation in software solutions\n
      💠 Continuous learning and self-improvement\n 
    """
)           