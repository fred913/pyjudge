from flask import Response


def generate_403(text: str | None = None):
    return Response(text or "Forbidden", status=403)


def generate_404(text: str | None = None):
    return Response(text or "Not found", status=404)
