from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    path("post_phone_send_otp/", PhoneSendOtp.as_view()),
    path("post_phone_v_otp/", VerifySms.as_view()),
    path("register/", RegisterUserApi.as_view()),
    path("teacher/", UserTeacherCreateApi.as_view()),
    path("student/", UserStudentCreateApi.as_view()),
    # path("teacher/", TeacherCreateApiView.as_view()),
    # path("ass/", BaseSerializer.as_view())
]
