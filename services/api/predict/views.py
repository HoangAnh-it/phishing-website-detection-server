from rest_framework import generics, response, status

import services.settings as settings
import requests
from services.app import ApiConfig
from .utils import preprocess_input
import numpy as np


class Predict(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        model = ApiConfig.model
        body = request.data
        url = body["url"]
        try:
            res = requests.get(url)
            if res.status_code == status.HTTP_200_OK:
                html = res.text
                url_input, html_input = preprocess_input(url, html)
                predict = model.predict([np.array(url_input), np.array(html_input)])[0][0]
                threshold = 0.5
                return response.Response(
                    {
                        "predict": predict,
                        "threshold": threshold,
                    }
                )

            raise Exception("Unknown website")

        except Exception as e:
            print(e)
            return response.Response(
                {"message": "Cannot access this website."},
                status=status.HTTP_400_BAD_REQUEST,
            )
