from django.db import models


class BlackList(models.Model):
    class Meta:
        db_table = "black_list"

    name = models.CharField(null=True, blank=True, max_length=255, default="")
    url = models.TextField(null=True, blank=True, default="")


class WhiteList(models.Model):
    class Meta:
        db_table = "white_list"

    name = models.CharField(null=True, blank=True, max_length=255, default="")
    url = models.TextField(null=True, blank=True, default="")
