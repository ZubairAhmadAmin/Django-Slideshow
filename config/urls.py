from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from slideshow.views import change_lang

urlpatterns = [
    path('change_lang/', change_lang, name='change_lang')
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('slideshow.urls')),
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)