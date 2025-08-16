# app.py
import streamlit as st
from sentiment_classifier import analyze_sentiment

# --- Streamlit UI ---

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: linear-gradient(to right, #e0f7fa, #b3e5fc);
    }
    [data-testid="stSidebar"] {
        background-image: linear-gradient(to right, #b3e5fc, #e0f7fa);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("MoodLens: Transformer-Powered Sentiment Analyzer")

# --- Container for the 'About This App' section ---
about_container = st.container()
with about_container:
    st.header("About This App")
    st.write(
        """
        MoodLens is an interactive web application that uses a pre-trained transformer model 
        to analyze the sentiment of a given text. It is built to demonstrate the power of 
        modern natural language processing (NLP) in a simple and intuitive way.
        """
    )
    st.markdown("---")


with st.sidebar:
    st.header("Text Input")
    user_text = st.text_area("Enter your text here to analyze its sentiment:", height=200)
    analyze_button = st.button("Analyze Text")

# --- Container for the analysis results ---
results_container = st.container()

if analyze_button:
    if user_text:
        with st.spinner('Analyzing...'):
            try:
                sentiment, score = analyze_sentiment(user_text)

                with results_container:
                    st.header("Analysis Result")
                    st.metric(label="Sentiment Score", value=f"{score:.2f}")

                    if sentiment == "POSITIVE":
                        st.success(f"Sentiment: **Positive** 😊")
                    elif sentiment == "NEGATIVE":
                        st.error(f"Sentiment: **Negative** 😠")
                    else:
                        st.info(f"Sentiment: **Neutral** 😐")

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to analyze.")