"""
Commande pour insérer les étapes initiales du parcours.
Usage: python manage.py seed_parcours
"""
from django.core.management.base import BaseCommand
from api.models import Parcours


PARCOURS_INITIAL = [
    {"date": "2022 - Présent", "titre": "Directeur Créatif", "lieu": "Studio Design", "localisation": "Lomé, Togo", "description": "Direction des projets créatifs, gestion des équipes de design et développement de la stratégie visuelle pour les clients majeurs.", "ordre": 0},
    {"date": "2021", "titre": "Formation UX/UI Avancée", "lieu": "École du Design", "localisation": "En ligne", "description": "Formation spécialisée en conception d'expérience utilisateur et interfaces innovantes.", "ordre": 1},
    {"date": "2019 - 2022", "titre": "Designer Senior", "lieu": "Agence Digitale Creative", "localisation": "Lomé, Togo", "description": "Conception et réalisation de projets web et mobiles pour des clients internationaux. Responsable de l'identité visuelle et de l'expérience utilisateur.", "ordre": 2},
    {"date": "2018", "titre": "Master en Design Graphique", "lieu": "Université des Arts", "localisation": "Lomé, Togo", "description": "Spécialisation en design d'interface et communication visuelle. Projet de fin d'études sur l'accessibilité dans le design web.", "ordre": 3},
    {"date": "2016 - 2019", "titre": "Designer Web", "lieu": "StartUp Innovante", "localisation": "Lomé, Togo", "description": "Création de sites web, applications et supports marketing pour une startup en pleine croissance.", "ordre": 4},
]


class Command(BaseCommand):
    help = "Insère les étapes initiales du parcours"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Remplacer toutes les étapes existantes",
        )

    def handle(self, *args, **options):
        if Parcours.objects.exists() and not options["force"]:
            self.stdout.write(
                self.style.WARNING("Des étapes existent déjà. Utilisez --force pour les remplacer.")
            )
            return

        if options["force"]:
            Parcours.objects.all().delete()
            self.stdout.write("Anciennes étapes supprimées.")

        for p in PARCOURS_INITIAL:
            Parcours.objects.create(**p)

        self.stdout.write(
            self.style.SUCCESS(f"{len(PARCOURS_INITIAL)} étapes créées.")
        )
