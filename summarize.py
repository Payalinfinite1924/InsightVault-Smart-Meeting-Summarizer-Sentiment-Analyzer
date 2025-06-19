import whisper
from transformers import pipeline
from textblob import TextBlob
import json

model = whisper.load_model("base")
summarizer = pipeline("summarization")

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def extract_action_items(text):
    lines = text.split('.')
    return [line.strip() for line in lines if 'will' in line or 'must' in line or 'need to' in line]

def process_meeting(audio_path):
    result = model.transcribe(audio_path)
    text = result['text']

    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    sentiment_score = get_sentiment(text)
    sentiment = "Positive" if sentiment_score > 0.2 else "Negative" if sentiment_score < -0.2 else "Neutral"
    action_items = extract_action_items(text)

    report = {
        "summary": summary,
        "sentiment": sentiment,
        "action_items": action_items,
        "full_text": text
    }

    return json.dumps(report, indent=4)
