from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CarouselImage, Program, Feature, Plan, Testimonial, ContactSubmission, SiteSetting, Event, Speaker, BrochureLead
from django.contrib.auth.decorators import user_passes_test
from .forms import ContactForm
from .automation import send_to_whatsapp, send_to_google_sheets

# ... (omitted code for brevity, but let's replace lines 3 to 71 carefully)


def home(request):
    programs = Program.objects.all()
    features = Feature.objects.all()
    plans = Plan.objects.all()
    testimonials = Testimonial.objects.all()
    slides = CarouselImage.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # AUTOMATION
            try:
                settings = SiteSetting.objects.first()
                lead_data = {
                    "name": contact.name,
                    "email": contact.email,
                    "phone": contact.phone,
                    "message": contact.message,
                    "timestamp": str(contact.created_at)
                }
                # Non-blocking automation triggers
                send_to_whatsapp(lead_data, settings)
                send_to_google_sheets(lead_data, settings)
            except Exception as e:
                # Log error but don't disrupt user experience
                print(f"Automation error: {e}")

            messages.success(request, "Thanks! We'll get back to you within 24 hours.")
            return redirect('home')
    else:
        form = ContactForm()

    ctx = {
        'programs': programs,
        'features': features,
        'plans': plans,
        'testimonials': testimonials,
        'slides': slides,
        'form': form,
    }
    return render(request, 'home.html', ctx)

@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    # Summary Counts
    counts = {
        'programs': Program.objects.count(),
        'features': Feature.objects.count(),
        'plans': Plan.objects.count(),
        'testimonials': Testimonial.objects.count(),
        'contact_submissions': ContactSubmission.objects.count(),
        'slides': CarouselImage.objects.count(),
        'events': Event.objects.count(),
        'speakers': Speaker.objects.count(),
        'brochure_leads': BrochureLead.objects.count(),
    }

    # Recent submissions
    recent_submissions = ContactSubmission.objects.order_by('-created_at')[:10]
    recent_event_submissions = BrochureLead.objects.order_by('-created_at')[:10]

    ctx = {
        'counts': counts,
        'recent_submissions': recent_submissions,
        'recent_event_submissions': recent_event_submissions,
    }
    return render(request, 'admin_dashboard.html', ctx)

def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '500.html', status=500)

def events_page(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events.html', {'events': events})

def event_detail(request, event_id):
    from django.shortcuts import get_object_or_404
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})

from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def download_brochure(request, event_id):
    from django.shortcuts import get_object_or_404
    event = get_object_or_404(Event, id=event_id)
    
    if not event.brochure:
        return JsonResponse({"status": "error", "message": "No brochure available for this event."}, status=400)
        
    name = request.POST.get('name', '').strip()
    phone = request.POST.get('phone', '').strip()
    
    if not name or not phone:
        return JsonResponse({"status": "error", "message": "Name and phone number are required."}, status=400)
        
    # Save lead
    lead = BrochureLead.objects.create(event=event, name=name, phone=phone)
    
    # Trigger automation notifications
    try:
        settings = SiteSetting.objects.first()
        lead_data = {
            "name": lead.name,
            "email": "N/A (Brochure)",
            "phone": lead.phone,
            "message": f"Downloaded brochure for event: {event.title}",
            "timestamp": str(lead.created_at)
        }
        send_to_whatsapp(lead_data, settings)
        send_to_google_sheets(lead_data, settings)
    except Exception as e:
        print(f"Automation error: {e}")
        
    return JsonResponse({
        "status": "success",
        "brochure_url": event.brochure.url,
        "message": "Thank you! Your download is starting."
    })
