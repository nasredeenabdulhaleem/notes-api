from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Note


# class UserSerializer(serializers.ModelSerializer):
#     class META:
#         model = User
#         fields = ["username", "email", "password"]


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "note"]
