import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load an audio file
audio_file = "recorded_audio.wav"
y, sr = librosa.load(audio_file)

# Create and display a spectrogram
plt.figure(figsize=(10, 4))
librosa.display.specshow(librosa.amplitude_to_db(librosa.stft(y), ref=np.max),
                         y_axis='log', x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()