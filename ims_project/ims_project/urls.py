# project/urls.py

from django.contrib import admin
from django.urls import path, include  # include is necessary for app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),  # Include the app's URLs
]
