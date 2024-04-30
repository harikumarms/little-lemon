from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.   

class MenuModelAPITest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='Abc123456!')
        self.client.force_authenticate(user=user)

    def test_add_menu(self):
        url = '/api/v1/restaurant/menu'
        data = {'item': 'Sambar', 'price': 20.00, 'inventory': 20}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_all(self):
        url = '/api/v1/restaurant/menu'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)