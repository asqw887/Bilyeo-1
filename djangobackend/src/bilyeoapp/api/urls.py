from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import (
	UserCreateView,
)

urlpatterns = [
    path('register/', UserCreateView.as_view()),
    path('home/login/token/', obtain_jwt_token),
]
