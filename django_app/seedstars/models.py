from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    email = models.EmailField(max_length=150, primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.email
