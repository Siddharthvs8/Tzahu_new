from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CarouselImage, Program, Feature, Plan, Testimonial, ContactSubmission, SiteSetting
from django.contrib.auth.decorators import user_passes_test
from .forms import ContactForm
from .automation import send_to_whatsapp, send_to_google_sheets

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
    }

    # Recent submissions
    recent_submissions = ContactSubmission.objects.order_by('-created_at')[:10]

    ctx = {
        'counts': counts,
        'recent_submissions': recent_submissions,
    }
    return render(request, 'admin_dashboard.html', ctx)

def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '500.html', status=500)
