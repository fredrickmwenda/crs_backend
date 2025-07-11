import csv
from django.utils.dateparse import parse_datetime
from rest_framework.parsers import MultiPartParser
from rest_framework import generics, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import DropFile, DropEntry
from .serializers import DropFileSerializer, DropEntrySerializer
from apps.cards.models import Card
from apps.attendants.models import Attendant

class DropEntryListView(generics.ListAPIView):
    queryset = DropEntry.objects.select_related('card', 'attendant', 'drop_file')
    serializer_class = DropEntrySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['attendant', 'card', 'matched', 'drop_file']
    search_fields = ['attendant__full_name', 'card__card_number']
    ordering_fields = ['drop_time', 'amount']
    ordering = ['-drop_time']

class DropFileUploadView(generics.CreateAPIView):
    serializer_class = DropFileSerializer
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        drop_file = DropFile.objects.create(file=uploaded_file)

        decoded = uploaded_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded)

        for row in reader:
            card_number = row.get('card_number')
            try:
                card = Card.objects.get(card_number=card_number)
            except Card.DoesNotExist:
                card = None

            attendant = None
            if card:
                active_assignment = card.cardassignment_set.filter(revoked_at__isnull=True).first()
                if active_assignment:
                    attendant = active_assignment.attendant

            DropEntry.objects.create(
                drop_file=drop_file,
                card=card,
                attendant=attendant,
                drop_time=parse_datetime(row['drop_time']),
                amount=row['amount'],
                matched=bool(attendant),
            )

        drop_file.processed = True
        drop_file.save()

        return Response(DropFileSerializer(drop_file).data, status=status.HTTP_201_CREATED)

