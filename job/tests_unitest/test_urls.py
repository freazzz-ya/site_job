# news/tests/test_routes.py
from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse

from users.models import Worker


class TestUrl(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создаём пользователя.
        cls.user = Worker.objects.create(username='testUser')
        cls.user_special = Worker.objects.create(
            username='testUser2', role='Special',
            email='Max@mail.ru',
        )
        # Создаём объект клиента.
        cls.user_client = Client()
        cls.user_client_special = Client()
        # "Логинимся" в клиенте при помощи метода force_login().
        cls.user_client.force_login(cls.user)
        cls.user_client_special.force_login(
            cls.user_special
        )
        # Теперь через этот клиент можно отправлять запросы
        # от имени пользователя с логином "testUser"

    def test_successful_creation_job(self):
        news_count = Worker.objects.count()
        self.assertEqual(news_count, 2)

    def test_home_page(self):
        url = reverse('job:job_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_neuronet_page(self):
        url = reverse('job:neiro_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_profile(self):
        url = reverse('job:finance_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_profile_auth(self):
        url = reverse('job:finance_view')
        response = self.user_client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_finance_add_work(self):
        url = reverse('job:finance_add_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_finance_add_work_auth(self):
        url = reverse('job:finance_add_view')
        response = self.user_client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_finance_other_add_view(self):
        url = reverse('job:finance_other_add_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_finance_other_add_view_auth(self):
        url = reverse('job:finance_other_add_view')
        response = self.user_client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_finance_list_view(self):
        url = reverse('job:finance_list_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        response_auth = self.user_client.get(url)
        self.assertEqual(response_auth.status_code, HTTPStatus.OK)

    def test_finance_list_view_auth(self):
        url = reverse('job:finance_list_view')
        response = self.user_client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_special_view(self):
        url = reverse('job:special_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        response_auth = self.user_client.get(url)
        self.assertEqual(response_auth.status_code, HTTPStatus.FOUND)
        response_auth_special = self.user_client_special.get(url)
        self.assertEqual(response_auth_special.status_code, HTTPStatus.OK)

    def test_calculation_view(self):
        # Test anonymous user
        url = reverse('job:finance_calculation')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        # Test logged-in user
        response_login_client = self.user_client.get(url)
        self.assertEqual(response_login_client.status_code, HTTPStatus.OK)

    def test_finance_list_expenses_view(self):
        url = reverse('job:finance_list_expenses_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        # Test logged-in user
        response_login_client = self.user_client.get(url)
        self.assertEqual(response_login_client.status_code, HTTPStatus.OK)

    def test_profile_edit_view(self):
        url = reverse('job:profile_edit')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        # Test logged-in user
        response_login_client = self.user_client.get(url)
        self.assertEqual(response_login_client.status_code, HTTPStatus.OK)
