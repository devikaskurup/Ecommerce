from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


from Public import urls
import Public  
from Product import urls
import Product  
from cart import urls
import cart


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(Public.urls)),
    path("product/",include(Product.urls)),
    path("cart/",include(cart.urls)),
]
urlpatterns =urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)