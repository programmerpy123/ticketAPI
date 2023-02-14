from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import View
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Person, Question, Answer
from .serializers import PersonSerializer, QuestionSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework import status
from permissions import IsOwnerOrReadonly

@api_view(['GET','POST','PUT'])
@permission_classes([IsAdminUser])
def home(request):
     persons = Person.objects.all()
     ser_data = PersonSerializer(instance=persons, many = True)
     return Response(data=ser_data.data)

# @api_view(['GET','POST','DELETE','PUT','OPTIONS','HEAD'])


class QuestionListView(APIView):
     permission_classes=[IsAuthenticated]

     def get(self, request):
          questions = Question.objects.all()
          ser_data = QuestionSerializer(instance=questions, many=True).data
          return Response(ser_data)


class QuestionCreateView(APIView):
     """
     create new question
     """
     serializer_class = QuestionSerializer
     def post(self, request):
          ser_data = QuestionSerializer(data=request.data)
          # print(ser_data)

          if ser_data.is_valid():

               ser_data.save()
               print(ser_data.data)
               return Response(data=ser_data.data, status=status.HTTP_200_OK)
          return Response(data=ser_data.errors,status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
     permission_classes = [IsOwnerOrReadonly]
     def put(self, request, pk):
          question = Question.objects.get(pk=pk)
          self.check_object_permissions(request, question)
          ser_data = QuestionSerializer(instance=question, data=request.data, partial=True)
          if ser_data.is_valid():
               ser_data.save()
               return Response(data=ser_data.data, status=status.HTTP_200_OK)
          return Response(data=ser_data.errors,status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
     permission_classes = [IsAuthenticated]
     def delete(self,request, pk):
         try :
           question = Question.objects.get(id=pk)
           question.delete()
           return Response({'message': 'successfully deleted resource'})

         except ObjectDoesNotExist :
              return Response({'message': 'out of range'})



