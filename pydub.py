from pydub import AudioSegment
from pydub.silence import split_on_silence
import pydub.playback as playback

# Load the recorded audio file
audio = AudioSegment.from_wav("recorded_audio.wav")

# Define the minimum length of silence (in milliseconds) to consider as a content break
min_silence_length = 1000  # Adjust as needed

# Split the audio based on silence
content_segments = split_on_silence(audio, min_silence_len=min_silence_length, silence_thresh=-40) # Adjust silence threshold as needed

# Play each content segment and export it as a separate audio file
for i, segment in enumerate(content_segments):
    print(f"Playing Content {i + 1}")
    playback.play(segment)
    segment.export(f"content_{i}.wav", format="wav")

print("Audio content separated and saved as individual files.")