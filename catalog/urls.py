from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts, product_detail

app_name = 'catalog'

urlpatterns = [
    path('', index, name='home'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('contacts/', contacts, name='contacts')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
