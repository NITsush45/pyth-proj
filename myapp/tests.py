from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Bank, Branch

class BankTests(APITestCase):
    def setUp(self):
        self.bank = Bank.objects.create(name="Test Bank")
        self.branch = Branch.objects.create(
            bank_id=self.bank,
            ifsc="TEST1234",
            branch="Test Branch",
            address="Test Address",
            city="Test City",
            district="Test District",
            state="Test State"
        )

    def test_get_banks(self):
        response = self.client.get(reverse('bank-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Bank', str(response.content))

    def test_get_branches(self):
        response = self.client.get(reverse('branch-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Branch', str(response.content))

