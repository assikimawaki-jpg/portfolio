from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from .models import Profil, Competence, Projet, Parcours, MessageContact
from .serializers import (
    ProfilSerializer,
    CompetenceSerializer,
    ProjetSerializer,
    ParcoursSerializer,
    MessageContactSerializer,
)
from .permissions import IsAdminOrReadOnly


class ProfilViewSet(viewsets.ModelViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAdminOrReadOnly]


class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    permission_classes = [IsAdminOrReadOnly]


class ParcoursViewSet(viewsets.ModelViewSet):
    queryset = Parcours.objects.all()
    serializer_class = ParcoursSerializer
    permission_classes = [IsAdminOrReadOnly]


class MessageContactViewSet(viewsets.ModelViewSet):
    queryset = MessageContact.objects.all()
    serializer_class = MessageContactSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAdminUser()]

    def perform_create(self, serializer):
        serializer.save(lu=False)

    @action(detail=True, methods=["post"], permission_classes=[IsAdminUser])
    def reply(self, request, pk=None):
        message = self.get_object()
        subject = request.data.get("subject", "").strip()
        body = request.data.get("body", "").strip()

        if not subject or not body:
            return Response(
                {"detail": "Sujet et message requis."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=getattr(
                    settings, "DEFAULT_FROM_EMAIL", settings.EMAIL_HOST_USER
                ),
                to=[message.email],
            )
            email.send(fail_silently=False)
            message.lu = True
            message.save(update_fields=["lu"])
            return Response({"detail": "Réponse envoyée."}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response(
                {"detail": f"Échec d'envoi: {exc}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
