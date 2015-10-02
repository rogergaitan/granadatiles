from rest_framework import status
from rest_framework.test import  APITestCase


class SectionTest(APITestCase):


    def test_section_list_200(self):
        response = self.client.get('/api/sections/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_section_cover_404(self):
        response = self.client.get('/api/section/1/cover')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_section_retrieve_404(self):
        response = self.client.get('/api/section/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
