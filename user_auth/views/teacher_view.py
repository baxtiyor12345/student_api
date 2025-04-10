from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import *
from user_auth.models import Teacher
from user_auth.serializers import TeacherSerializer


class TeacherUserApi(APIView):
    @swagger_auto_schema(request_body=TeacherSerializer)
    def post(self,request):
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            password=serializer.validated_data.get("password")
            serializer.validated_data["password"]=make_password(password)
            serializer.save()
            return Response({
                "status":True,
                "detail":"Account create"
            })

    def get(self, request):
        users=Teacher.objects.all().order_by('-id')
        serializer=UserSerializer(users, many=True)
        return Response(data=serializer.data)