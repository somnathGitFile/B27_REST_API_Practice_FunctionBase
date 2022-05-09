from functools import partial
from django.shortcuts import render
from .models import Book
from rest_framework.views import APIView
from book.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class BookDetails(APIView):
    def get(self, request):
            bok= Book.objects.all()
            serializer = BookSerializer(bok, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data, many= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)
    
class BookInfo(APIView):
    def get(self, request, id):
        try:
            bok = Book.objects.get(id=id)
        except Book.DoesNotExist:
            msg = {'msg':'Record Does not Found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(bok, data=request.data)

    def put(self, request, id):
        try:
            bok = Book.objects.get(id=id)
        except Book.DoesNotExist:
            msg = {'msg':'Record Does not Found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(bok, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            bok = Book.objects.get(id=id)
        except Book.DoesNotExist:
            msg = {'msg':'Record Does not Found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        bok.delete()
        msg = {'msg':'Record delete Successfully!!!!'}
        return Response(msg,status=status.HTTP_204_NO_CONTENT)






