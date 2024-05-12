import speech_recognition as sr
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Download NLTK data for tokenization and stop words
nltk.download("punkt")
nltk.download("stopwords")

# Load NLTK stop words
stop_words = set(stopwords.words("english"))

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

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
        print(f"Content {i + 1} Stemmed Text: {stemmed_text}")
    except sr.UnknownValueError:
        print(f"Content {i + 1} - Google Web Speech API could not understand audio.")
    except sr.RequestError as e:
        print(f"Content {i + 1} - Could not request results from Google Web Speech API; {e}")

print("Stemming complete.")