from django.test import TestCase

from store.models import Category, Product
from django.contrib.auth.models import User


class TestCategoryModel(TestCase):

    def setUp(self):
        self.data1 =  Category.objects.create(name='testCat', slug='testCat')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field/return attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data,Category))
        self.assertEqual(str(data),'testCat')


class TestProductModel(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name='testCat', slug='testCat')
        User.objects.create(username='admin')
        self.data1 =  Product.objects.create(category_id=1, title='test product', created_by_id=1, 
                                            slug='test-product', price='300.00', image='test')

    def test_product_model_entry(self):
        """
        Test Product model data insertion/types/field/return attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data,Product))
        self.assertEqual(str(data), 'test product')