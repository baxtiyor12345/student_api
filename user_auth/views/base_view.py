# from django.contrib.auth.hashers import make_password
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from ..serializers import *
# from user_auth.models import Teacher
# from user_auth.serializers import TeacherSerializer
#
# class BaseCreateApi(APIView):
#     @swagger_auto_schema(request_body=BaseSerializer)
#     def post(self,request):
#         request={"success":True}
#         serializer=BaseSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             # password=serializer.validated_data.get("password")
#             # serializer.validated_data["password"]=make_password(password)
#             serializer.save()
#             request["data"] = serializer.data
#             return Response(data=request)
#         return Response(serializer.data)