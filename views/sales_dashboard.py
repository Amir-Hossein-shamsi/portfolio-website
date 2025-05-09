import streamlit as st
import os
from  utils import *

p_image = get_image_base64("assets/project.png")
# st.sidebar.markdown(
#     f"""
#     <div style="text-align: center;">
#         <img src="data:image/png;base64,{logo_base64}" alt="Logo" width="120">
#         <p>Online Analytics</p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
# Custom CSS for enhanced styling
st.markdown("""
<style>
:root {
    --primary-color: #2E86C1;
    --secondary-color: #F4F6F6;
}

body {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.project-card {
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    margin: 15px 0;
    background: white;
    transition: transform 0.3s, box-shadow 0.3s;
    border-left: 5px solid var(--primary-color);
}
.github-link {
    color: #000000 !important;
    font-weight: 500;
}

.project-title {
    color: var(--primary-color) !important;
    margin-bottom: 15px !important;
}

.project-image {
    border-radius: 10px;
    margin-bottom: 20px;
    transition: transform 0.3s;
}

.project-image:hover {
    transform: scale(1.03);
}

.btn-primary {
    background: var(--primary-color) !important;
    color: white !important;
    padding: 8px 20px;
    border-radius: 25px;
    text-decoration: none;
    transition: all 0.3s;
    border: none;
}

.btn-primary:hover {
    background: #2471A3 !important;
    transform: translateY(-2px);
}

.footer {
    padding: 2rem;
    background: var(--primary-color);
    color: white !important;
    border-radius: 15px;
    margin-top: 40px !important;
}

/* Modify existing footer links */
.footer a {
    color: black !important;
    text-decoration: none;
    transition: opacity 0.3s;
}

.footer a:hover {
    opacity: 0.8;
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# Project data
projects = [
    {
        "title": "📚 DRF Book Store",
        "description": """
            Django REST Framework API for book management with features:
            - JWT Authentication
            - Advanced filtering & searching
            - Custom permissions system
            - Cart functionality
            - Swagger documentation
            """,
        "image": "assets/project.png",
        "code_url": "https://github.com/Amir-Hossein-shamsi/drf-book-store",
        "demo_url": "#"
    },
    {
        "title": "🤖 AI ChatBot",
        "description": """
            Intelligent conversational agent featuring:
            - Groq API integration
            - LangChain framework
            - DeepSeek-r1 model
            - Context-aware responses
            - Multi-turn conversations
            """,
        "image": "assets/project.png",
        "code_url": "#",
        "demo_url": "#"
    },
    {
        "title": "🎥 Video Converter",
        "description": """
            Desktop application for video processing:
            - FFmpeg integration
            - Custom resolution/output control
            - Batch processing
            - Progress tracking
            - PyQt GUI
            """,
        "image": "assets/project.png",
        "code_url": "#",
        "demo_url": "#"
    },
    {
        "title": "📃 PDF Summarizer ",
        "description": """
            This project provides a Python script that loads PDF documents from an assets directory,
            combines their text content, and uses Groq's ChatGroq large language model via LangChain to generate concise summaries:
           - Bulk PDF Loading: Automatically discovers and loads all PDF files under ./assets.
           - Text Extraction: Uses PyMuPDFLoader to extract text from each page of the PDFs.
           - Context Formatting: Merges extracted page contents into a single context string for summarization.
           - LLM Summarization: Utilizes Groq's deepseek-r1-distill-llama-70b model with LangChain to produce reliable, non-hallucinatory summaries.
           - Configurable Summary Length: Specify the desired word count for the summary.
            """,
        "image": "assets/project.png",
        "code_url": "https://github.com/Amir-Hossein-shamsi/PDF-Summarizer",
        "demo_url": "#"
    },
    {
        "title": "📺 Video Player",
        "description": """
            Media player application with features:
           - Play, Pause & Stop media files
           - Seek Bar for random access within video/audio
           - Volume Control & Mute toggle
           - Fullscreen Mode
           - Open File Dialog: supports .mp4, .avi, .mkv, .mov, .mp3, .wav and encrypted .enc files
           - AES-CTR Decryption of .enc files using a password (PBKDF2-HMAC-SHA256 key derivation)
           - Progress Feedback during decryption
           - Temporary File Cleanup on exit
            """,
        "image": "assets/project.png",
        "code_url": "https://github.com/Amir-Hossein-shamsi/video_player",
        "demo_url": "#"
    },
    {
        "title": "🎛️ Audio Signal Analysis",
        "description": """
            A Python script to load, analyze, and visualize WAV audio files by plotting their waveform:
            - Prints audio duration.
            - Displays and saves waveform plot as image (in this case test.png)
            """,
        "image": "assets/project.png",
        "code_url": "https://github.com/Amir-Hossein-shamsi/Audio-Signal-Analysis",
        "demo_url": "#"
    },
    {
        "title": "🔐 SecureCrypt",
        "description": """
            SecureCrypt is a polished desktop application built with PyQt6 and Python, offering robust, password-based encryption and decryption for files and directories.
            With AES-256-CTR, PBKDF2 key derivation, and an intuitive GUI, protecting your data has never been easier—or looked so good:
           - File & Directory Encryption: Encrypt individual files or entire folders (directories auto-zipped).
           - Seamless Decryption: Restore original files or unpack encrypted archives with a single click.
           - AES-256-CTR Security: Industry-standard encryption with random salt & nonce per operation.
           - PBKDF2 with 150 000 Iterations: Strong key stretching using SHA-256.
           - Real-time Progress & Status: Dynamic progress bar and status messages keep you informed.
           - Password Strength Meter: Visual feedback (Weak/Medium/Strong) encourages secure passwords.
           - Persistent Settings: Remembers last-used directory via QSettings.
            """,
        "image": "assets/project.png",
        "code_url": "https://github.com/Amir-Hossein-shamsi/securecrypt",
        "demo_url": "#"
    },
]

# Header section
st.markdown("<h1 style='text-align: center; color: var(--primary-color);'>Amir Hossein Shamsi</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; margin-bottom: 40px;'>Python Developer </h3>", unsafe_allow_html=True)

# Projects grid
for project in projects:
    with st.container():
        st.markdown(f'<div class="project-card">', unsafe_allow_html=True)
        
        # Project image with error handling
        col_img, col_content = st.columns([1, 2])
        with col_img:
            if os.path.exists(project["image"]):
                st.markdown(f'<img src="data:image/png;base64,{p_image}" class="project-image" style="width: 100%">', 
                           unsafe_allow_html=True)
            else:
                st.error("Image not available")
        
        with col_content:
            # Project title and description
            st.markdown(f'<h2 class="project-title">{project["title"]}</h2>', unsafe_allow_html=True)
            st.markdown(project["description"])
            
            # Action buttons
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.markdown(f'<a href="{project["code_url"]}" class="btn-primary" target="_blank">View Code</a>', 
                           unsafe_allow_html=True)
            with btn_col2:
                if project["demo_url"] != "#":
                    st.markdown(f'<a href="{project["demo_url"]}" class="btn-primary" target="_blank">Live Demo</a>', 
                               unsafe_allow_html=True)
                else:
                    st.markdown(f'<button class="btn-primary" disabled>Demo Coming Soon</button>', 
                               unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <h3 style='text-align: center; color: white;'>Let's Connect!</h3>
    <p style='text-align: center; margin-bottom: 0;'>
        <a href="https://github.com/Amir-Hossein-shamsi" class="github-link" target="_blank">
            GitHub • 
        </a>
        <a href="#" style='color: black !important; text-decoration: none;'>
            LinkedIn • 
        </a>
        <a href="#" style='color: white !important; text-decoration: none;'>
            Personal Website
        </a>
    </p>
</div>
""", unsafe_allow_html=True)