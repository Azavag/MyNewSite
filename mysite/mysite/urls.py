from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('main', include('main.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'), name='polls'),
    path('blogs/', include('blogs.urls'), name='blogs'),
    path('', include('User.urls'), name='User'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

