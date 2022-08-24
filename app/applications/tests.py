import os

import django
from django.db.utils import IntegrityError
from django.test import TestCase

# from sqlite3 import IntegrityError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings_test')
django.setup()


# Create your tests here.
class ApplicationAPITest(TestCase):
    url = '/applications'
    detail_url = url + '/1'

    def test_create(self):
        data = {
            'user': 1,
            'post': 2
        }
        response = self.client.post(self.url, data)
        # 요청이 성공적으로 처리되었는지 확인
        self.assertEqual(response.status_code, 201)

    def test_integrity(self):
        data = {
            'user': 1,
            'post': 1
        }
        # IntegrityError가 발생하는지 확인
        with self.assertRaises(IntegrityError) as context:
            self.client.post(self.url, data)
        self.assertTrue('UNIQUE constraint failed' in str(context.exception))

    def test_destroy(self):
        response = self.client.delete(self.detail_url)
        # 요청이 성공적으로 처리되었는지 확인
        self.assertEqual(response.status_code, 204)
