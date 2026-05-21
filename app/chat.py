import os
import pandas as pd
import google.generativeai as genai
import streamlit as st
import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from PIL import Image
import io

def show_chat_page():
    """Display the chat page content"""
    st.title("💬 Chat with EMOTIVE")
    st.markdown("""
    Have a conversation with our AI-powered emotion detection system.
    """)
    
    # Initialize session state for stage tracking
    if "analysis_stage" not in st.session_state:
        st.session_state.analysis_stage = "cnn"
    if "captured_photo" not in st.session_state:
        st.session_state.captured_photo = None
    if "predictions" not in st.session_state:
        st.session_state.predictions = None
    
    # Image Input Stage (CNN)
    if st.session_state.analysis_stage == "cnn":
        st.subheader("📷 Image Input")
        
        camera_photo = st.camera_input("Take a photo with your camera")
        
        if camera_photo is not None:
            st.image(camera_photo, caption="Camera Photo", use_container_width=True)
            st.success("Photo captured successfully!")
            st.session_state.captured_photo = camera_photo
            
            if st.button("Analyze Emotion", key="analyze_camera"):
                st.session_state.analysis_stage = "cnn_processing"
                st.rerun()
    
    # CNN Processing Stage
    if st.session_state.analysis_stage == "cnn_processing":
        st.subheader("🔍 CNN Analysis (Facial Recognition)")
        st.write("Analyzing facial expressions and emotions...")
        
        # Load model and make predictions
        if st.session_state.captured_photo is not None:
            try:
                # Load the CNN model
                model_path = "models/CNN_ep50.h5"
                model = load_model(model_path)
                
                # Process the image
                img = Image.open(st.session_state.captured_photo)
                # Convert to grayscale
                img = img.convert('L')
                img_array = np.array(img.resize((48, 48))) / 255.0
                
                # Add batch and channel dimensions
                img_array = np.expand_dims(img_array, axis=0)
                img_array = np.expand_dims(img_array, axis=-1)
                
                # Make prediction
                predictions = model.predict(img_array, verbose=0)
                
                # Emotion classes based on FER2013 dataset
                emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
                
                # Get top 3 predictions
                top_3_indices = np.argsort(predictions[0])[-3:][::-1]
                
                st.session_state.predictions = predictions[0]
                
                # Display results
                st.write("**Top 3 Emotion Predictions:**")
                for rank, idx in enumerate(top_3_indices, 1):
                    emotion = emotion_labels[idx]
                    confidence = predictions[0][idx] * 100
                    st.write(f"{rank}. **{emotion}**: {confidence:.2f}%")
                
            except Exception as e:
                st.error(f"Error loading model: {e}")
        
        if st.button("Complete CNN Analysis"):
            st.session_state.analysis_stage = "nlp"
            st.rerun()
    
    # NLP Stage (appears after CNN)
    elif st.session_state.analysis_stage == "nlp":
        st.subheader("📝 NLP Analysis (Sentiment & Emotion)")
        
        emotion_text = st.text_area(
            "Describe your feelings (max 100 characters):",
            placeholder="Type how you're feeling...",
            height=50,
            max_chars=100
        )
        
        if st.button("Share Your Feeling"):
            if emotion_text.strip():
                try:
                    # Load the NLP model
                    model_path = "models/NLP_ep15.h5"
                    nlp_model = load_model(model_path)
                    
                    # Create tokenizer from NLP.csv to match training (from nlp.ipynb)
                    nlp_csv = pd.read_csv("data/NLP.csv")
                    vocab_size = 10000
                    max_length = 150
                    
                    tokenizer = Tokenizer(num_words=vocab_size, oov_token="OOV")
                    tokenizer.fit_on_texts(nlp_csv['statement'].astype(str).values)
                    
                    # Tokenize and pad the input text (matching nlp.ipynb preprocessing)
                    text_sequences = tokenizer.texts_to_sequences([emotion_text.lower()])
                    text_padded = pad_sequences(text_sequences, maxlen=max_length, padding='post')
                    
                    # Flatten to match expected input shape (None, 9600)
                    text_flattened = text_padded.flatten().reshape(1, -1).astype(np.float32)
                    
                    # Make prediction
                    nlp_predictions = nlp_model.predict(text_flattened, verbose=0)
                    
                    # Emotion labels (matching emotion_map from nlp.ipynb: 6 classes)
                    emotion_labels = ['Surprise', 'Joy', 'Sadness', 'Anger', 'Fear', 'Love']
                    
                    # Get top 3 predictions
                    top_3_indices = np.argsort(nlp_predictions[0])[-3:][::-1]
                    
                    st.write("**Top 3 Emotion Predictions:**")
                    for rank, idx in enumerate(top_3_indices, 1):
                        emotion = emotion_labels[idx]
                        confidence = nlp_predictions[0][idx] * 100
                        st.write(f"{rank}. **{emotion}**: {confidence:.2f}%")
                    
                except Exception as e:
                    st.error(f"Error analyzing text: {e}")
            else:
                st.warning("Please describe how you're feeling!")
        
        if st.button("Start Over"):
            st.session_state.analysis_stage = "cnn"
            st.session_state.captured_photo = None
            st.session_state.predictions = None
            st.rerun()

