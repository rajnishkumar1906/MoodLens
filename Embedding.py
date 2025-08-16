# embedding.py
from transformers import AutoModel
import torch
import streamlit as st

@st.cache_resource
def get_model():
    """Loads and caches the transformer model."""
    return AutoModel.from_pretrained("bert-base-uncased")

# Load the model
model = get_model()

def get_embedding(tokens):
    """Generates an embedding for the input tokens."""
    with torch.no_grad():
        outputs = model(**tokens)
        cls_embedding = outputs.last_hidden_state[:, 0, :]
    return cls_embedding
