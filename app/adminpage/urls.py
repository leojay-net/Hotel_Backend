from django.urls import path
from .views import (AddAdminUser, CreateUser, AdminUsers, RemoveAdminUser)
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('add_user/', CreateUser.as_view(), name="add-user"),
    path('add_admin/<str:pk>', AddAdminUser.as_view(), name="add-admin"),
    path('remove_admin/<str:pk>', RemoveAdminUser.as_view(), name="add-admin"),
    path('admin_users/', AdminUsers.as_view(), name="all-admin"),
    path('register/',views.RegisterView.as_view(),name="register"),
    path('login/',views.LoginAPIView.as_view(),name="login"),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]