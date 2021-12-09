from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from . import models
import random


class WordSerializator(serializers.ModelSerializer):
    class Meta:
        model = models.Words
        fields = ['pk', 'gender', 'words']


class RandomWord(APIView):
    def get(self, *args, **kwargs):
        all_words = models.Words.objects.all()
        random_word = random.choice(all_words)
        serial_word = WordSerializator(random_word, many=False)
        return Response(serial_word.data)


class NextWord(APIView):
    def get(self, request, pk, format=None):
        word = models.Words.objects.filter(pk__gt=pk).first()
        if not word:
            return Response({'no': 'no'})
        serial_word = WordSerializator(word, many=False)
        return Response(serial_word.data)
