from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=120, default='TZaHu')
    tagline = models.CharField(max_length=200, blank=True, default='The Sales Hunter')
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    primary_color = models.CharField(max_length=7, default='#000000')  # black
    accent_color = models.CharField(max_length=7, default='#f5c518')  # gold
    text_color = models.CharField(max_length=7, default='#eaeaea')

    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=120, blank=True, default='Kochi • Kerala • India')

    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    hero_badge = models.CharField(max_length=160, blank=True, default='Proven playbooks • 100% placement support')
    hero_headline = models.CharField(max_length=160, default='Build a hunter-class sales engine.')
    hero_subheadline = models.TextField(blank=True, default='We train teams, place talent, and design revenue systems for entrepreneurs, freshers, and growing companies. Scripts, cadences, and strategy—delivered.')
    cta_primary_text = models.CharField(max_length=60, default='Get Free Audit →')
    cta_secondary_text = models.CharField(max_length=60, default='Explore Programs')

    footer_text = models.CharField(max_length=200, blank=True, default='All rights reserved.')

    class Meta:
        verbose_name = 'Site Setting (create exactly one)'
        verbose_name_plural = 'Site Setting'

    def __str__(self):
        return 'Site Settings'

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel/')
    alt_text = models.CharField(max_length=200, blank=True)
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.alt_text or f'Carousel #{self.pk}'

class Program(models.Model):
    tag = models.CharField(max_length=80)
    title = models.CharField(max_length=160)
    points_text = models.TextField(help_text='One bullet per line')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def points(self):
        return [p.strip() for p in self.points_text.splitlines() if p.strip()]

    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=240)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title

class Plan(models.Model):
    name = models.CharField(max_length=120)
    price_label = models.CharField(max_length=120, help_text='e.g., ₹50,000 / month or Custom')
    highlight = models.BooleanField(default=False)
    perks_text = models.TextField(help_text='One bullet per line')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def perks(self):
        return [p.strip() for p in self.perks_text.splitlines() if p.strip()]

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=160, blank=True)
    quote = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.name} — {self.role}' if self.role else self.name

class ContactSubmission(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} <{self.email}>'
