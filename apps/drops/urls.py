from django.urls import path
from .views import DropFileUploadView, DropEntryListView

urlpatterns = [
    path('upload/', DropFileUploadView.as_view(), name='drop-upload'),
    path('entries/', DropEntryListView.as_view(), name='drop-entries'),
]
