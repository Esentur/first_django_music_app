from dataclasses import field
from rest_framework import serializers
from music_app.models import Music

class MusicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Music
        fields = '__all__'
        # fields = ['title']