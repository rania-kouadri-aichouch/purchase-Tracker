
from django.contrib import admin
from django.urls import include, path
from .views import landing_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing'),
    path('accounts/', include('accounts.urls')), 
    path('receipts/', include('receipts.urls')), 


]
