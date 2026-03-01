"""Middleware pour exempt CSRF sur l'API REST (JWT)."""


class DisableCSRFForAPI:
    """Exempt /api/ du contrôle CSRF pour les requêtes cross-origin (SPA)."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/api/"):
            setattr(request, "_dont_enforce_csrf_checks", True)
        return self.get_response(request)
