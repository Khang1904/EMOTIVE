import os
import pandas as pd
import google.generativeai as genai
import streamlit as st
import json

def show_about_page():
    """Display the about page content"""
    st.title("ℹ️ About EMOTIVE")
    
    st.markdown("""
    EMOTIVE is an advanced emotion detection and analysis system that bridges the gap 
    between what you feel and how you express it.
    """)
    
    st.divider()
    
    # Goals, Targets & Use Cases
    st.markdown("## 🎯 Goals, Targets & Use Cases")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎪 Goals")
        st.markdown("""
        - Accurately detect emotions from facial expressions
        - Analyze emotional content in text
        - Provide empathetic AI-driven insights
        - Bridge visual and textual emotion understanding
        """)
    
    with col2:
        st.markdown("### 🎯 Target Users")
        st.markdown("""
        - Mental health practitioners
        - Customer service teams
        - UX researchers
        - Content creators
        - Anyone seeking emotional awareness
        """)
    
    with col3:
        st.markdown("### 💡 Use Cases")
        st.markdown("""
        - Emotional awareness training
        - Customer feedback analysis
        - Mental health support
        - User experience optimization
        - Sentiment analysis at scale
        """)
    
    st.divider()
    
    # Developer Story
    st.markdown("## 📖 The Developer's Journey")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🌟 How It Started",
        "🔬 Phase 1: Vision",
        "📝 Phase 2: Language",
        "🤖 Phase 3: Intelligence",
        "🎨 Phase 4: UX",
        "🎯 Lessons"
    ])
    
    with tab1:
        st.markdown("""
        ### The Beginning
        
        EMOTIVE was born from a simple question: *"Can AI truly understand how we feel?"*
        
        By combining cutting-edge computer vision and natural language processing, we set out to create 
        a system that doesn't just detect emotions, but understands them. Starting with pre-trained CNN models 
        on the FER2013 dataset for facial recognition, we expanded into text analysis using a custom NLP model 
        trained on real emotional expressions.
        
        The turning point came when we integrated Google's Generative AI—transforming raw predictions into 
        meaningful, empathetic conversations. Now, EMOTIVE doesn't just tell you *what* you're feeling; 
        it *understands why* and responds with genuine insight.
        """)
    
    with tab2:
        st.markdown("""
        ### Building the CNN Model
        
        **The Challenge**: Facial emotion recognition is notoriously difficult. Expressions are nuanced, 
        cultural contexts vary, and lighting conditions matter.
        
        **Our Approach**:
        - Leveraged the FER2013 dataset (35,887 images across 7 emotions)
        - Built a CNN architecture with Embedding layers, Batch Normalization, and Dropout
        - Trained for 50 epochs, carefully monitoring validation loss
        - Achieved robust predictions on: Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise
        
        **Key Insight**: Real-time emotion detection required preprocessing—converting images to grayscale, 
        resizing to 48x48, and normalizing pixel values. Speed and accuracy were both critical.
        """)
    
    with tab3:
        st.markdown("""
        ### Training the NLP Model
        
        **The Challenge**: Emotions expressed in text are even more abstract. Sarcasm, context, and cultural 
        references all matter. We needed a model that could capture emotional nuance in words.
        
        **Our Approach**:
        - Used the "Emotions Dataset for NLP" with 6 emotion categories (Surprise, Joy, Sadness, Anger, Fear, Love)
        - Implemented tokenization with a vocabulary of 10,000 words and max sequence length of 150
        - Applied embedding layers to convert words to dense vectors (64-dimensional)
        - Trained for 15 epochs with carefully tuned Dropout (0.5) to prevent overfitting
        
        **Key Insight**: LabelEncoder became our friend for maintaining consistent emotion mappings. 
        What the model learns during training must perfectly match what the app uses during inference.
        """)
    
    with tab4:
        st.markdown("""
        ### Generative AI Integration
        
        **The Challenge**: Raw emotion labels (7 from vision, 6 from text) are just numbers. 
        We needed to transform them into genuine, empathetic responses.
        
        **Our Approach**:
        - Integrated Google's Gemini 2.0 Flash API for real-time, intelligent responses
        - Designed a system prompt that considers both visual and textual emotions
        - Built a multi-turn chat interface to keep conversations natural and flowing
        - Added session state management to remember the emotional context
        
        **Key Insight**: AI responses are most powerful when they acknowledge *both* what you show 
        (facial expression) and what you say (textual description). This dual perspective creates 
        genuine understanding.
        """)
    
    with tab5:
        st.markdown("""
        ### Complete User Experience
        
        **The Challenge**: Multiple ML models, API calls, and session management had to work seamlessly 
        in a user-friendly interface.
        
        **Our Approach**:
        - Built a 3-stage workflow: Photo Capture → Text Input → AI Chat
        - Used Streamlit for rapid prototyping and real-time updates
        - Implemented robust error handling for model loading and API failures
        - Optimized image preprocessing for speed and accuracy
        - Added visual feedback (confidence scores, top-3 predictions)
        
        **The Result**: A seamless experience where users move from camera → description → conversation 
        without friction.
        """)
    
    with tab6:
        st.markdown("""
        ### Key Takeaways
        
        ✨ **Integration is Everything** - The hardest part wasn't building individual models; 
        it was making them work together seamlessly.
        
        ✨ **Session State Matters** - Tracking user progress through multiple stages 
        (capturing, analyzing, chatting) required careful state management.
        
        ✨ **Consistency is Key** - Emotion labels must match exactly between training and inference. 
        One mismatch can break the entire pipeline.
        
        ✨ **Context Amplifies AI** - Providing Generative AI with both visual and textual context 
        dramatically improves response quality.
        
        ✨ **Speed Requires Optimization** - Real-time predictions demand careful preprocessing 
        and model selection. Every millisecond counts.
        """)
    
    st.divider()
    
    # Tech Stack & Features Side by Side
    
    col_tech, col_features = st.columns(2)
    
    with col_tech:
        st.markdown("### ⚙️ Technology Stack")
        st.markdown("""
        **Frontend** • Streamlit (Interactive UI)
        
        **Vision** • TensorFlow/Keras • CNN Models (50 epochs) • PIL
        
        **NLP** • TensorFlow/Keras • Tokenizer + Embeddings • LabelEncoder • scikit-learn
        
        **AI** • Google Generative AI (Gemini 2.0)
        
        **Data** • Pandas • NumPy
        
        **Datasets** • FER2013 • Emotions Dataset for NLP
        """)
    
    with col_features:
        st.markdown("### 🌟 Features")
        st.markdown("""
        ✅ **Real-Time Detection** • Capture emotions via camera instantly
        
        ✅ **Multi-Modal Analysis** • Combines facial & textual emotion inputs
        
        ✅ **AI-Powered Chat** • Intelligent, empathetic responses
        
        ✅ **Accurate Classifications** • 7 facial + 6 text emotions
        
        ✅ **Confidence Scoring** • Transparency in predictions
        
        ✅ **Contextual Understanding** • Considers visual & text cues
        
        ✅ **Interactive Chat** • Ongoing dialogue with AI coach
        
        ✅ **Session Persistence** • Remember your emotional journey
        """)
    
    st.divider()
    
    # Project Impact
    st.markdown("## 🚀 Why EMOTIVE Matters")
    st.info("""
    In a world where emotional intelligence matters more than ever, EMOTIVE bridges the gap 
    between technology and human emotion. Whether you're seeking self-awareness, training AI systems, 
    or building empathetic products, EMOTIVE is your partner in understanding the human experience.
    """)
    
    st.divider()
    
    # Model Stats
    st.markdown("## 📊 Model Performance & Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔬 CNN Vision Model")
        
        perf_cols = st.columns(2)
        with perf_cols[0]:
            st.metric("Accuracy", "63.37%", "FER2013 Test Set")
            st.metric("Precision", "63.76%", "Weighted Avg")
        with perf_cols[1]:
            st.metric("Recall", "63.37%", "Weighted Avg")
            st.metric("F1-Score", "62.41%", "Weighted Avg")
    
    with col2:
        st.markdown("### 📝 NLP Text Model")
        
        perf_cols = st.columns(2)
        with perf_cols[0]:
            st.metric("Accuracy", "82.40%", "Test Set")
            st.metric("Precision", "83.05%", "Weighted Avg")
        with perf_cols[1]:
            st.metric("Recall", "82.40%", "Weighted Avg")
            st.metric("F1-Score", "82.56%", "Weighted Avg")
    

