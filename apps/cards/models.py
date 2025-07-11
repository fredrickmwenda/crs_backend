from django.db import models

# Create your models here.
class Card(models.Model):
    card_number = models.CharField(max_length=50, unique=True)
    is_assigned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.card_number