from django.db import models


class Profil(models.Model):
    nom = models.CharField(max_length=120)
    titre_professionnel = models.CharField(max_length=160)
    photo = models.ImageField(upload_to="profil/photos/", blank=True, null=True)
    bio = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=30, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    cv = models.FileField(upload_to="profil/cv/", blank=True, null=True)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"

    def __str__(self):
        return self.nom


class Competence(models.Model):
    NIVEAU_CHOICES = [
        ("debutant", "Débutant"),
        ("intermediaire", "Intermédiaire"),
        ("avance", "Avancé"),
        ("expert", "Expert"),
    ]

    nom = models.CharField(max_length=120)
    niveau = models.CharField(max_length=20, choices=NIVEAU_CHOICES)
    pourcentage = models.PositiveIntegerField()
    categorie = models.CharField(max_length=80)
    icon = models.URLField(max_length=500, blank=True)

    class Meta:
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"
        ordering = ["-pourcentage", "nom"]

    def __str__(self):
        return f"{self.nom} ({self.niveau})"


class Projet(models.Model):
    titre = models.CharField(max_length=160)
    description = models.TextField()
    image = models.ImageField(upload_to="projets/images/", blank=True, null=True)
    lien_demo = models.URLField(blank=True)
    lien_github = models.URLField(blank=True)
    date_creation = models.DateField()

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ["-date_creation"]

    def __str__(self):
        return self.titre


class Parcours(models.Model):
    """Étape du parcours professionnel ou académique."""

    date = models.CharField(max_length=80)  # ex: "2022 - Présent", "2019 - 2022"
    titre = models.CharField(max_length=160)  # ex: "Directeur Créatif"
    lieu = models.CharField(max_length=160)  # ex: "Studio Design"
    localisation = models.CharField(max_length=120)  # ex: "Lomé, Togo"
    description = models.TextField()
    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Parcours"
        verbose_name_plural = "Parcours"
        ordering = ["ordre", "-id"]

    def __str__(self):
        return f"{self.titre} @ {self.lieu}"


class MessageContact(models.Model):
    nom = models.CharField(max_length=120)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["-date_envoi"]

    def __str__(self):
        return f"{self.nom} - {self.sujet}"
