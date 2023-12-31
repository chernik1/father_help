from django.db import models

# Create your models here.

class ParserDelete(models.Model):

    id_purchase = models.CharField(max_length=10000, default='')

    def __str__(self):
        return f'{self.id_purchase}'

class Parser(models.Model):

    keyword = models.CharField(max_length=10000, default='')
    id_purchase = models.CharField(max_length=10000, default='')
    name_company = models.CharField(max_length=10000, default='')
    name_purchase = models.CharField(max_length=10000, default='')
    date = models.CharField(max_length=10000, default='')
    price = models.CharField(max_length=10000, default='')
    payer_number = models.CharField(max_length=10000, default='')
    location = models.CharField(max_length=10000, default='')
    forecast = models.CharField(max_length=4, default='Нету')

    def __str__(self):
        return f'{self.keyword} - {self.name_purchase}'


class ParserZaku(models.Model):

    keyword = models.CharField(max_length=10000, default='')
    url = models.URLField(max_length=10000)
    name_company = models.CharField(max_length=10000, default='')
    name_purchase = models.CharField(max_length=10000, default='')
    main_name_purchase = models.CharField(max_length=10000, default='')
    payer_number = models.CharField(max_length=10000, default='')
    price = models.CharField(max_length=10000, default='')
    location = models.CharField(max_length=10000, default='')
    forecast = models.CharField(max_length=4, default='Нету')

    def __str__(self):
        return f'{self.keyword} - {self.name_purchase}'

class ParserZakuDelete(models.Model):
    url = models.URLField(max_length=10000, default='')

    def __str__(self):
        return f'{self.url}'