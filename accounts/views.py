

# from .serializers import RegisterUserSerializer, RegisterDriverSerializer
# from rest_framework import generics
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class RegisterUserView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterUserSerializer


# class RegisterDriverView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterDriverSerializer

from .serializers import RegisterUserSerializer, RegisterDriverSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

User = get_user_model()

class RegisterUserView(generics.ListCreateAPIView):  # يدعم GET و POST
    queryset = User.objects.all()  # يمكنك تصفيتها حسب الحاجة
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]

class RegisterDriverView(generics.ListCreateAPIView):  # يدعم GET و POST
    queryset = User.objects.all()  # يمكنك تصفيتها حسب الحاجة
    serializer_class = RegisterDriverSerializer
    permission_classes = [AllowAny]
