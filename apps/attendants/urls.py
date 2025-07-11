# apps/attendants/urls.py

from django.urls import path
from .views import AssignCardView, RevokeCardView, AttendantListCreateView, AttendantRetrieveUpdateDestroyView

urlpatterns = [
    path('', AttendantListCreateView.as_view(), name='attendant-list-create'),
    path('<int:pk>/', AttendantRetrieveUpdateDestroyView.as_view(), name='attendant-detail'),
    path('<int:pk>/assign-card/', AssignCardView.as_view(), name='assign-card'),
    path('<int:pk>/revoke-card/', RevokeCardView.as_view(), name='revoke-card'),
]
