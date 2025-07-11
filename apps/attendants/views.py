from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Attendant, CardAssignment
from apps.cards.models import Card
from .serializers import AttendantSerializer, AssignCardSerializer
from rest_framework.permissions import IsAuthenticated
from apps.cards.models import Card
from apps.users.permissions import IsAdminUser

class AttendantListCreateView(generics.ListCreateAPIView):
    queryset = Attendant.objects.all()
    serializer_class = AttendantSerializer
    permission_classes = [IsAdminUser]

class AttendantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendant.objects.all()
    serializer_class = AttendantSerializer
    permission_classes = [IsAdminUser]


class AssignCardView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]

    def post(self, request, pk):
        attendant = Attendant.objects.get(pk=pk)
        card_id = request.data.get("card_id")

        try:
            card = Card.objects.get(pk=card_id)
        except Card.DoesNotExist:
            return Response({"detail": "Card not found"}, status=404)

        if card.is_assigned:
            return Response({"detail": "Card already assigned"}, status=400)

        # Revoke current assignment
        current = CardAssignment.objects.filter(attendant=attendant, revoked_at__isnull=True).first()
        if current:
            current.revoked_at = timezone.now()
            current.card.is_assigned = False
            current.card.save()
            current.save()

        # Assign new
        CardAssignment.objects.create(attendant=attendant, card=card)
        card.is_assigned = True
        card.save()

        return Response({"detail": f"Card {card.card_number} assigned to {attendant.full_name}"}, status=200)

class RevokeCardView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]

    def post(self, request, pk):
        attendant = Attendant.objects.get(pk=pk)
        active = CardAssignment.objects.filter(attendant=attendant, revoked_at__isnull=True).first()
        if not active:
            return Response({"detail": "No active card found."}, status=400)

        active.revoked_at = timezone.now()
        active.card.is_assigned = False
        active.card.save()
        active.save()

        return Response({"detail": f"Card {active.card.card_number} revoked from {attendant.full_name}"})
