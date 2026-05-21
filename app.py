import os
import pandas as pd
import google.generativeai as genai
import streamlit as st
import json
from app.chat import show_chat_page
from app.about import show_about_page
from app.config import show_config_page

# Set page configuration
st.set_page_config(
    page_title="EMOTIVE: The Emotion Visual Detector",
    page_icon="😊",
    layout="wide"
)

# Initialize session state for page tracking
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Create navbar in sidebar with buttons
st.sidebar.title("🧭 Navigation")

if st.sidebar.button("🏠 Home", use_container_width=True):
    st.session_state.current_page = "Home"
if st.sidebar.button("ℹ️ About", use_container_width=True):
    st.session_state.current_page = "About"
if st.sidebar.button("💬 Chat", use_container_width=True):
    st.session_state.current_page = "Chat"
# Page routing
if st.session_state.current_page == "Home":
    st.title("EMOTIVE: The Emotion Visual Detector")
    
    # Add handwritten subtitle with centered alignment
    st.markdown("""
        <div style="text-align: center;">
            <p style="font-family: 'Caveat', cursive; font-size: 52px; color: white; margin-top: -10px;">
                An AI that can understand your feelings
            </p>
        </div>
        <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Welcome to EMOTIVE! This application detects and analyzes emotions from visual input and text.
    
    Use the navigation menu on the left to explore different features:
    - **About**: Learn more about the project
    - **Chat**: Interact with our AI-powered emotion analysis
    - **Config**: Configure settings and preferences
    """)
    
elif st.session_state.current_page == "About":
    show_about_page()
    
elif st.session_state.current_page == "Chat":
    show_chat_page()
    
elif st.session_state.current_page == "Config":
    show_config_page()


