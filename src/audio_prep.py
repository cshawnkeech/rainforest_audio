import tensorflow as tf
from tensorflow import keras
import tensorflow_io as tfio


def mel_1s_snapshot(input):

    audio_tensor = tf.squeeze(input, axis=[-1])

    tensor = tf.cast(audio_tensor, tf.float32)

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
        fmax=11627.90) # 15000)
    
    return mel_spectrogram