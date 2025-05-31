from django.conf import settings
from .models import SiteSettings
from django.utils import timezone

def social_media_links(request):
    return{
        'facebook' : getattr(settings, 'FACEBOOK_URL', '#'),
        'twitter': getattr(settings, 'TWITTER_URL', '#'),
        'linkedin': getattr(settings, 'LINKEDIN_URL', '#'),
        'instagram': getattr(settings, 'INSTAGRAM_URL', '#'),
        'youtube': getattr(settings, 'YOUTUBE_URL', '#'),
        'google_plus': getattr(settings, 'GOOGLE_PLUS_URL', '#'),
    }


def social_links(request):
    return {
        "SOCIAL_LINKS": [
            {"name": "Facebook", "url": "#", "icon": "fab fa-facebook-f", "color": "#39569E", "followers": "12,346 Fans"},
            {"name": "Twitter", "url": "#", "icon": "fab fa-twitter", "color": "#52AAF4", "followers": "12,345 Followers"},
            {"name": "LinkedIn", "url": "#", "icon": "fab fa-linkedin-in", "color": "#0185AE", "followers": "12,345 Connects"},
            {"name": "Instagram", "url": "#", "icon": "fab fa-instagram", "color": "#C8359D", "followers": "12,345 Followers"},
            {"name": "YouTube", "url": "#", "icon": "fab fa-youtube", "color": "#DC472E", "followers": "12,345 Subscribers"},
            {"name": "Vimeo", "url": "#", "icon": "fab fa-vimeo-v", "color": "#055570", "followers": "12,345 Followers"},
        ]
    }

def categories_list(request):
    return{
        "CATEGORIES": [
            "Siyasət", "Biznes", "Korporativ", "Sağlamlıq", "Təhsil",
            "Elmlər", "Qidalar", "Əyləncə", "Səyahət", "Həyat tərzi"
        ]
    }

def site_settings(request):
    settings = SiteSettings.objects.first()  # İlk sətiri götür
    return {
        'site_settings': settings
    }

def current_date(request):
    return {'current_date': timezone.now().strftime('%A, %B %d, %Y')}