from rest_framework.permissions import BasePermission



class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'admin'
    
    
# class IsAdminOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in ['GET']:
#             return True
#         return request.user and request.user.role == 'admin'
