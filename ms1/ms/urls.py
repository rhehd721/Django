
from django.contrib import admin
from django.urls import path
import msapp.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', msapp.views.home, name='home'),
    path('introduce/', msapp.views.introduce, name='introduce'),
    path('test1/', msapp.views.test1, name='test1'),
    path('test2/', msapp.views.test2, name='test2'),
    path('profile/<int:designer_id>',  msapp.views.detail, name = "detail"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
