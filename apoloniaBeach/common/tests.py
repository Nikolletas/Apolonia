from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from apoloniaBeach.choices import DocumentChoices
from apoloniaBeach.common.models import Announcement
from apoloniaBeach.houses.models import House, Apartment

User = get_user_model()


class AnnouncementEditViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User',
            nationality='Some nationality',
            phone_number='00000000',
        )

        self.house = House.objects.create(
            name='A',
            floors=3,
        )
        self.apartment = Apartment.objects.create(
            house=self.house,
            number=1,
            apartment_area=20,
            common_parts_of_the_building=1,
        )
        self.user.apartment.add(self.apartment)

        self.announcement = Announcement.objects.create(
            title='Test',
            content='Some Content',
            category=DocumentChoices.OTHER,
            posted_by=self.user,
            date_posted=datetime.now()
        )

        self.url = reverse('announcement-edit', kwargs={'pk': self.announcement.pk})

        self.client = Client()

    def test_edit_announcement_as_owner(self):
        self.client.login(email='testuser@example.com', password='testpassword')
        response = self.client.post(self.url, {
            'title': 'Other Test',
            'content': 'Other Content',
            'category': DocumentChoices.OTHER,
        })

        self.assertEqual(Announcement.objects.all().count(), 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('announcements'))

        self.announcement.refresh_from_db()

        self.assertEqual(self.announcement.title, 'Other Test')
        self.assertEqual(self.announcement.content, 'Other Content')

    def test_edit_announcement_as_non_owner(self):
        other_user = User.objects.create_user(
            email='otheruser@example.com',
            password='otherpassword',
            first_name='Test',
            last_name='User',
            nationality='Some nationality',
            phone_number='00000000',
        )
        self.client.login(email='otheruser@example.com', password='otherpassword')
        response = self.client.post(self.url, {
            'title': 'Malicious Update',
            'content': 'Hacked content!',
            'category': DocumentChoices.OTHER,
        })

        self.assertEqual(response.status_code, 403)

        self.announcement.refresh_from_db()
        self.assertEqual(self.announcement.title, 'Test')
        self.assertEqual(self.announcement.content, 'Some Content')

