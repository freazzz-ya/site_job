from django.test import TestCase

from job.models import Job, Other_Source_model


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

    def test_successful_creation_job(self):
        news_count = Job.objects.count()
        self.assertEqual(news_count, 1)

    def test_successful_creation_other_source_model(self):
        news_count = Other_Source_model.objects.count()
        self.assertEqual(news_count, 1)
