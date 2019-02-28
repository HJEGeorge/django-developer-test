from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)
    # Salary
    # Postcodes & Dates
    # PDF Upload
