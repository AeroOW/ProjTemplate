from django.db import models


class Esport(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    developer = models.CharField(max_length=70, blank=False, default='')
    type = models.CharField(max_length=70, blank=False, default='PC/Console')
    prize_pool = models.CharField(max_length=70, blank=False, default='')
    peak_viewership = models.CharField(max_length=70, blank=False, default='')
