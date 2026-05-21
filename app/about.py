import os
import pandas as pd
import google.generativeai as genai
import streamlit as st
import json

def show_about_page():
    """Display the about page content"""
    st.title("ℹ️ About EMOTIVE")
    st.markdown("""
    ## Project Overview
    EMOTIVE is an advanced emotion detection and analysis system that combines:
    - **Computer Vision**: Facial expression recognition using CNN models
    - **Natural Language Processing**: Sentiment and emotion analysis from text
    - **AI Integration**: Powered by Google's Generative AI for intelligent insights
    
    ## Features
    - Real-time emotion detection from facial expressions
    - Text-based sentiment analysis
    - AI-powered emotional insights and responses
    - Visual emotion dataset analysis
    
    ## Technology Stack
    - **Frontend**: Streamlit
    - **Deep Learning**: TensorFlow/Keras
    - **NLP**: Google Generative AI
    - **Data Processing**: Pandas
    """)

