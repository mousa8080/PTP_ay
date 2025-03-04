from .models import DriverInfo
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'full_name',
            'phone',
            'national_id',
            'password',
            'password2',
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("كلمتا المرور غير متطابقتين.")
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



class RegisterDriverSerializer(RegisterUserSerializer):
    driver_photo = serializers.ImageField(required=True)
    license_photo = serializers.ImageField(required=True)
    license_number = serializers.CharField(required=True)


    class Meta(RegisterUserSerializer.Meta):
        fields = RegisterUserSerializer.Meta.fields + [
            'driver_photo',
            'license_photo',
            'license_number',
        ]

    def create(self, validated_data):
        driver_photo = validated_data.pop('driver_photo', None)
        license_photo = validated_data.pop('license_photo', None)
        license_number = validated_data.pop('license_number', None)

        validated_data['is_driver'] = True

        user = super().create(validated_data)

        DriverInfo.objects.create(
            user=user,
            driver_photo=driver_photo,
            license_photo=license_photo,
            license_number=license_number
        )

        return user