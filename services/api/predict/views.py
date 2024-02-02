from rest_framework import generics, response, status

import services.settings as settings
import requests
from services.app import AppConfig
from .utils import preprocess_input
import numpy as np


class Predict(generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        model = AppConfig.model
        body = request.data
        url = body["url"]
        res = requests.get(url)
        if res.status_code == status.HTTP_200_OK:
            html = res.text
            url_input, html_input = preprocess_input(url, html)
            predict = model.predict([np.array(url_input), np.array(html_input)])
            return response.Response(
                {
                    "predict": predict,
                    "url": url,
                }
            )

        print(res)
        return response.Response(
            {
                "predict": 0,
                "url": url,
            }
        )

    def get(self, request, *args, **kwargs):
        return response.Response("OK")
