from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Receipt
from .forms import ReceiptForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator



# get all receipts
class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = 'receipt_list.html'
    context_object_name = 'receipts'
    paginate_by = 5  # Number of receipts per page

    def get_queryset(self):
        return Receipt.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            receipts = paginator.page(page)
        except Exception as e:
            # If the page is not an integer, deliver the first page.
            receipts = paginator.page(1)

        context['receipts'] = receipts
        return context

# details
class ReceiptDetailView(DetailView):
    model = Receipt
    template_name = 'receipt_detail.html'
    context_object_name = 'receipt'


# create view
class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'receipt_form.html'
    success_url = reverse_lazy('receipt-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# update receipt view
class ReceiptUpdateView(UpdateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'receipt_update.html'
    success_url = reverse_lazy('receipt-list')


# deleteView
class ReceiptDeleteView(DeleteView):
    model = Receipt
    template_name = 'receipt_confirm_delete.html'
    success_url = reverse_lazy('receipt-list')
