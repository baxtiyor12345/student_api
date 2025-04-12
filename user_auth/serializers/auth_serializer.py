from rest_framework import serializers
from ..models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id","phone_number","password","is_active","is_teacher","is_staff","is_admin", "is_student")

class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password=serializers.CharField(required=True, write_only=True)
    new_password=serializers.CharField(required=True, write_only=True)
    re_new_password=serializers.CharField(required=True, write_only=True)

    def update(self, instance, validated_data):

        instance.password=validated_data.get("password", instance.password)

        if not validated_data["new_password"]:
            raise serializers.ValidationError({"new_password":"not found"})

        if not validated_data["old_password"]:
            raise serializers.ValidationError({"old_password":"not found"})

        if not instance.check_password(validated_data["old_password"]):
            raise serializers.ValidationError({"old_password":"wrong password"})

        if not validated_data["new_password"] != validated_data["re_new_password"]:
            raise serializers.ValidationError({"passwords":"passwords do not match"})

        if not validated_data["new_password"] == validated_data["re_new_password"] and instance.check_password(validated_data["old_password"]):
            instance.set_password(validated_data["new_password"])
            instance.save()
            return instance
    class Meta:
        model=User
        fields=["old_password", "new_password", "re_new_password"]

class SMSSerializer(serializers.Serializer):
    phone_number=serializers.CharField()


class VerifySMSSerializer(serializers.Serializer):
    phone_number=serializers.CharField()
    verification_code=serializers.CharField()
