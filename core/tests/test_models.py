from django.test import TestCase
from core.models import Program, Plan

class ModelMethodTests(TestCase):
    def test_program_points_split(self):
        p = Program.objects.create(tag='X', title='Y', points_text='One\nTwo\n\nThree', order=1)
        self.assertEqual(p.points(), ['One','Two','Three'])

    def test_plan_perks_split(self):
        pl = Plan.objects.create(name='Starter', price_label='₹', highlight=False, perks_text='A\nB\nC', order=1)
        self.assertEqual(pl.perks(), ['A','B','C'])
