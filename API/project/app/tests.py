from django.test import TestCase
from .models import Pereval

class PerevalModelTest(TestCase):
    def setUp(self):
        self.pereval = Pereval.objects.create(
            beauty_title='Test Beauty Title',
            title='Test Title',
            other_titles='Test Other Titles',
            connect='Test Connect',
            user_email='test@test.com',
            user_fam='Test Fam',
            user_name='Test Name',
            user_otc='Test Otc',
            user_phone='1234567890',
            latitude=12.345678,
            longitude=98.765432,
            height=1000,
            winter_level='Test Winter Level',
            summer_level='Test Summer Level',
            autumn_level='Test Autumn Level',
            spring_level='Test Spring Level',
            status='new'
        )

    def test_pereval_model(self):
        self.assertEqual(self.pereval.beauty_title, 'Test Beauty Title')
        self.assertEqual(self.pereval.title, 'Test Title')
        self.assertEqual(self.pereval.other_titles, 'Test Other Titles')
        self.assertEqual(self.pereval.connect, 'Test Connect')
        self.assertEqual(self.pereval.user_email, 'test@test.com')
        self.assertEqual(self.pereval.user_fam, 'Test Fam')
        self.assertEqual(self.pereval.user_name, 'Test Name')
        self.assertEqual(self.pereval.user_otc, 'Test Otc')
        self.assertEqual(self.pereval.user_phone, '1234567890')
        self.assertEqual(float(self.pereval.latitude), 12.345678)
        self.assertEqual(float(self.pereval.longitude), 98.765432)
        self.assertEqual(self.pereval.height, 1000)
        self.assertEqual(self.pereval.winter_level, 'Test Winter Level')
        self.assertEqual(self.pereval.summer_level, 'Test Summer Level')
        self.assertEqual(self.pereval.autumn_level, 'Test Autumn Level')
        self.assertEqual(self.pereval.spring_level, 'Test Spring Level')
        self.assertEqual(self.pereval.status, 'new')
