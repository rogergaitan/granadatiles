from rest_framework import status
from rest_framework.test import APITestCase


class GalleryAPITest(APITestCase):

     def test_gallery_list_200(self):
         response = self.client.get('/api/galleries/')
         self.assertEqual(response.status_code, status.HTTP_200_OK)
