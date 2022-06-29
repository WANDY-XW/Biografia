from django.contrib import admin
from django.urls import path, include


urlpatterns = [
  
    path('', include('Bios.urls')),
    # path('wandyadminxw/'),
    path('admin/', admin.site.urls),
]
