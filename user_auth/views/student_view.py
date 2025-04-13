from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import *
from user_auth.models import Student
from user_auth.serializers import StudentSerializer


class UserStudentCreateApi(APIView):
    @swagger_auto_schema(request_body=StudentSerializer)
    def post(self,request):
        data={"success":True}
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # password=serializer.validated_data.get("password")
            # serializer.validated_data["password"]=make_password(password)
            serializer.save()
            data["data"] = serializer.data
            return Response(data=data)
        return Response(serializer.errors)

    def get(self, request):
        student=Student.objects.all().order_by('-id')
        serializer=TeacherSerializer(student, many=True)
        return Response(data=serializer.data)

    def get(self, request, pk):
        response = {"success": True}

        try:
            student = Teacher.objects.get(pk=pk)
            serializer = TeacherSerializer(student)
            response["data"] = serializer.data
            return Response(data=response)
        except Teacher.DoesNotExist:
            response["success"] = False
            return Response(data=response)

    def put(self, request, pk):
        response = {"success": True}

        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                response["data"] = serializer.data
                return Response(data=response)
            return Response(data=serializer.data)
        except Student.DoesNotExist:
            response["success"] = False
            return Response(data=response)

    def patch(self, request, pk):
        response = {"success": True}

        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                response["data"] = serializer.data
                return Response(data=response)
            return Response(data=serializer.data)
        except Student.DoesNotExist:
            response["success"] = False
            return Response(data=response)

    def delete(self, request, pk):
        response = {"success": True}

        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            response["error"] = "bunday malumot yuq"
            return Response(data=response, status=status.HTTP_417_EXPECTATION_FAILED)
        id = student.pk
        student.delete()
        return Response(data={"id": f"{id} o`chirildi"})