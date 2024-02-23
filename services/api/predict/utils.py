import pickle, os
import services.settings as settings
import pandas as pd
import numpy as np
from keras.utils import pad_sequences

mine_max_url_size = 250
mine_max_html_size = 2500


def preprocess_input(url, html):
    url_tokenizer = None
    html_tokenizer = None
    with open(os.path.join(settings.MODEL_STORAGE, "url_tokenizer.pickle"), "rb") as handle:
        url_tokenizer = pickle.load(handle)

    with open(os.path.join(settings.MODEL_STORAGE, "html_tokenizer.pickle"), "rb") as handle:
        html_tokenizer = pickle.load(handle)

    url_sequences = url_tokenizer.texts_to_sequences([url])
    html_sequences = html_tokenizer.texts_to_sequences([html])
    mine_url_sequences = pad_sequences(url_sequences, maxlen=mine_max_url_size, padding="post")
    mine_html_sequences = pad_sequences(html_sequences, maxlen=mine_max_html_size, padding="post")
    return mine_url_sequences, mine_html_sequences
