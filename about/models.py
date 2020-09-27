from django.db import models


class About(models.Model):
     title = models.CharField(max_length=150, verbose_name='Başlık')
     content = models.TextField(verbose_name='İçerik')
     image = models.ImageField(null=True, blank=True)

     def __str__(self):
         return self.title