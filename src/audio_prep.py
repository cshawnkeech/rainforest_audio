import tensorflow as tf
from tensorflow import keras
import tensorflow_io as tfio

import numpy as np

import os

# System filepath setup
import sys

# add data folders to path
sys.path.insert(1, '../data')
sys.path.insert(1, '../src')
sys.path.insert(1, '../img')


def mel_1s_snapshot(input):
    
    sr = 48000
    
    a_tensor = tf.convert_to_tensor(input, dtype=tf.float32)

    tensor = tf.cast(a_tensor, tf.float32)


    spectrogram = tfio.experimental.audio.spectrogram(
        tensor,
        nfft=512,
        window=512,
        stride=256
    )

    mel_spectrogram = tfio.experimental.audio.melscale(
        spectrogram, 
        rate=sr, 
        mels=128, 
        fmin=93.75,     # 20, 
        fmax=13687.5) # 15000)
    
    reshape = tf.expand_dims(mel_spectrogram.numpy(), -1)
    
    return np.array(reshape)

