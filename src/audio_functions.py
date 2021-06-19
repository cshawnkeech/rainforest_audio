'''
Code Adjusted From...
https://gist.github.com/mabdrabo/8678538




'''

import pyaudio
import wave

import matplotlib.pyplot as plt

import os
import struct
import numpy as np

import time
from tkinter import TclError


def record_short(record_seconds=5):
    dev_index = 0 # should be built in mic
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 # lav only has one channel...
    RATE = 44100 #44100
    CHUNK = 1024
    RECORD_SECONDS = record_seconds
    WAVE_OUTPUT_FILENAME = "file.wav"
    
    # device index found by p.get_device_info_by_index(ii)

    audio = pyaudio.PyAudio()

    # print available microphones
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))



    # start Recording
    stream = audio.open(
        input_device_index=dev_index,
        format=FORMAT, 
        channels=CHANNELS,
        rate=RATE, 
        input=True,
        frames_per_buffer=CHUNK)
    
    
    print ("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print ("finished recording")


    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close() 


def stream_seconds(how_long=1):

    '''
    Adapted
    
    https://github.com/markjay4k/Audio-Spectrum-Analyzer-in-Python/blob/master/audio%20spectrum_pt1_waveform_viewer.ipynb
    '''

    FORMAT = pyaudio.paFloat32
    CHANNELS = 1  # lav only has one channel...
    RATE = 44100  # 44100
    CHUNK = 1024 * 4 # one second worth of audio at a time....This may be far too large...
    dev_index = 0
    
    # print available microphones
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):

        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:

            print("Input Device id ", i, " - ",
                  p.get_device_info_by_host_api_device_index(0, i).get('name'))

#     # create matplotlib figure and axes
#     fig, ax = plt.subplots(1, figsize=(15, 7))

    # pyaudio class instance
    p = pyaudio.PyAudio()
    


    # stream object to get data from microphone
    stream = p.open(
        input_device_index=dev_index, # my device
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        output=True,
        frames_per_buffer=CHUNK
    )

    data = stream.read(CHUNK)

    print(data)



#     # variable for plotting
#     x = np.arange(0, 2 * CHUNK, 2)

#     # create a line object with random data
#     line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)

#     # basic formatting for the axes
#     plt.bar([x for x in range(24)], tf.nn.softmax(prediction[1]))
#     plt.xticks(ticks = [i for i in range(24)], labels=[str(i) for i in range(24)])
#     plt.title('Which Species?')
#     plt.ylabel('Probability')
#     plt.xlabel('Species')
#     plt.ylim(0,1)
#     # show the plot
#     plt.show(block=False)

#     print('stream started')

#     # for measuring frame rate
#     frame_count = 0
#     start_time = time.time()

    while how_long > 0:

        print(f"how_long")

#         # binary data
#         data = stream.read(CHUNK)  

#         # convert data to integers, make np array, then offset it by 127
#         data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

#         # create np array and offset by 128
#         data_np = np.array(data_int, dtype='b')[::2] + 128

#         line.set_ydata(data_np)

#         # update figure canvas
#         try:
#             fig.canvas.draw()
#             fig.canvas.flush_events()
#             frame_count += 1

#         except TclError:

#             # calculate average frame rate
#             frame_rate = frame_count / (time.time() - start_time)

#             print('stream stopped')
#             print('average frame rate = {:.0f} FPS'.format(frame_rate))
#             break
        
        how_long -= 1