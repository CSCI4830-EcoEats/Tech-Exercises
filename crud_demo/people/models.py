from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"
