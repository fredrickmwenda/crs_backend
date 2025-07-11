# apps/attendants/serializers.py

from .models import Attendant, CardAssignment
from apps.cards.models import Card
from rest_framework import serializers

class CardAssignmentSerializer(serializers.ModelSerializer):
    card_number = serializers.CharField(source='card.card_number', read_only=True)

    class Meta:
        model = CardAssignment
        fields = ['id', 'card', 'card_number', 'assigned_at', 'revoked_at']

class AttendantSerializer(serializers.ModelSerializer):
    current_card = serializers.SerializerMethodField()
    assignment_history = CardAssignmentSerializer(source='card_assignments', many=True, read_only=True)

    class Meta:
        model = Attendant
        fields = ['id', 'full_name', 'email', 'phone_number', 'is_active', 'current_card', 'assignment_history']

    def get_current_card(self, obj):
        active = obj.card_assignments.filter(revoked_at__isnull=True).first()
        return active.card.card_number if active else None
