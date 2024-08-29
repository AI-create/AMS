# from rest_framework.permissions import BasePermission, SAFE_METHODS

# class IsAdminOrReadOnly(BasePermission):
#     """
#     Custom permission to only allow admins to edit or delete an object, but
#     allow read-only access for everyone else.
#     """

#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         return request.user.is_staff or request.user.is_superuser
