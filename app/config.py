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
    
    # Initialize session state for API key selection
    if "selected_api_key" not in st.session_state:
        st.session_state.selected_api_key = "OFFICIAL_KEY"
    if "custom_api_key" not in st.session_state:
        st.session_state.custom_api_key = ""
    
    # API Key Selection
    st.subheader("🔑 API Configuration")
    
    tab1, tab2 = st.tabs(["Predefined Keys", "Custom Key"])
    
    with tab1:
        st.markdown("Select from available predefined API keys:")
        available_keys = ["OFFICIAL_KEY", "TEST_KEY_1", "TEST_KEY_2", "TEST_KEY_3"]
        
        selected_key = st.selectbox(
            "Select the API key to use for the model:",
            options=available_keys,
            index=available_keys.index(st.session_state.selected_api_key),
            help="Choose which API key configuration to use for Gemini API calls",
            key="predefined_key_select"
        )
        
        if selected_key != st.session_state.selected_api_key:
            st.session_state.selected_api_key = selected_key
            st.session_state.custom_api_key = ""
            st.success(f"API key changed to: {selected_key}")
    
    with tab2:
        st.markdown("Enter your own Gemini API key:")
        custom_key = st.text_input(
            "Your API Key:",
            type="password",
            value=st.session_state.custom_api_key,
            help="Paste your Gemini API key here. It will be kept secure.",
            key="custom_api_input"
        )
        
        if custom_key != st.session_state.custom_api_key:
            st.session_state.custom_api_key = custom_key
            if custom_key:
                st.session_state.selected_api_key = None
                st.success("Custom API key has been set!")
            else:
                st.session_state.selected_api_key = "OFFICIAL_KEY"
