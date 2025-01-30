from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import UserRegisterAPIView, UserLoginAPIView

urlpatterns = [
    path('login/', UserLoginAPIView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('register/', UserRegisterAPIView.as_view()),
]