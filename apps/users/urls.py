from django.urls import path
from .views import AdminCreateUserView, UserListView, ProfileView, UserDetailView, UserUpdateView, UserDeleteView, UserSelfUpdateView, ChangePasswordView
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
   
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('me/', ProfileView.as_view(), name='user-profile'),
    path('me/update/', UserSelfUpdateView.as_view(), name='user-self-update'),
    path('me/change-password/', ChangePasswordView.as_view(), name='user-change-password'),

    # Admin only
    path('users/', UserListView.as_view(), name='user-list'),
    path('create/', AdminCreateUserView.as_view(), name='user-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
