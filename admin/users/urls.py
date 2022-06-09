from django.contrib import admin
from django.urls import path
# from .views import register, login, logout, AuthenticatedUser, PermissionAPIView, RoleViewSet
from .views import users, register

# urlpatterns = [
    # path('register/', register),
    # path('login/', login),
    # path('logout/', logout),
    # path('user/', AuthenticatedUser.as_view()),
    # path('permissions/', PermissionAPIView.as_view()),
    # path('roles/', RoleViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create',
    # })),
    # path('role/<str:pk>', RoleViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'delete'
    # }))
# ]

urlpatterns = [
    path('users/', users),
    path('register/', register)
]