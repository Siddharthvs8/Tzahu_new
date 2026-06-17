from django.contrib import admin
from .models import SiteSetting, CarouselImage, Program, Feature, Plan, Testimonial, ContactSubmission, Event, Speaker, BrochureLead

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Brand', {'fields': ('site_name','tagline','logo','primary_color','accent_color','text_color')}),
        ('Contact', {'fields': ('phone','email','location')}),
        ('Socials', {'fields': ('instagram_url','linkedin_url','youtube_url')}),
        ('Hero', {'fields': ('hero_badge','hero_headline','hero_subheadline','cta_primary_text','cta_secondary_text')}),
        ('Footer', {'fields': ('footer_text',)}),
        ('Automation', {
            'fields': ('whatsapp_number', 'whatsapp_webhook_url', 'google_sheets_webhook_url'),
            'description': 'Configure external lead sync here.'
        }),
    )

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('order', 'alt_text', 'caption')
    list_editable = ('order',)
    list_display_links = ('alt_text',)  # clickable link

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'tag')
    list_editable = ('order',)
    list_display_links = ('title',)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'text')
    list_editable = ('order',)
    list_display_links = ('title',)

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'price_label', 'highlight')
    list_editable = ('order', 'highlight')
    list_display_links = ('name',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'role')
    list_editable = ('order',)
    list_display_links = ('name',)

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','created_at')
    readonly_fields = ('created_at',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'price', 'early_bird_price', 'early_bird_deadline')
    search_fields = ('title', 'description', 'detailed_description')
    list_filter = ('date',)
    filter_horizontal = ('speakers',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'detailed_description', 'date', 'location', 'thumbnail', 'image', 'speakers', 'brochure')
        }),
        ('Pricing & Offers', {
            'fields': ('price', 'early_bird_price', 'early_bird_deadline')
        }),
    )

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'company')
    search_fields = ('name', 'company', 'role')

@admin.register(BrochureLead)
class BrochureLeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'event', 'created_at')
    list_filter = ('event', 'created_at')
    search_fields = ('name', 'phone', 'event__title')
    readonly_fields = ('created_at',)
