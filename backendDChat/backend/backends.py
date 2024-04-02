# import json
# import pdb
# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from rest_framework.decorators import api_view
# from .models import Employee,User
# from .serializer import EmployeeSerializers,UserSerializers
# from rest_framework.response import Response
# from datetime import datetime
from django.contrib.auth.hashers import make_password,check_password

# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth import authenticate

# class CustomAuthBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None):
#         try:
#             user = User.objects.get(username=username)
#             if user.check_password(password):
#                 return user
#         except User.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
from .models import User

class CustomAuthBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                print('asdasdasd')
                return user
        except User.DoesNotExist:
            return None
