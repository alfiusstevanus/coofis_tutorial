from django.contrib.auth.models import update_last_login
from rest_framework import generics, status
from rest_framework.response import Response
from apps.accounts.serializers.auth_serializers import UserLoginSerializer, UserRefreshTokenSerializer, UserRegisterSerializer

class LoginGenericAPIView(generics.GenericAPIView):
    """user Login"""

    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        update_last_login(None, serializer.user)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response.set_cookie("refresh", str(serializer.data['token']['refresh']))
        return response

class RefreshGenericAPIView(generics.GenericAPIView):
    """refresh token"""

    serializer_class = UserRefreshTokenSerializer

    def post(self, request, *args, **kwargs):
        request.data["refresh"] = request.COOKIES.get("refresh")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.get_new_token(serializer.validated_data)
        update_last_login(None, serializer.user)
        return Response(result, status=status.HTTP_200_OK)
    
class LogoutGenericAPIView(generics.GenericAPIView):
    """user logout"""
    serializer_class = UserLoginSerializer

    def post(self, _):
        response = Response()
        response.delete_cookie(key="refresh")
        response.data = {"status": True, "details": {"message": "logout"}}
        response.status = status.HTTP_200_OK
        response.delete_cookie('jwt')
        return response

class RegisterGenericView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)