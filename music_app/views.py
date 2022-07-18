from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from music_app.models import Music
from music_app.serializers import MusicSerializer

# Create your views here.

@api_view(['GET'])
def hello_world(request):
    return Response('Hello world')

@api_view(['GET'])
def get_music(request):
    musics = Music.objects.all()
    # print('*******************')
    # print(request)
    # print(dir(request))
    # print('*******************')
    #print(musics)
    serializer=MusicSerializer(musics,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_detail(request,id):
    try:    
        music= Music.objects.get(id=id)
    except Music.DoesNotExist:
       
        return Response('Нет такой музыки')
    serializer = MusicSerializer(music, many=False)
    return Response(serializer.data)

@api_view(['PATCH'])
def music_patch(request,id):
    try:    
        music= Music.objects.get(id=id)
    except Music.DoesNotExist:
        return Response('Нет такой музыки')
    serializer = MusicSerializer(music, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def music_create(request):
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def music_delete(request,id):
    try:    
        music= Music.objects.get(id=id)
    except Music.DoesNotExist:
        return Response('Нет такой музыки')
    music.delete()
    return Response('Successfully deleted')

