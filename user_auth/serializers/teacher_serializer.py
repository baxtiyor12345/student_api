from django.contrib.auth import authenticate
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import *
from .auth_serializer import *

#
# class TeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Teacher
#         fields=["id", "user", "departments", "course", "descriptions"]
#
# class TeacherUserSerializer(serializers.ModelSerializer):
#     is_active=serializers.BooleanField(read_only=True)
#     is_staff=serializers.BooleanField(read_only=False)
#     is_teacher=serializers.BooleanField(read_only=True)
#     is_admin=serializers.BooleanField(read_only=False)
#     is_student=serializers.BooleanField(read_only=False)
#
#     class Meta:
#         model=User
#         fields=("id","phone_number","password","is_active","is_teacher","is_staff","is_admin", "is_student")
#
# class TeacherPostSerializer(serializers.Serializer):
#     user=UserSerializer()
#     teacher=TeacherSerializer()

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    departments = serializers.PrimaryKeyRelatedField(queryset=Departments.objects.all(), many=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)

    class Meta:
        model = Teacher
        fields = ['user', 'departments', 'course', 'descriptions']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        departments_data = validated_data.pop('departments', [])
        course_data = validated_data.pop('course', [])

        user = User.objects.create_user(**user_data)
        teacher = Teacher.objects.create(user=user, **validated_data)

        teacher.departments.set(departments_data)
        teacher.course.set(course_data)

        return teacher


    # def validate(self, attrs):
    #     phone_number = attrs.get("phone_number")
    #     password = attrs.get("password")
    #
    #     try:
    #         user = User.objects.get(phone_number=phone_number)
    #     except User.DoesNotExist:
    #         raise serializers.ValidationError(
    #             {
    #                 "success":False,
    #                 "detail":"User does not exist"
    #             })
    #     auth_user=authenticate(phone_number=user.phone_number, password=password)
    #     if auth_user is None:
    #         raise serializers.ValidationError(
    #             {
    #                 "success":False,
    #                 "detail":"Phone_number or password is invalid"
    #             }
    #         )
    #     attrs["user"]=auth_user
    #     return attrs

