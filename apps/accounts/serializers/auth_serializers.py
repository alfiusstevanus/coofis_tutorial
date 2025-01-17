import jwt
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from apps.accounts.models import User

class UserLoginSerializer(TokenObtainPairSerializer):
    password = serializers.CharField(required=True)

    default_error_messages = {
        "inactive_account": _("User account is disabled."),
        "invalid_credentials": _("Unable to login with provided credentials."),
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(username=attrs.get("username"), password=attrs.get("password"))
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(
                    self.error_messages["inactive_account"]
                )
            return attrs
        else:
            raise serializers.ValidationError(
                self.error_messages["invalid_credentials"]
            )
        
    def to_representation(self, instance):
        refresh = RefreshToken.for_user(self.user)
        life_time = int(refresh.access_token.lifetime.total_seconds())
        response = {
                "username": self.user.username,
                "email": self.user.email,
                "token": {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                    "life_time": life_time
                },
        }
        return response

class UserRefreshTokenSerializer(TokenRefreshSerializer):

    def __init__(self, *args, **kwargs):
        super(UserRefreshTokenSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        data = super().validate(attrs)
        data['refresh'] = attrs.get("refresh")
        return data
    
    def get_new_token(self, validated_date):
        access_token = validated_date.get("access")
        refresh_token = validated_date.get("refresh")
        refresh = RefreshToken(refresh_token)
        life_time = int(refresh.access_token.lifetime.total_seconds())
        jwt_decode = jwt.decode(
                access_token,
                settings.SIMPLE_JWT["SIGNING_KEY"],
                algorithms=[settings.SIMPLE_JWT["ALGORITHM"]],
                )
        self.user = User.objects.get(id=jwt_decode['user_id'])
        response_formated = {
            "token": {
                "access": access_token,
                "life_time": life_time
            }
        }
        return response_formated

class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super(UserRegisterSerializer, self).__init__(*args, **kwargs)
        self.user = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password','password_confirm']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data.pop('password_confirm'):
            raise serializers.ValidationError("Password confirmation does not match")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user