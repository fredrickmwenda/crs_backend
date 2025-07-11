from django.db import models
from apps.attendants.models import Attendant
from apps.cards.models import Card

class DropFile(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='drops/')
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"DropFile {self.id} ({self.file.name})"

class DropEntry(models.Model):
    drop_file = models.ForeignKey(DropFile, on_delete=models.CASCADE, related_name='entries')
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True)
    attendant = models.ForeignKey(Attendant, on_delete=models.SET_NULL, null=True, blank=True)
    drop_time = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    matched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.card} - {self.amount} @ {self.drop_time}"
