from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Optional: Customize Django Admin titles
admin.site.site_header = "Car Dealer Admin"
admin.site.site_title = "Car Dealer Portal"
admin.site.index_title = "Welcome to the Car Dealer Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('cars/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),  # your custom account routes + allauth
    path('contacts/', include('contacts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
