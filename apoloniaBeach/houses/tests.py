
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from apoloniaBeach.houses.forms import EditApartmentForm
from apoloniaBeach.houses.models import House, Apartment

User = get_user_model()


class AddApartmentViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User',
            nationality='Some nationality',
            phone_number='00000000',
            is_superuser=True,
        )
        self.house = House.objects.create(
            name='A',
            floors=1,
        )

        self.url = reverse('add-apartment')

    def test_add_appartment(self):
        self.client = Client()
        self.client.login(email='testuser@example.com', password='testpassword')

        response = self.client.post(self.url, {
            'house': self.house.pk,
            'number': '1',
            'apartment_area': 20,
            'common_parts_of_the_building': 1,
            'for_rental': False,
            'for_sale': False,
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Apartment.objects.count(), 1)

    def test_redirect_anonymous_user(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_non_permission(self):
        user = User.objects.create_user(
            email='test@test.com',
            password='testpassword',
            first_name='Test',
            last_name='User',
            nationality='Some nationality',
            phone_number='00000000',
        )
        self.client = Client()
        self.client.login(email='test@test.com', password='testpassword')
        response = self.client.post(self.url, {
            'house': self.house.pk,
            'number': '1',
            'apartment_area': 20,
            'common_parts_of_the_building': 1,
            'for_rental': False,
            'for_sale': False,
        })
        self.assertEqual(response.status_code, 403)


class EditApartmentFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'number': '1',
            'apartment_area': 20,
            'common_parts_of_the_building': 1,
            'for_rental': False,
            'for_sale': False,
        }

    def test_edit_apartment__form_true(self):
        form = EditApartmentForm(data=self.valid_data)

        self.assertTrue(form.is_valid())

    def test_edit_apartment__form_false(self):
        self.valid_data['number'] = '1a4'
        form = EditApartmentForm(data=self.valid_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'number': ['Number can start with number and finish with number or letter.']})


class ApartmentModelTest(TestCase):
    def setUp(self):
        self.house = House.objects.create(
            name='A',
            floors=1,
        )
        self.apartment = Apartment.objects.create(
            house=self.house,
            number='1',
            apartment_area=20,
            common_parts_of_the_building=1,
            for_rental=False,
            for_sale=False,
        )

    def test_apartment_full_area(self):
        self.assertEqual(self.apartment.get_full_area(), '21.00')

    def test_apartment_name(self):
        self.assertEqual(str(self.apartment), 'A1')
