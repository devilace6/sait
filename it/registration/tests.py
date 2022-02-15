from django.test import TestCase
from django.contrib.auth.models import User
from registration.forms import UserRegistrationForm

class TestSupportForm(TestCase):
    def test_request_created(self):
        email = "makss@mail.ru"
        username = "hello123"
        password = "123456"
        password2 = "123456"
        data = {
            "email": email,
            "username": username, "password": password, "password2": password2
        }
        form = UserRegistrationForm(data=data)
        self.assertTrue(form.is_valid())

    @classmethod
    def setUpTestData(cls):
        User.objects.create(email='maxim123@mail.ru', username='maksim')

    def test_first_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'имя пользователя')

    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length, 100)


