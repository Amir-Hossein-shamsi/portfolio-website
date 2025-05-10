import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
from utils import *
from query import *

# ----page Setup ----
about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
sales_dashbord = st.Page(
    "views/sales_dashboard.py",
    title="Projects",
    icon=":material/bar_chart:",
)
chat_bot = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
st.set_page_config(page_title="Dashboard", page_icon="🏞️", layout="wide", initial_sidebar_state="expanded")

# ------Navigation page -----

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [sales_dashbord, chat_bot],
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("assets/pic1.JPG")
st.sidebar.markdown(
    """
    <div style="text-align: center;">
        Made by AmirHossein (<a href="mailto:shamsiamirhossein1@gmail.com">shamsiamirhossein1@gmail.com</a>)
    </div>
    """,
    unsafe_allow_html=True
)
# ----page Config ----
pg.run()