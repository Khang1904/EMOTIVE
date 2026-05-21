import os
import pandas as pd
import google.generativeai as genai
import streamlit as st
import json

def show_config_page():
    """Display the configuration page"""
    st.title("⚙️ Configuration")
    st.markdown("""
    Configure your EMOTIVE settings and preferences here.
    """)
    
    # Placeholder for configuration options
    st.subheader("Settings")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Your configuration options will appear here")
    with col2:
        st.write("More settings coming soon")
