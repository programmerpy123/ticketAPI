from rest_framework import serializers
from django.contrib.auth.models import User

def email_validate(value):
    pass

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True,write_only=True)
  #field level
    def validate_username(self, value):
        if value == 'amirreza':
            raise serializers.ValidationError('این کاربر اجازه دسترسی ندارد')

        return value
#object level
    def validate(self, data):
        if data['password']!= data['confirm_password']:
            raise serializers.ValidationError('مقدار پسورد ها هم خوانی ندارد')
        return data


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'comfirm_password')

    def create(self, validated_data):
        del validated_data['comfirm_password']
        return User.objects.create_user(**validated_data)

    comfirm_password = serializers.CharField()
    def validate_username(self, value):
            if value == 'amirrezam':
                raise serializers.ValidationError('این کاربر اجازه دسترسی ندارد')

            return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


