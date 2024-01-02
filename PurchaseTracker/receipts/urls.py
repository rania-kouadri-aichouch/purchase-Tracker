from django.urls import path
from .views import ReceiptListView, ReceiptDetailView, ReceiptCreateView, ReceiptUpdateView, ReceiptDeleteView

urlpatterns = [
    path('receipts/', ReceiptListView.as_view(), name='receipt-list'),
    path('receipts/<int:pk>/', ReceiptDetailView.as_view(), name='receipt-detail'),
    path('receipts/new/', ReceiptCreateView.as_view(), name='receipt-create'),
    path('receipts/<int:pk>/edit/', ReceiptUpdateView.as_view(), name='receipt-update'),
    path('receipts/<int:pk>/delete/', ReceiptDeleteView.as_view(), name='receipt-delete'),
]
