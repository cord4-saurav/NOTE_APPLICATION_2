from django.shortcuts import render
from .models import NoteAPI
from .serializers import Note_APISerializer
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.
class Note_APIViewSet(viewsets.ModelViewSet):
    queryset = NoteAPI.objects.all()
    serializer_class = Note_APISerializer

