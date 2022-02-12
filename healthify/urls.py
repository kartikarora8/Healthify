from django.contrib import admin
from django.urls import path, include

from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('noentry/', admin.site.urls),
    path('patient/', include('patient.urls')),
    path('labs/', include('labs.urls')),
    path('doctors/', include('doctors.urls')),
    path('', include('administration.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)