from django.db import models
from apps.cards.models import Card

class Attendant(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

class CardAssignment(models.Model):
    attendant = models.ForeignKey(Attendant, on_delete=models.CASCADE, related_name='card_assignments')
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    revoked_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-assigned_at']

    def __str__(self):
        return f"{self.card.card_number} → {self.attendant.full_name}"
