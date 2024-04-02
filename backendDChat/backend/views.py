import json
import pdb
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Employee,User
from .serializer import EmployeeSerializers,UserSerializers
from rest_framework.response import Response
from datetime import datetime
from django.contrib.auth.hashers import make_password,check_password

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# @api_view(['GET','POST','PUT','DELETE'])
@api_view(['GET','POST','PUT','DELETE'])
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_data = data['data']
        username = user_data['username']
        password = user_data['password']

        user = authenticate(username=username, password=password)
        # pdb.set_trace()
        if user is not None:
            refresh = RefreshToken.for_user(user)
            userData ={
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'UserID' : user.id,
                'UserFullname':user.firstname + ' ' + user.middlename + '. ' + user.lastname

            }
            return JsonResponse({'data': userData}, status=200)
        else:
            # Authentication failed
            return JsonResponse({'error': 'Invalid username or password'}, status=401)

    return JsonResponse({'error': 'Method not allowed'}, status=405)



# def login(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         user_data = data['data']
#         username = user_data['username']
#         password = user_data['password']

#         # Query the database for the user
#         # try:
#         pdb.set_trace()
#         user = authenticate(username=username, password=password)
#         userData ={
#                 'UserID' : user.id,
#                 'UserFullname':user.firstname + ' ' + user.middlename + '. ' + user.lastname

#             }
#             # Passwords match, login successful
#             # Perform login logic here (e.g., set session variables)
#         return JsonResponse({'data':userData}, status=200)
#             # user = User.objects.get(username=username)
#     #     except User.DoesNotExist:
#     #         # User not found, handle accordingly (e.g., display error message)
#     #         return HttpResponse('Invalid username or password', status=401)

#     #     # Compare the provided password with the hashed password stored in the database
#     #     if check_password(password, user.password):
#     #         userData ={
#     #             'UserID' : user.id,
#     #             'UserFullname':user.firstname + ' ' + user.middlename + '. ' + user.lastname

#     #         }
#     #         # Passwords match, login successful
#     #         # Perform login logic here (e.g., set session variables)
#     #         return JsonResponse({'data':userData}, status=200)
#     #     else:
#     #         # Passwords don't match, login failed
#     #         # Handle accordingly (e.g., display error message)
#     #         return HttpResponse('Invalid username or password', status=401)
#     # else:
#     #     # Handle GET request (e.g., display login form)
#     #     pass
#     # # Create your views here.


@api_view(['GET','POST','PUT','DELETE'])
def employee(request):
    if request.method =='GET':
        data = Employee.objects.all()
        serializeData = EmployeeSerializers(data,many=True)
        print(serializeData.data)
        # return Response(serializeData.data)
        return JsonResponse({'data':serializeData.data})
    elif request.method =='POST':
        data = json.loads(request.body)
        print(data)

        return JsonResponse({'EMPLOYEE':'Success'})
    elif request.method =='DELETE':
        return JsonResponse({'EMPLOYEE':'Success'})

@api_view(['GET','POST','PUT','DELETE'])
def signup(request):
    if request.method =='GET':
        data = User.objects.all()
        serializeData = UserSerializers(data,many=True)
        print(serializeData.data)
        # return Response(serializeData.data)
        return JsonResponse({'data':serializeData.data})
    elif request.method =='POST':
        data = json.loads(request.body)
        user_data = data['data']
        timestamp_str = user_data.get('bdate')
        timestamp_dt = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        local_timestamp_dt = timestamp_dt.astimezone()
        hashed_password = make_password(user_data['password'])
        # Format the datetime object as a string in a specific format
        formatted_timestamp = local_timestamp_dt.strftime('%Y-%m-%d')

        findUser = User.objects.filter(username=user_data['username']).first()
        findEmail = User.objects.filter(email=user_data['email']).first()
        if findUser:
            print('User')
            return JsonResponse({'message':'User Already Exist..'},status=400)
        
        elif findEmail:
            print('Email')
            return JsonResponse({'message':'Email Already Registered..'},status=400)
        else:
            saveUser = User(
                firstname=user_data['firstname'],
                middlename=user_data.get('middlename'),  # Use get() to handle optional fields
                lastname=user_data['lastname'],
                bdate=formatted_timestamp,  # Use get() to handle optional fields
                email=user_data['email'],
                username=user_data['username'],
                password=hashed_password
            )

            saveUser.save()
            return JsonResponse({'message':'User Successfully Added'},status=200)
    elif request.method =='DELETE':
        return JsonResponse({'EMPLOYEE':'Success'})