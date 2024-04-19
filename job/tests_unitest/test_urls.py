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
        # Создаём объект клиента.
        cls.user_client = Client()
        # "Логинимся" в клиенте при помощи метода force_login().
        cls.user_client.force_login(cls.user)
        # Теперь через этот клиент можно отправлять запросы
        # от имени пользователя с логином "testUser"

    def test_successful_creation_job(self):
        news_count = Worker.objects.count()
        self.assertEqual(news_count, 1)

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

    def test_finance_list_view_auth(self):
        url = reverse('job:finance_list_view')
        response = self.user_client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_special_view(self):
        url = reverse('job:special_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_special_view_auth(self):
        url = reverse('job:special_view')
        response = self.user_client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
