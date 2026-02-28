from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profil",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nom", models.CharField(max_length=120)),
                ("titre_professionnel", models.CharField(max_length=160)),
                ("photo", models.ImageField(blank=True, null=True, upload_to="profil/photos/")),
                ("bio", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("telephone", models.CharField(blank=True, max_length=30)),
                ("linkedin", models.URLField(blank=True)),
                ("github", models.URLField(blank=True)),
                ("cv", models.FileField(blank=True, null=True, upload_to="profil/cv/")),
            ],
            options={
                "verbose_name": "Profil",
                "verbose_name_plural": "Profil",
            },
        ),
        migrations.CreateModel(
            name="Competence",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nom", models.CharField(max_length=120)),
                (
                    "niveau",
                    models.CharField(
                        choices=[
                            ("debutant", "Débutant"),
                            ("intermediaire", "Intermédiaire"),
                            ("avance", "Avancé"),
                            ("expert", "Expert"),
                        ],
                        max_length=20,
                    ),
                ),
                ("pourcentage", models.PositiveIntegerField()),
                ("categorie", models.CharField(max_length=80)),
            ],
            options={
                "verbose_name": "Compétence",
                "verbose_name_plural": "Compétences",
                "ordering": ["-pourcentage", "nom"],
            },
        ),
        migrations.CreateModel(
            name="Projet",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titre", models.CharField(max_length=160)),
                ("description", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="projets/images/")),
                ("lien_demo", models.URLField(blank=True)),
                ("lien_github", models.URLField(blank=True)),
                ("date_creation", models.DateField()),
            ],
            options={
                "verbose_name": "Projet",
                "verbose_name_plural": "Projets",
                "ordering": ["-date_creation"],
            },
        ),
        migrations.CreateModel(
            name="MessageContact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nom", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("sujet", models.CharField(max_length=200)),
                ("message", models.TextField()),
                ("date_envoi", models.DateTimeField(auto_now_add=True)),
                ("lu", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Message",
                "verbose_name_plural": "Messages",
                "ordering": ["-date_envoi"],
            },
        ),
    ]
