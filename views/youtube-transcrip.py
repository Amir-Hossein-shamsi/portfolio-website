import streamlit as st
from dotenv import load_dotenv
import os
import requests
import re
from openai import OpenAI
import streamlit.components.v1 as components

load_dotenv()

def extract_video_id(url):
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11})',
        r'youtu\.be\/([0-9A-Za-z_-]{11})',
        r'embed\/\/([0-9A-Za-z_-]{11})',
        r'shorts\/([0-9A-Za-z_-]{11})'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_transcript(url):
    headers = {
        "x-api-key": os.getenv("SUPA_API_KEY"),
        "Content-Type": "application/json"
    }
    response = requests.get(f"https://api.supadata.ai/v1/youtube/transcript?url={url}&text=true", headers=headers)
    return response.json()['content']

def get_translated_transcript(content):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("QWEN_API_KEY"),
    )

    completion = client.chat.completions.create(
        extra_body={},
        model="deepseek/deepseek-chat-v3-0324:free",
        messages=[
            {"role": "system", "content": "Translate to fluent Persian language and improve readability"},
            {"role": "user", "content": content}
        ]
    )
    return completion.choices[0].message.content

st.title("YouTube Video Translator (DEMO) ")
url = st.text_input("Enter YouTube video URL", "")

if st.button("Process Video") and url:
    with st.spinner("Processing video and translating content..."):
        try:
            # Get video ID first
            video_id = extract_video_id(url)
            if not video_id:
                st.error("❌ Invalid YouTube URL")
                st.stop()

            # Get transcript
            transcript = get_transcript(url)
            
            # Translate
            translated = get_translated_transcript(transcript)
            
            # Create embed URL
            embed_url = f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0"
            
            # Show results after processing completes
            col1, col2 = st.columns([3, 2])
            
            with col1:
                components.html(
                    f"""
                    <iframe width="100%" height="400" 
                        src="{embed_url}" 
                        frameborder="0" 
                        allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" 
                        allowfullscreen
                        referrerpolicy="strict-origin-when-cross-origin"
                        style="border-radius: 10px; margin-bottom: 20px;">
                    </iframe>
                    """,
                    height=420
                )
            
            with col2:
                st.markdown(
                    f"""
                    <div dir="rtl" style="
                        text-align: right;
                        font-family: Tahoma;
                        font-size: 16px;
                        line-height: 1.8;
                        padding: 20px;
                        color:black;
                        background: #fff;
                        border-radius: 10px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                        height: 500px;
                        overflow-y: auto;
                    ">
                        {translated}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        except Exception as e:
            st.error(f"🚨 Error: {str(e)}")