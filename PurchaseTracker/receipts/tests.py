from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Receipt
from django.urls import reverse

class ReceiptModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

        # Create a test receipt
        self.receipt = Receipt.objects.create(
            user=self.user,
            store_name='Test Store Name',
            date_of_purchase=timezone.now().date(),
            item_list='item 1, item 2',
            total_amount=2000.00,
        )

    def test_receipt_creation(self):
        # Test if the receipt is created successfully
        self.assertEqual(self.receipt.user, self.user)
        self.assertEqual(self.receipt.store_name, 'Test Store Name')
        self.assertEqual(self.receipt.date_of_purchase, timezone.now().date())
        self.assertEqual(self.receipt.item_list, 'item 1, item 2')
        self.assertEqual(self.receipt.total_amount, 2000.00)

    def test_receipt_str_representation(self):
        expected_str = f"Test Store Name - {timezone.now().date()}"
        self.assertEqual(str(self.receipt), expected_str)

    def test_receipt_meta_verbose_name_plural(self):
        self.assertEqual(str(Receipt._meta.verbose_name_plural), "Receipts")



class ReceiptListViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

        # Create some test receipts
        Receipt.objects.create(user=self.user, store_name='Store 1', date_of_purchase='2024-01-01', total_amount=5000.00)
        Receipt.objects.create(user=self.user, store_name='Store 2', date_of_purchase='2024-02-01', total_amount=4500.00)

    def test_receipt_list_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword123')

        # Test the return of 200 status code
        response = client.get(reverse('receipt-list'))
        self.assertEqual(response.status_code, 200)

        # Test that the correct template is used
        self.assertTemplateUsed(response, 'receipt_list.html')

        # Test that the number of receipts
        self.assertEqual(len(response.context['receipts']), 2)

class ReceiptDetailViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

        # Create a test receipt
        self.receipt = Receipt.objects.create(user=self.user, store_name='Test Store Name', date_of_purchase='2024-01-01', total_amount=5000.00)

    def test_receipt_detail_view(self):
        client = Client()

        # Test that the view returns a 200 status code
        response = client.get(reverse('receipt-detail', kwargs={'pk': self.receipt.pk}))
        self.assertEqual(response.status_code, 200)

        # Test that the correct template is used
        self.assertTemplateUsed(response, 'receipt_detail.html')

        # Test that the receipt in the context matches the created receipt
        self.assertEqual(response.context['receipt'], self.receipt)


class ReceiptCreateViewTest(TestCase):
    # create user
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

    def test_receipt_create_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword123')

        # Test that the view returns a 200 status code successfully
        response = client.get(reverse('receipt-create'))
        self.assertEqual(response.status_code, 200)

        # Test that the correct template is used
        self.assertTemplateUsed(response, 'receipt_form.html')

        # Test creating a new receipt
        data = {
            'store_name': 'New Store Name',
            'date_of_purchase': '2024-03-01',
            'item_list': 'Item 1, Item 2',
            'total_amount': 4000.00,
        }
        response = client.post(reverse('receipt-create'), data)
        
        # Check if the receipt is created successfully
        self.assertEqual(response.status_code, 302)  # Test successful redirect
        self.assertTrue(Receipt.objects.filter(user=self.user, store_name='New Store Name').exists())

class ReceiptUpdateViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

        # Create a test receipt
        self.receipt = Receipt.objects.create(user=self.user, store_name='Test Store Name', date_of_purchase='2024-01-01', total_amount=2000.00)

    def test_receipt_update_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword123')

        #Test 200 status code
        response = client.get(reverse('receipt-update', kwargs={'pk': self.receipt.pk}))
        self.assertEqual(response.status_code, 200)

        # Test that the correct template is used
        self.assertTemplateUsed(response, 'receipt_update.html')

        # Test updating the receipt
        data = {
            'store_name': 'Updated Store',
            'date_of_purchase': '2024-02-01',
            'item_list': 'Updated Item 1, Updated Item 2',
            'total_amount': 4500.00,
        }
        response = client.post(reverse('receipt-update', kwargs={'pk': self.receipt.pk}), data)
        
        # Check if the receipt is updated
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Receipt.objects.get(pk=self.receipt.pk).store_name, 'Updated Store')

class ReceiptDeleteViewTest(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpassword123')

        self.receipt = Receipt.objects.create(user=self.user, store_name='Test Store Name', date_of_purchase='2024-01-01', total_amount=2000.00)

    def test_receipt_delete_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword123')

        # Test that the view returns a 200 status code
        response = client.get(reverse('receipt-delete', kwargs={'pk': self.receipt.pk}))
        self.assertEqual(response.status_code, 200)

        # Test that the correct template is used
        self.assertTemplateUsed(response, 'receipt_confirm_delete.html')

        # Test deleting the receipt
        response = client.post(reverse('receipt-delete', kwargs={'pk': self.receipt.pk}))
        self.assertEqual(response.status_code, 302)  
        self.assertFalse(Receipt.objects.filter(pk=self.receipt.pk).exists())

