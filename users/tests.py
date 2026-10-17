from django.test import TestCase
from django.urls import reverse

from .models import User

PASSWORD = 'Sup3r-Secret-Pass!'


class RegisterTests(TestCase):
    def register(self, **overrides):
        data = {
            'username': 'ali',
            'first_name': 'Ali',
            'last_name': 'Valiyev',
            'email': 'ali@example.com',
            'birth_date': '2000-01-31',
            'password1': PASSWORD,
            'password2': PASSWORD,
        }
        data.update(overrides)
        return self.client.post(reverse('register'), data)

    def test_register_hashes_password_and_logs_in(self):
        response = self.register()

        self.assertRedirects(response, reverse('user_home'))
        user = User.objects.get(username='ali')
        self.assertNotEqual(user.password, PASSWORD)
        self.assertTrue(user.check_password(PASSWORD))
        self.assertEqual(int(self.client.session['_auth_user_id']), user.pk)

    def test_password_mismatch_is_rejected(self):
        response = self.register(password2='something-else-123')

        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.exists())

    def test_duplicate_email_is_rejected(self):
        User.objects.create_user('first', 'ali@example.com', PASSWORD)

        self.register()

        self.assertFalse(User.objects.filter(username='ali').exists())


class LoginTests(TestCase):
    def setUp(self):
        User.objects.create_user('ali', 'ali@example.com', PASSWORD)

    def test_login_with_correct_password(self):
        response = self.client.post(reverse('login'), {'username': 'ali', 'password': PASSWORD})

        self.assertRedirects(response, reverse('user_home'))

    def test_login_with_another_users_password_fails(self):
        User.objects.create_user('bob', 'bob@example.com', 'Other-Pass-456!')

        response = self.client.post(reverse('login'), {'username': 'ali', 'password': 'Other-Pass-456!'})

        self.assertEqual(response.status_code, 200)
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_home_requires_login(self):
        response = self.client.get(reverse('user_home'))

        self.assertRedirects(response, f"{reverse('login')}?next={reverse('user_home')}")

    def test_logout(self):
        self.client.login(username='ali', password=PASSWORD)

        response = self.client.post(reverse('logout'))

        self.assertRedirects(response, reverse('login'))
        self.assertNotIn('_auth_user_id', self.client.session)
