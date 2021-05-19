import os

DATASET_PATH = 'genre_dataset_reduced'
JSON_PATH = 'data.json'

def save_mfcc(dataset_path, json_path, n_mfcc=13, n_fft=2048, hop_length=512, num_segments=5):
    '''
    num_segments: chop up each file into multiple segments

    '''

    data = {
        "mapping": list(), # these will be the human-readable titles for each label
        "mfcc": list(), # these will be the training inputs
        "labels": list(), # these will be the labels
    }

    # loop through all the files
    for i, dirpath, dirnames, filenames in enumerate(os.walk(dataset_path)):

        # ensure that we're not at the root level...
        if dirpath is not dataset_path:

            pass

