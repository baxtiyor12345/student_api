from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import *
from user_auth.models import Teacher
from user_auth.serializers import TeacherSerializer


# class TeacherCreateApi(APIView):
#     @swagger_auto_schema(request_body=TeacherPostSerializer)
#     def post(self,request):
#         data={"success":True}
#         user=request.data["user"]
#         phone_number=request.data["phone_number"]
#         teacher=request.data["teacher"]
#         user_serializer=UserSerializer(data=user)
#         if user_serializer.is_valid(raise_exception=True):
#             user_serializer.is_teacher=True
#             user_serializer.is_active=True
#             user_serializer.password=(make_password(user_serializer.validated_data.get("password")))
#             user=user_serializer.save()
#
#             user_id=User.objects.filter(phone_number=phone_number).is_valid("id")[0]["id"]
#             teacher["user"]=user_id
#             teacher_serializer = TeacherSerializer(data=teacher)
#
#             if teacher_serializer.is_valid(raise_exception=True):
#                 teacher_serializer.save()
#                 data["user"]=user_serializer.data
#                 data["teacher"]=teacher_serializer.data
#                 return Response(data=data)
#             return Response(data=teacher_serializer.errors)
#         return Response(data=user_serializer.errors)
#             # return Response({
#             #     "status":True,
            #     "detail":"Account create"
            # })

    # def get(self, request):
    #     users=Teacher.objects.all().order_by('-id')
    #     serializer=UserSerializer(users, many=True)
    #     return Response(data=serializer.data)
#
# class TeacherCreateApiView(ListCreateAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer

class UserTeacherCreateApi(APIView):
    @swagger_auto_schema(request_body=TeacherSerializer)
    def post(self,request):
        data={"success":True}
        serializer=TeacherSerializer(data=request.data)
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