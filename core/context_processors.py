from django.utils import timezone
from .models import SiteSetting, Event

def site_settings(request):
    settings = SiteSetting.objects.first()
    upcoming_events_count = Event.objects.filter(date__gte=timezone.now()).count()
    return {
        'SITE': settings,
        'UPCOMING_EVENTS_COUNT': upcoming_events_count,
        'HAS_NEW_EVENTS': upcoming_events_count > 0,
    }
