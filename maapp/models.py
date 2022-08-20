from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200, default=' uma sring')
    preço = models.FloatField(default=0.0)
    quantidade= models.IntegerField(default=0)
    total = models.FloatField(default=0.0)

