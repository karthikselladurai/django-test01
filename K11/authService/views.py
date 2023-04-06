from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .UserSerializer import UsersSerializer
from .encryption import SHA256PasswordHasher
from .models import UserModel


@api_view(['POST'])
def signup(request):
    user_data = JSONParser().parse(request)
    if user_data['email']:
        email = user_data['email']
        print("1")
        try:
            user = UserModel.objects.get(email=email)
            resp = {'status': 'Unsuccess', 'data': [], 'message': 'Email Already Exits'}
            return JsonResponse(resp, status=400)

        except UserModel.DoesNotExist:
            print('2')
            # resp = {'status': 'Unsuccess', 'data': [], 'message': 'User not found'}
            # return JsonResponse(resp, status=400)
            hasher = SHA256PasswordHasher()
            password = user_data['password']
            # salt = user_data['email']
            # print(hasher.encode(password).decode('latin1'))
            user_data['password'] = hasher.encode(password)
            item = UsersSerializer(data=user_data)
            print(3)
            if item.is_valid():
                # item.save()
                return Response(status=status.HTTP_200_OK,
                                data={"status": "Success", "data": item.data, "message": 'Signup Successfully'})
            print(item.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={"status": "Unsuccess", "data": [], "message": 'Invalid Details'})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={"status": "Unsuccess", "data": [], "message": ' Invalid Email'})

@api_view(['POST'])
def signin(request):
    user_data = JSONParser().parse(request)
    email = user_data['email']
    password = user_data['password']
    hasher = SHA256PasswordHasher()
    try:
        user = UserModel.objects.get(email=email)
        print(password, user.password,user.name,'>>>>>>>>>>>> hasher.verify(password, user.password)', hasher.verify(password, user.password))
        if hasher.verify(password, user.email):
            user_data = {
                'id': user.userId,
                'username': user.name,
                'email': user.email,
            }
            resp = {'status': 'Success', 'data': user_data, 'message': 'SignIn Successfully'}
            return JsonResponse(resp, status=200)
        else:
            resp = {'status': 'Unsuccess', 'data': [], 'message': 'Incorrect Email Or Password'}
            return JsonResponse(resp, status=200)

    except UserModel.DoesNotExist:
        resp = {'status': 'Unsuccess', 'data': [], 'message': 'User not found'}
        return JsonResponse(resp, status=400)
