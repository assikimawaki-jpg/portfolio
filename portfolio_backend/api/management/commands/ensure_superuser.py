"""
Crée le superutilisateur s'il n'existe pas (pour déploiement Railway).
Lit les variables : DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD
"""
import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Crée le superutilisateur s'il n'existe pas"

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME", "Mawaki")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "Antoine@05#")

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS(f"Superutilisateur '{username}' existe déjà."))
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f"Superutilisateur '{username}' créé."))
