
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer
from rest_framework import viewsets
from django.contrib.auth import get_user_model

User = get_user_model()


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = ()
    serializer_class = RegisterSerializer

