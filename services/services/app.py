import os
import tensorflow as tf
from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):
    name = "api"
    config_model = os.path.join(settings.MODEL_STORAGE, "model.json")
    weight_model = os.path.join(settings.MODEL_STORAGE, "model_weight.h5")
    model = None
    with open(config_model, "r") as json_file:
        model_json = json_file.read()
        model = tf.keras.models.model_from_json(model_json)

    print(model.summary())
    model.load_weights(weight_model)
