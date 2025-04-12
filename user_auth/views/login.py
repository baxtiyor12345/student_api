import random
from random import randint
from ..make_tokens import *
from django.contrib.auth.hashers import make_password
from django.core.cache import cache
from django.core.serializers import serialize
from django.template.context_processors import request
from django.utils.autoreload import raise_last_exception
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import *
from ..models import *


class PhoneSendOtp(APIView):
    @swagger_auto_schema(request_body=SMSSerializer)
    def post(self, request, *args, **kwargs):
        phone_number=request.data.get("phone_number")
        if phone_number:
            phone=str(phone_number)
            user=User.objects.filter(phone_number=phone)
            if user.exists():
                return Response(
                    {
                        "status":False,
                        "detail":"Phone_number alredy exists"
                    }
                )
            else:
                key=send_otp()
                print("====================",key)
                if key:
                    cache.set(phone_number,key)

                    return Response({"message":"Sms send successfully"}, status=status.HTTP_200_OK)
                return Response({"message":"Failed to send SMS"}, status=status.HTTP_400_BAD_REQUEST)



def send_otp():
    otp=str(random.randint(1001,9999))
    return otp

class VerifySms(APIView):
    @swagger_auto_schema(request_body=VerifySMSSerializer)
    def post(self, request):
        serializer=VerifySMSSerializer(data=request.data)
        if serializer.is_valid():
            phone_number=serializer.validated_data["phone_number"]
            verification_code=serializer.validated_data["verification_code"]
            cached_code=str(cache.get(phone_number))
            if verification_code==str(cached_code):
                return Response(
                    {
                        "status":True,
                        "detail":"OTP matched please proceed for registration"
                    }
                )
            else:
                return Response(
                    {
                        "status":False,
                        "detail":"OTP incorrect"
                    }
                )



class RegisterUserApi(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            password=serializer.validated_data.get("password")
            serializer.validated_data["password"]=make_password(password)
            serializer.save()
            return Response({
                "status":True,
                "detail":"Account create"
            })

    def get(self, request):
        users=User.objects.all().order_by('-id')
        serializer=UserSerializer(users, many=True)
        return Response(data=serializer.data)

class ChangePasswordView(APIView):
    permission_classes = (permissions.IsAuthenticated)

    def patch(self, request, *args, **kwargs):
        serializer=ChangePasswordSerializer(instance=self.request.user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginApi(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer=LoginSerializer(data=request)
        serializer.is_valid(raise_exception=True)

        user=serializer.validated_data.get("user")
        token=get_tokens_for_user(user)
        token["salom"]="hi"
        token["is_admin"]=user.is_superuser

        return Response(dat=token, status=status.HTTP_200_OK)

