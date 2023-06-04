import numpy as np
import soundfile as sf

def generate_random_pitch(duration, sample_rate):
    num_samples = int(duration * sample_rate)
    num_segments = int(duration / 0.25)  # Number of 0.25-second segments
    segment_samples = int(sample_rate * 0.25)  # Number of samples in each segment

    frequencies = np.random.uniform(80, 1000, num_segments)  # Random frequencies between 80 and 1000 Hz

    signal = np.empty(num_samples)
    for i in range(num_segments):
        start_sample = i * segment_samples
        end_sample = (i + 1) * segment_samples
        t = np.linspace(0, 0.25, segment_samples, endpoint=False)
        segment_signal = np.sin(2 * np.pi * frequencies[i] * t)
        signal[start_sample:end_sample] = segment_signal

    return signal

def save_audio_file(filename, signal, sample_rate):
    sf.write(filename, signal, sample_rate, 'PCM_24')

# Parameters
duration = 5  # Duration of the audio in seconds
sample_rate = 44100  # Number of samples per second (standard for audio)

# Generate random pitch sequence
signal = generate_random_pitch(duration, sample_rate)

# Save the signal as an audio file
filename = 'random_pitch_sequence.wav'
save_audio_file(filename, signal, sample_rate)

print(f"Audio file '{filename}' generated.")
