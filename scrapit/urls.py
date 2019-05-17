from scrapit import views
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf import settings

urlpatterns=[
    url(r'^home/$', views.home, name='home'),
    url(r'^$', views.register, name='register'),
    url(r'accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
