from django.urls import re_path

from .views import Predict

urlpatterns = [
    re_path(r"^$", Predict.as_view()),
]
