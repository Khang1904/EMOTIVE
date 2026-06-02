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
    
    # Display current selection status
    st.markdown("### Current Key Selection")
    if st.session_state.selected_api_key:
        st.info(f"✅ Using predefined key: **{st.session_state.selected_api_key}**")
    elif st.session_state.custom_api_key:
        st.info(f"✅ Using custom API key (first 10 chars): **{st.session_state.custom_api_key[:10]}***")
    else:
        st.warning("⚠️ No API key selected. Please select or enter a key below.")
    
    st.divider()
    
    # Predefined Keys Section
    st.markdown("### 📦 Predefined Keys")
    col1, col2 = st.columns([3, 1])
    with col1:
        available_keys = ["OFFICIAL_KEY", "TEST_KEY_1", "TEST_KEY_2", "TEST_KEY_3"]
        selected_key = st.selectbox(
            "Select a predefined API key:",
            options=available_keys,
            help="Choose which predefined API key configuration to use",
            key="predefined_key_select"
        )
    
    with col2:
        st.write("")  # Spacing
        st.write("")  # Spacing
        if st.button("✓ Select", key="select_predefined"):
            st.session_state.selected_api_key = selected_key
            st.session_state.custom_api_key = ""
            st.success(f"✅ Switched to: {selected_key}")
            st.rerun()
    
    st.divider()
    
    # Custom Key Section
    st.markdown("### 🔐 Custom Key")
    col1, col2 = st.columns([3, 1])
    with col1:
        custom_key = st.text_input(
            "Enter your own Gemini API key:",
            type="password",
            value=st.session_state.custom_api_key,
            help="Paste your Gemini API key here. It will be kept secure.",
            key="custom_api_input"
        )
    
    with col2:
        st.write("")  # Spacing
        st.write("")  # Spacing
        if st.button("✓ Select", key="select_custom"):
            if custom_key.strip():
                st.session_state.custom_api_key = custom_key
                st.session_state.selected_api_key = None
                st.success("✅ Custom API key selected!")
                st.rerun()
            else:
                st.error("Please enter a valid API key.")
