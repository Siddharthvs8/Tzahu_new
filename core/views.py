from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CarouselImage, Program, Feature, Plan, Testimonial
from .forms import ContactForm

def home(request):
    programs = Program.objects.all()
    features = Feature.objects.all()
    plans = Plan.objects.all()
    testimonials = Testimonial.objects.all()
    slides = CarouselImage.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
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
