from django.test import TestCase
from restaurant.models import Menu


class MenuTestCase(TestCase):
    
    def setUp(self):
        Menu.objects.create(item='Icecream', price=100.00, inventory=100)
    def test_get_item(self):
        menu_item_object = Menu.objects.get(item='Icecream')
        menu_item = Menu.objects.create(item='Icecream2', price=100.00, inventory=100)
        menu_item_str = menu_item.get_item()
        self.assertEqual(menu_item_str, 'Icecream2 : 100.0')
        self.assertEqual(menu_item_object.item, 'Icecream')
        self.assertEqual(menu_item_object.price, 100.00)
        self.assertEqual(menu_item_object.inventory, 100)
        
    def test_get_all(self):
        menu_item_object = Menu.objects.get()
        self.assertEqual(menu_item_object.item, 'Icecream')
        self.assertEqual(menu_item_object.price, 100.00)
        self.assertEqual(menu_item_object.inventory, 100)