import os

# import tensorflow as tf
from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = "api"

    def ready(self):
        return super().ready()
