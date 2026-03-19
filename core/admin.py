from django.contrib import admin
from .models import SiteSetting, CarouselImage, Program, Feature, Plan, Testimonial, ContactSubmission

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Brand', {'fields': ('site_name','tagline','logo','primary_color','accent_color','text_color')}),
        ('Contact', {'fields': ('phone','email','location')}),
        ('Socials', {'fields': ('instagram_url','linkedin_url','youtube_url')}),
        ('Hero', {'fields': ('hero_badge','hero_headline','hero_subheadline','cta_primary_text','cta_secondary_text')}),
        ('Footer', {'fields': ('footer_text',)}),
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
