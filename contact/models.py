from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=150, verbose_name='İsim')
    email = models.CharField(max_length=150, verbose_name='email')
    topic = models.CharField(max_length=150, verbose_name='Konu')
    content = models.TextField(verbose_name='İçerik')