from django.db import models
from .auth_user import *
from .model_teacher import *

class Group(BaseModel):
    title=models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

class Student(BaseModel):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    group=models.ManyToManyField('Group', related_name="student")
    course=models.ManyToManyField(Course, related_name="student")
    is_line=models.BooleanField(default=False)
    descriptions=models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.phone_number

class Parents(BaseModel):
    student=models.OneToOneField(Student, on_delete=models.CASCADE)
    ful_name=models.CharField(max_length=500, blank=True, null=True)
    phone_number=models.CharField(max_length=500, blank=True, null=True)
    address=models.CharField(max_length=500, blank=True, null=True)
    descriptions=models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.ful_name
