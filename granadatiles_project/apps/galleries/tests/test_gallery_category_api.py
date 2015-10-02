from rest_framework import status
from rest_framework.test import APITestCase

class GalleryCategoryAPITest(APITestCase):

    def test_images_404(self):
        response = self.client.get('/api/galleriescategories/1/images/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
