from django.contrib import admin
from .models import Profil, Competence, Projet, MessageContact


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ("nom", "titre_professionnel", "email", "telephone")
    search_fields = ("nom", "titre_professionnel", "email")


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ("nom", "categorie", "niveau", "pourcentage")
    list_filter = ("categorie", "niveau")
    search_fields = ("nom", "categorie")
    ordering = ("-pourcentage", "nom")


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ("titre", "date_creation", "lien_demo", "lien_github")
    list_filter = ("date_creation",)
    search_fields = ("titre", "description")
    ordering = ("-date_creation",)


@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ("nom", "email", "sujet", "date_envoi", "lu")
    list_filter = ("lu", "date_envoi")
    search_fields = ("nom", "email", "sujet", "message")
    ordering = ("-date_envoi",)
    actions = ["marquer_comme_lu"]

    def marquer_comme_lu(self, request, queryset):
        queryset.update(lu=True)

    marquer_comme_lu.short_description = "Marquer les messages sélectionnés comme lus"
