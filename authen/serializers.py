from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    phone = serializers.IntegerField(required=True)
    address = serializers.CharField(max_length=100, required=False)
    city = serializers.CharField(max_length=30, required=False)
    state = serializers.CharField(max_length=30, required=False)
    country = serializers.CharField(max_length=50, required=False)
    pin_code = serializers.IntegerField(required=True)

    class Meta:
         model = User
         fields = ['first_name', 'last_name', 'email', 'password', 'phone', 'address', 'city', 'state', 'country', 'pin_code']


    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email is already in use'})
        return super().validate(attrs)
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model=User
        fields = ['email', 'password']