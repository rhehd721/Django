# Static
- path = App/static

## Setting.py에게 Static의 존재 알리기
- setting.py
```python
STATIC_URL = '/static/'

# STATIC_DIR = os.path.join(BASE_DIR, 'APP_Name', 'static_folder_name')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    STATIC_DIR,
] # static 파일들이 현재 어디에 존재하는지

# static 파일들이 어디로 모일것인지
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
- python3 manage.py collectstatic
- {% load staticfiles %}
```html
<!-- HTML -->
{% load static %}
<img src = "{% static 'test.jpg' %}">
```

## Media
- setting.py
```python
MEDIA_URL = '/media/'

# media 파일들이 어디로 모일것인지
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
- urls.py애 media 존재 알리기
```python
from django.contrib import admin
from django.urls import path
import App.views
from django.conf import settings    # 추가
from django.conf.urls.static import static    # 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', App.views.index, name = "index")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # 추가
```
- pip install pillow
- models.py
```python
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	photo = models.ImageField(upload_to 'images/')

    def __str__(self):
        return self.title
```