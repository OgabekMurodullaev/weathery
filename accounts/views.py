from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import UserSerializer, UserLoginSerializer


class UserRegisterAPIView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'],
                                password=serializer.validated_data['password'])

            if user:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                data = {
                    "message": "You have successfully logged in",
                    "access": access_token,
                    "refresh": str(refresh),
                }
                return Response(data=data, status=status.HTTP_200_OK)
            return Response(data={"errors": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)