"""
Commande pour insérer les compétences initiales en base.
Usage: python manage.py seed_competences
"""
from django.core.management.base import BaseCommand
from api.models import Competence


COMPETENCES_INITIALES = [
    # Design
    {"nom": "Adobe Photoshop", "niveau": "avance", "pourcentage": 90, "categorie": "Design",
     "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/photoshop/photoshop-plain.svg"},
    {"nom": "Adobe Illustrator", "niveau": "expert", "pourcentage": 95, "categorie": "Design",
     "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/illustrator/illustrator-plain.svg"},
    {"nom": "Adobe InDesign", "niveau": "avance", "pourcentage": 85, "categorie": "Design",
     "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/indesign/indesign-plain.svg"},
    {"nom": "Figma", "niveau": "expert", "pourcentage": 95, "categorie": "Design",
     "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg"},
    {"nom": "Sketch", "niveau": "avance", "pourcentage": 80, "categorie": "Design",
     "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sketch/sketch-original.svg"},
    # Développement
    {"nom": "HTML/CSS", "niveau": "expert", "pourcentage": 90, "categorie": "Développement",
     "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"},
    {"nom": "JavaScript", "niveau": "avance", "pourcentage": 85, "categorie": "Développement",
     "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"},
    {"nom": "React", "niveau": "avance", "pourcentage": 80, "categorie": "Développement",
     "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"},
    {"nom": "WordPress", "niveau": "avance", "pourcentage": 85, "categorie": "Développement",
     "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/wordpress/wordpress-plain.svg"},
    {"nom": "Git", "niveau": "intermediaire", "pourcentage": 75, "categorie": "Développement",
     "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"},
    # Motion & 3D
    {"nom": "Adobe After Effects", "niveau": "avance", "pourcentage": 85, "categorie": "Motion & 3D",
     "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/aftereffects/aftereffects-plain.svg"},
    {"nom": "Adobe Premiere Pro", "niveau": "avance", "pourcentage": 80, "categorie": "Motion & 3D",
     "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/premierepro/premierepro-plain.svg"},
    {"nom": "Cinema 4D", "niveau": "intermediaire", "pourcentage": 70, "categorie": "Motion & 3D",
     "icon": "https://www.svgrepo.com/show/373543/cinema-4d.svg"},
    {"nom": "Blender", "niveau": "intermediaire", "pourcentage": 65, "categorie": "Motion & 3D",
     "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/blender/blender-original.svg"},
    {"nom": "Lottie", "niveau": "avance", "pourcentage": 85, "categorie": "Motion & 3D",
     "icon": "https://framerusercontent.com/images/27k5A6CzdmGNNnh9WlkdtSdQfd8.svg"},
]


class Command(BaseCommand):
    help = "Insère les compétences initiales en base"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Remplacer toutes les compétences existantes par la liste initiale",
        )

    def handle(self, *args, **options):
        if Competence.objects.exists() and not options["force"]:
            self.stdout.write(
                self.style.WARNING("Des compétences existent déjà. Utilisez --force pour les remplacer.")
            )
            return

        if options["force"]:
            Competence.objects.all().delete()
            self.stdout.write("Anciennes compétences supprimées.")

        for c in COMPETENCES_INITIALES:
            Competence.objects.create(**c)

        self.stdout.write(
            self.style.SUCCESS(f"{len(COMPETENCES_INITIALES)} compétences créées.")
        )
