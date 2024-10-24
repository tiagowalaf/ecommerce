from django.contrib import admin
from django.urls import path, include
from configurations import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('ecommerce.urls')),
    path('admin/', admin.site.urls),
    path('register/', include('crtuser.urls'))
]
# urlpatterns += static(settings.STATIC_URL, )