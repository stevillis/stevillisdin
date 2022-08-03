"""
App views.
"""

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def index(request: WSGIRequest) -> HttpResponse:
    """
    Homepage.
    """
    context = {

    }

    return render(
        request=request,
        template_name='index.html',
        context=context
    )
