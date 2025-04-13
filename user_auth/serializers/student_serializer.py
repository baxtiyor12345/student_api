from rest_framework import serializers
from ..models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .auth_serializer import *

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)


    class Meta:
        model = Student
        fields = ['user','group', 'is_line', 'course', 'descriptions']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        group_data = validated_data.pop('group', [])
        course_data = validated_data.pop('course', [])


        user = User.objects.create_user(**user_data)
        student = Student.objects.create(user=user, **validated_data)

        student.group.set(group_data)
        student.course.set(course_data)

        return student