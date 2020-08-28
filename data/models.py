from django.db import models

# Create your models here.


class Info(models.Model):
    day = models.DateField()
    country_abr = models.CharField(max_length=10)
    country = models.CharField(max_length=70)
    region = models.CharField(max_length=10)
    deaths = models.IntegerField()
    cum_deaths = models.IntegerField()
    confirmed = models.IntegerField()
    cum_confirmed = models.IntegerField()

    def __str__(self):
        return self.country


class world(models.Model):
    day = models.DateField()
    deaths = models.IntegerField()
    cum_deaths = models.IntegerField()
    confirmed = models.IntegerField()
    cum_confirmed = models.IntegerField()

    def __str__(self):
        return str(self.day)


class active_countrie(models.Model):
    country_abr = models.CharField(max_length=10)
    country = models.CharField(max_length=70)

    def __str__(self):
        return self.country_abr


class all_countrie(models.Model):
    coun_abr = models.CharField(max_length=10)
    coun = models.CharField(max_length=70)

    def __str__(self):
        return self.coun_abr
