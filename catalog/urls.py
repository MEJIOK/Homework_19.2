from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (IndexView, ProductDetailView, ContactsView)

app_name = 'catalog'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
