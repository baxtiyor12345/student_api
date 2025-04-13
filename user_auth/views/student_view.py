from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
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
        teacher=Teacher.objects.all().order_by('-id')
        serializer=TeacherSerializer(teacher, many=True)
        return Response(data=serializer.data)