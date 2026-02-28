from rest_framework import serializers
from .models import Profil, Competence, Projet, Parcours, MessageContact


class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = "__all__"


class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = "__all__"


class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = "__all__"


class ParcoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcours
        fields = "__all__"


class MessageContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageContact
        fields = "__all__"
        read_only_fields = ["date_envoi"]
