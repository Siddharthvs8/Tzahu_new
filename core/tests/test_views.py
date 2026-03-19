from django.test import TestCase
from django.urls import reverse
from core.models import SiteSetting, Program, Plan, Feature, Testimonial, ContactSubmission

class HomeViewTests(TestCase):
    def setUp(self):
        SiteSetting.objects.create(site_name='TZaHu', tagline='The Sales Hunter')
        Program.objects.create(tag='For Entrepreneurs', title='Business Lab', points_text='Point A\nPoint B', order=1)
        Plan.objects.create(name='Growth (Most Popular)', price_label='₹50,000 / month', highlight=True, perks_text='Perk 1', order=1)

    def test_home_status_ok(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('programs', resp.context)
        self.assertIn('plans', resp.context)

    def test_contact_post_creates_submission(self):
        data = {'name':'Test User','email':'test@example.com','phone':'','message':'Hello'}
        resp = self.client.post(reverse('home'), data)
        self.assertEqual(resp.status_code, 302)  # redirect on success
        self.assertEqual(ContactSubmission.objects.count(), 1)

    def test_growth_plan_highlighted(self):
        self.assertTrue(Plan.objects.filter(name__icontains='Growth', highlight=True).exists())
