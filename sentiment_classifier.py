# sentiment_classifier.py
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import streamlit as st

# We will use a threshold to classify as 'Neutral' if confidence is low.
NEUTRAL_THRESHOLD = 0.65

@st.cache_resource
def load_model_and_tokenizer():
    """Loads and caches a pre-trained sentiment classification model and its tokenizer."""
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model_and_tokenizer()

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text using a pre-trained transformer model.
    It returns the sentiment label and a confidence score.
    """
    # Tokenize the input text and convert it into a format the model can use.
    tokens = tokenizer(text, return_tensors="pt")

    # Pass the tokens to the model to get the sentiment output.
    with torch.no_grad():
        outputs = model(**tokens)
        logits = outputs.logits
    
    # Use softmax to convert the raw model output (logits) into probabilities.
    probabilities = torch.nn.functional.softmax(logits, dim=1)
    
    # Get the index of the highest probability.
    predicted_class_id = torch.argmax(probabilities).item()
    
    # Get the score (confidence) for the predicted class.
    score = probabilities[0, predicted_class_id].item()

    # The model's output labels are 0 for negative and 1 for positive.
    # We add logic to handle a 'Neutral' sentiment.
    if score < NEUTRAL_THRESHOLD:
        sentiment = "NEUTRAL"
    elif predicted_class_id == 1:
        sentiment = "POSITIVE"
    else:
        sentiment = "NEGATIVE"
        
    return sentiment, score
