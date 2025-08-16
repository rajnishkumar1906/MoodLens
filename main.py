# main.py
from tokenization import tokenize_text
from Embedding import get_embedding
from sentiment_classifier import analyze_sentiment
from utils import save_to_json

def process_input():
    results = []

    while True:
        text = input("\nEnter text to analyze (or type 'exit' to quit):\n")
        if text.lower() == "exit":
            break
        if not text.strip():
            print("Please enter some valid text!")
            continue

        # Tokenization & Embedding
        tokens = tokenize_text(text)
        embedding = get_embedding(tokens)

        # Sentiment analysis
        sentiment = analyze_sentiment(text)
        result = sentiment[0] if isinstance(sentiment, list) else sentiment

        # Show final result
        label = result['label'].lower()
        score = result['score']
        print(f"\nSentiment: {label.capitalize()} ({score:.2f})")

        # Save results
        results.append({
            "text": text,
            "token_ids": tokens['input_ids'].tolist(),
            "attention_mask": tokens['attention_mask'].tolist(),
            "embedding_shape": embedding.shape,
            "sentiment": result
        })

    if results:
        save_to_json(results, "post_sentiment.json")
        print(f"\nAll results saved to 'post_sentiment.json'.")

if __name__ == "__main__":
    process_input()
