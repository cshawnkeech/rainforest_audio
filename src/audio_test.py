import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np

# import os


file = 'capstones/rainforest_audio/data/rfcx-species-audio-detection/train/0a4e7e350.flac'

# waveform

# np 1d array sample rate * duration of song...
# so sr * T --> 22050 * 30
signal, sr = librosa.load(file, sr=22050)

print(sr)

# Audio waveform
# librosa.display.waveplot(signal, sr=sr)
# plt.xlabel("time")
# plt.ylabel("amplitude")
# plt.show()

# print("i'm printing")
# print(os.getcwd())

# fft -> spectrum
# number of values = number of samples in wavform..
# with complex values, get magnitude of these values
fft = np.fft.fft(signal)

magnitude = np.abs(fft)  # gets magnitude for frequency

# map to relative frequency
# magnitude per each frequency bin
frequency = np.linspace(0, sr, len(magnitude))  # evenly spaced interval

# plt.plot(frequency, magnitude)
# plt.xlabel('frequency')
# plt.ylabel('magnitude')
# this will give a symmetric image w mirror images on r and left of frame...
# only need first half
# plt.show()

left_frequency = frequency[:int(len(frequency)/2)]
left_magnitude = magnitude[:int(len(magnitude)/2)]

# plt.plot(left_frequency, left_magnitude)
# plt.xlabel('frequency')
# plt.ylabel('magnitude')
# # this will return left half
# plt.show()

# this is only a snapshot...

# stft -> spectrogram
# number of samples per fft
# size of window for each single fft
n_fft = 2048  # in number of samples
hop_length = 512  # in number of samples
stft = librosa.core.stft(signal,
                         hop_length=hop_length,
                         n_fft=n_fft)

spectrogram = np.abs(stft)

# librosa.display.specshow(spectrogram,
#                          sr=sr,
#                          hop_length=hop_length)
# plt.xlabel('time')
# plt.ylabel('frequency')
# plt.show()

log_spectrogram = librosa.amplitude_to_db(spectrogram)

# librosa.display.specshow(log_spectrogram,
#                          sr=sr,
#                          hop_length=hop_length)
# plt.xlabel('time')
# plt.ylabel('frequency')
# plt.colorbar()
# plt.show()

MFCCs = librosa.feature.mfcc(signal, 
                             n_fft=n_fft, 
                             hop_length=hop_length, 
                             n_mfcc=13)

librosa.display.specshow(MFCCs,
                         sr=sr,
                         hop_length=hop_length)
plt.xlabel('time')
plt.ylabel('MFCC Coefficients')
plt.colorbar()
plt.show()
