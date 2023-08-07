from rest_framework import serializers
from .models import CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['profile_pic', 'email', 'password']

class UserNullSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = []

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'phone_no', 'sex']
    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        phone_no = attrs.get('phone_no', '')
        sex = attrs.get('sex', '')
        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255, min_length=3)
    username = serializers.CharField(max_length=64, read_only=True)
    password = serializers.CharField(max_length=68, min_length=6,write_only=True)
    
    tokens = serializers.SerializerMethodField()
    def get_tokens(self, obj):
        user = CustomUser.objects.get(email=obj['email'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'tokens']
    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')
        user = auth.authenticate(email=email,password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
