from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.db import models

# Create your models here.

class FoodEntry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField(help_text="kcal")

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"
