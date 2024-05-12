import speech_recognition as sr
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from textblob import TextBlob
import os
import matplotlib.pyplot as plt

# Initialize the recognizer
recognizer = sr.Recognizer()


# Load NLTK stop words
stop_words = set(stopwords.words("english"))

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# Initialize counters for sentiment classification
positive_count = 0
negative_count = 0
neutral_count = 0

# Lists to store sentiment labels for each content segment
sentiment_labels = []

# Iterate over the separated audio segments
for i in range(len(content_segments)):
    audio_file_path = f"content_{i}.wav"

    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        # Use the Google Web Speech API to transcribe the audio
        text = recognizer.recognize_google(audio_data)

        # Tokenize the transcribed text
        tokens = word_tokenize(text)

        # Remove stop words and perform stemming
        filtered_tokens = [stemmer.stem(word) for word in tokens if word.lower() not in stop_words]

        # Reconstruct the text from stemmed tokens
        stemmed_text = " ".join(filtered_tokens)

        # Perform sentiment analysis using TextBlob
        analysis = TextBlob(stemmed_text)
        sentiment = analysis.sentiment

        # Classify sentiment as positive, negative, or neutral
        if sentiment.polarity > 0.1:
            sentiment_label = "Positive"
            positive_count += 1
        elif sentiment.polarity < -0.1:
            sentiment_label = "Negative"
            negative_count += 1
        else:
            sentiment_label = "Neutral"
            neutral_count += 1

        sentiment_labels.append(sentiment_label)

        print(f"Content {i + 1} Stemmed Text: {stemmed_text}")
        print(f"Content {i + 1} Sentiment: Polarity = {sentiment.polarity:.2f}, Subjectivity = {sentiment.subjectivity:.2f}")
        print(f"Content {i + 1} Sentiment Classification: {sentiment_label}\n")
    except sr.UnknownValueError:
        print(f"Content {i + 1} - Google Web Speech API could not understand audio.")
    except sr.RequestError as e:
        print(f"Content {i + 1} - Could not request results from Google Web Speech API; {e}")