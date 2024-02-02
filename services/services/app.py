import os
import tensorflow as tf
from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):
    name = "api"
    model_path = os.path.join(settings.MODEL_STORAGE, "phishing_model.h5")
    model = tf.keras.models.load_model(model_path)
