
# **MoodLens: Transformer-Powered Sentiment Analyzer**

**MoodLens** is an interactive web application that harnesses the power of pre-trained transformer models to perform accurate sentiment analysis on any user-provided text. Built with **Python**, **Streamlit**, and **Hugging Face Transformers**, MoodLens demonstrates the capabilities of modern NLP in a clean, intuitive interface.

---

## ✨ **Features**

* **Real-time Sentiment Analysis**: Instantly classify text as **positive**, **negative**, or **neutral**.
* **Confidence Scoring**: Receive a numerical confidence score for each prediction.
* **User-Friendly Interface**: A sleek, interactive **Streamlit** UI for seamless interaction.
* **Modular Architecture**: Structured Python files for clarity, maintainability, and reusability.

---

## 🚀 **Getting Started**

### **Prerequisites**

* Python 3.8+ installed on your system.
* Recommended: Use a **virtual environment** for dependency management.

### **Installation**

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is empty, manually install:

```bash
pip install streamlit transformers torch
```

---

### **Running the Application**

**1. Streamlit Web App**
Launch the interactive web app in your browser:

```bash
streamlit run app.py
```

**2. Command-Line Interface (CLI)**
For terminal-based interaction:

```bash
python main.py
```

Enter text for analysis. Type `exit` to quit.

---

## 📂 **Project Structure**

| File                      | Description                                                         |
| ------------------------- | ------------------------------------------------------------------- |
| `app.py`                  | Main Streamlit application handling the web UI                      |
| `main.py`                 | CLI interface for sentiment analysis                                |
| `sentiment_classifier.py` | Core logic for loading the pre-trained model and making predictions |
| `tokenization.py`         | Handles tokenization of input text                                  |
| `embedding.py`            | Generates vector representations (embeddings) of text               |
| `utils.py`                | Utility functions, including saving results to JSON                 |
| `post_sentiment.json`     | Sample output file                                                  |
| `requirements.txt`        | Lists project dependencies                                          |

---

MoodLens is the perfect starting point for exploring NLP, sentiment analysis, and transformer models in an interactive and practical way.

---
