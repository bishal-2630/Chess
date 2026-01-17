"""
Django views for Chess Game API
"""
from django.http import HttpResponse

def health_check(request):
    """Health check endpoint for Railway"""
    return HttpResponse("Chess Game API is running! ✅", content_type='text/plain')
