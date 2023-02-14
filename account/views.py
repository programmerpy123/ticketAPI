from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, UserSignUpSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class Register(APIView):

    def post(self, request):
        ser_data = UserSignUpSerializer(data = request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    users = User.objects.all()
    def list(self, request):
        srz_data = UserSerializer(instance=self.users, many=True)
        return Response(srz_data.data)


    def create(self, request):
        pass

    def retrieve(self, requset, pk=None):
        users = self.users.get(pk=pk)
        srz_data = UserSerializer(instance=users)
        return Response(srz_data.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def  destroy(self, request, pk=None):
        user = self.users.get(pk=pk)
        user.is_active = True
        user.save()
        return Response({'message': 'successfully deactivated'})
