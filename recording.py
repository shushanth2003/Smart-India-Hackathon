import pyaudio
import wave

# Constants for audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Number of frames per buffer
RECORD_SECONDS = 300  # Maximum recording time in seconds (adjust as needed)
OUTPUT_FILENAME = "recorded_audio.wav"

audio = pyaudio.PyAudio()

# Create an audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording... Press Ctrl+C to stop.")

frames = []

try:
    while True:
        data = stream.read(CHUNK)
        frames.append(data)
except KeyboardInterrupt:
    print("Recording stopped.")

# Close and terminate the audio stream
stream.stop_stream()
stream.close()
audio.terminate()