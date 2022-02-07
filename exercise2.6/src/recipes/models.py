from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    instructions = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})
