from django.test import TestCase

# Импортируем модель, чтобы работать с ней в тестах.
from job.models import Neural_network, Job, Other_Source_model


class TestNews(TestCase):
    CHAR_FIELD_MAX_LEN = 256
    TITLE = 'Заголовок новости'
    DISCRIPTION = 'Тестовый текст'

    @classmethod
    def setUpTestData(cls):
        cls.job = Job.objects.create(
            title=cls.TITLE,
            discription=cls.DISCRIPTION,
        )
        cls.other_source_model = Other_Source_model.objects.create(
            title='Заголовок новости',
            discription='Тестовый текст',
        )

    def test_successful_creation_Job(self):
        news_count = Job.objects.count()
        self.assertEqual(news_count, 1)

    def test_successful_creation_Other_Source_model(self):
        news_count = Other_Source_model.objects.count()
        self.assertEqual(news_count, 1)
