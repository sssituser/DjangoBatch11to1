from django.urls import path

from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.register, name='register'),
    path('show/', views.show, name='show'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)