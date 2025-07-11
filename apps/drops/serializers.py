from rest_framework import serializers
from .models import DropFile, DropEntry

class DropEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DropEntry
        fields = ['id', 'card', 'attendant', 'drop_time', 'amount', 'matched']

class DropFileSerializer(serializers.ModelSerializer):
    entries = DropEntrySerializer(many=True, read_only=True)

    class Meta:
        model = DropFile
        fields = ['id', 'file', 'uploaded_at', 'processed', 'entries']
