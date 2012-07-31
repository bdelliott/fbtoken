from django.conf import settings

def base_url(request):
    """Add the base absolute url of the webapp to the context."""
    return {"BASE_URL": settings.BASE_URL}

def fb_settings(request):
    """Add Facebook app settings to the context."""
    return {
        "FACEBOOK_APP_ID": settings.FACEBOOK_APP_ID,
        "FACEBOOK_APP_SECRET": settings.FACEBOOK_APP_SECRET,
        "FACEBOOK_STUB_API": settings.FACEBOOK_STUB_API,
    }

