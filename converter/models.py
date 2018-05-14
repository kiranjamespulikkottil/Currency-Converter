from django.db import models
from django.urls import reverse

class Conversion(models.Model):
    CURRENCY = (('USD', 'USD'), ('EUR', 'EUR'), ('INR', 'INR'), ('SGD', 'SGD'), ('GBP', 'GBP'))
    from_currency = models.CharField(max_length=100, choices=CURRENCY, default='INR')
    value = models.FloatField()
    to_currency = models.CharField(max_length=100, choices=CURRENCY, default='INR')
    converted_value = models.FloatField()


    def get_absolute_url(self):
        return reverse('home')

class History(models.Model):
    user_name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    history = models.TextField()
