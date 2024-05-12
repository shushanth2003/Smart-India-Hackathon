# Audio to Text Transcription with Sentiment Analysis

This repository contains Python code for converting audio recordings into text transcripts using speech recognition, segmenting the audio content, and performing sentiment analysis on each segment.

## Dependencies

Before running the code, make sure you have the following dependencies installed:

- Python 3.x
- `pyaudio`
- `wave`
- `librosa`
- `matplotlib`
- `pydub`
- `speech_recognition`
- `nltk`
- `textblob`

You can install the required dependencies using `pip`:

```bash
pip install pyaudio wave librosa matplotlib pydub SpeechRecognition nltk textblob
```

## Usage

1. Run the `record_audio.py` script to record audio from your microphone. Adjust the `RECORD_SECONDS` variable in the script to set the maximum recording time. The recorded audio will be saved as `recorded_audio.wav`.

2. Run the `segment_audio.py` script to split the recorded audio into individual segments based on silence. Adjust the `min_silence_length` parameter in the script to control the minimum length of silence required to consider it as a content break. The segmented audio files will be saved as `content_i.wav`, where `i` represents the segment number.

3. Run the `transcribe_audio.py` script to transcribe each audio segment into text using Google Web Speech API. The transcribed text for each segment will be displayed in the console.

4. (Optional) Run the `stemming.py` script to perform stemming on the transcribed text and print the stemmed text for each segment.

5. (Optional) Run the `sentiment_analysis.py` script to perform sentiment analysis on each segment using TextBlob. The sentiment classification (positive, negative, neutral) for each segment will be displayed in the console.

## Example

Here's an example of how you can use the code:

```bash
python record_audio.py
python segment_audio.py
python transcribe_audio.py
python stemming.py
python sentiment_analysis.py
```
