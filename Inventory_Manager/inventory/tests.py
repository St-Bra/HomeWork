from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Product

class ProductAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')

        # Получение JWT токена
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.token = response.data['access']
        self.auth_header = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}

    def test_create_product(self):
        url = reverse('product-list')  # /api/products/
        data = {
            'name': 'Test Product',
            'art': 'TP12345',
            'description': 'Test description',
        }
        response = self.client.post(url, data, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.first().name, 'Test Product')

    def test_list_products(self):
        Product.objects.create(name='Test1', art='A1')
        Product.objects.create(name='Test2', art='A2')
        url = reverse('product-list')
        response = self.client.get(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_product(self):
        product = Product.objects.create(name='Test1', art='A1')
        url = reverse('product-detail', kwargs={'pk': product.pk})
        response = self.client.get(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test1')

    def test_update_product(self):
        product = Product.objects.create(name='Test1', art='A1')
        url = reverse('product-detail', kwargs={'pk': product.pk})
        data = {'name': 'Updated Product', 'art': 'A1'}
        response = self.client.put(url, data, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.name, 'Updated Product')

    def test_delete_product(self):
        product = Product.objects.create(name='Test1', art='A1')
        url = reverse('product-detail', kwargs={'pk': product.pk})
        response = self.client.delete(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)


