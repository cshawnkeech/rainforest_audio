# import os

# import librosa

import tensorflow as tf
# from tensorflow import keras
# import tensorflow_io as tfio

# System filepath setup
import sys

# add data folders to path
sys.path.insert(1, '../data')
sys.path.insert(1, '../src')
sys.path.insert(1, '../img')

# this import has sto follow sytem filepath setup...
import src.audio_prep as a_prep


mel_model = tf.keras.models.load_model('../data/saved_models/mel_1_sec_model_96acc/mel_1_sec_96_model')

# Check its architecture
# mel_model.summary()


def get_pred(audio_chunk):
    '''
    input:
        audio_chunk of 48kHz, 1 second of audio

    returns:
        nparray
    '''
    a_prepped = a_prep.mel_1s_snapshot(audio_chunk)

    return mel_model.predict(a_prepped)
