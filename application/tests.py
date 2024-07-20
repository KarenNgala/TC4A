from django.test import TestCase
from .models import Customer, Order


class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="Jane Doe", code="JD432", phone_number="1234567890")

    def test_customer_creation(self):
        jane = Customer.objects.get(name="Jane Doe")
        self.assertEqual(jane.code, "JD432")
        self.assertEqual(jane.phone_number, "1234567890")


class OrderTestCase(TestCase):
    def setUp(self):
        customer = Customer.objects.create(name="Jane Doe", code="JD432")
        Order.objects.create(customer=customer, item="Laptop", amount=35000.00)

    def test_order_creation(self):
        order = Order.objects.get(item="Laptop")
        self.assertEqual(order.amount, 35000.00)

