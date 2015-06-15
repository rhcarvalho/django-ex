from django.http import HttpResponse
from django.db import connection


def live(request):
    """View to check server liveness"""
    return HttpResponse()

def ready(request):
    """View to check server readiness"""
    connection.ensure_connection()
    if connection.is_usable():
        return HttpResponse()
    return HttpResponse(status=503)
