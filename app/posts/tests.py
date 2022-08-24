import os

import django
from django.test import TestCase

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings_test')
django.setup()


# Create your tests here.
class PostAPITests(TestCase):
    url = '/posts'
    detail_url = url + '/1'

    def test_list(self):
        response = self.client.get(self.url)
        # 요청이 성공적으로 처리되었는지 확인
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        response = self.client.get(self.url + '?search=Python')
        # 요청이 성공적으로 처리되었는지 확인
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        data = {
            'company': 3,
            'position': 'Django 백엔드 개발자',
            'reward': 1000000,
            'skill': 'Django',
            'content': '네이버에서 백엔드 개발자를 채용합니다.'
        }
        response = self.client.post(self.url, data)
        # 요청이 성공적으로 처리되었는지 확인
        self.assertEqual(response.status_code, 201)

    def test_create_bad_request(self):
        data = {
            'position': 'Django 백엔드 개발자',
            'reward': 1000000,
            'skill': 'Django',
            'content': '네이버에서 백엔드 개발자를 채용합니다.'
        }
        response = self.client.post(self.url, data)
        # Bad Request인지 확인
        self.assertEqual(response.status_code, 400)

    def test_retrieve(self):
        response = self.client.get(self.detail_url)
        # 요청이 성공적으로 처리되었는지 확인
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        data = {
            'id': 1,
            'skill': 'Django',
            'content': "원티드랩에서 백엔드 주니어 개발자를 '적극' 채용합니다.",
        }
        response = self.client.patch(self.detail_url, data, content_type="application/json")
        # 요청이 성공적으로 처리되었는지 확인
        self.assertEqual(response.status_code, 200)

        # 데이터가 제대로 업데이트 되었는지 확인
        response = self.client.get(self.detail_url)
        new_data = response.data
        self.assertEqual(new_data['id'], data['id'])
        self.assertEqual(new_data['skill'], data['skill'])
        self.assertEqual(new_data['content'], data['content'])

    def test_destroy(self):
        response = self.client.delete(self.detail_url)
        # 요청이 성공적으로 처리되었는지 확인
        self.assertEqual(response.status_code, 204)

        # 데이터가 제대로 삭제되었는지 확인
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 404)
