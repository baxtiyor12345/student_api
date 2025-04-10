from django.contrib.auth import authenticate
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import *


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=["user"]

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        password = attrs.get("password")

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "success":False,
                    "detail":"User does not exist"
                })
        auth_user=authenticate(phone_number=user.phone_number, password=password)
        if auth_user is None:
            raise serializers.ValidationError(
                {
                    "success":False,
                    "detail":"Phone_number or password is invalid"
                }
            )
        attrs["user"]=auth_user
        return attrs

