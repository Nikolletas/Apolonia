from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from apoloniaBeach.albums.models import Album
from apoloniaBeach.choices import PhotoTypesChoices
from apoloniaBeach.houses.models import Apartment, House

User = get_user_model()


class AddCommonPhotoViewTest(TestCase):
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
            floors=1,
        )
        self.apartment = Apartment.objects.create(
            house=self.house,
            number=1,
            apartment_area=20,
            common_parts_of_the_building=1,
        )
        self.user.apartment.add(self.apartment)

        self.url = reverse('photo-common-add')

    def test_add_common_photo_authenticated_user(self):
        self.client = Client()
        self.client.login(email='testuser@example.com', password='testpassword')
        uploaded_file = SimpleUploadedFile(
            name='sample_photo.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\xff\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',
            content_type='image/jpeg'
        )

        response = self.client.post(self.url, {
            'photo': uploaded_file,
            'description': 'Sample description',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Album.objects.count(), 1)

        album = Album.objects.first()
        self.assertEqual(album.photo_type, PhotoTypesChoices.COMMON)
        self.assertEqual(album.published_by, self.user)
        self.assertEqual(album.description, 'Sample description')

    def test_redirect_anonymous_user(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_non_apartment_owner_forbidden(self):
        self.client = Client()
        self.client.login(email='testuser@example.com', password='testpassword')
        self.user.apartment.clear()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)
