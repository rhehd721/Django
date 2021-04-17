# Urls
- path = Project/urls.py
- 내가만든 HTML이 어떤 URL 주소 입력시 띄워질지 지정

```python
from django.contrib import admin
from django.urls import path
import App.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', App.views.index, name = "index"),
]
```