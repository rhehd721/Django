# Urls
- path = Project/urls.py
- 내가만든 HTML이 어떤 URL 주소 입력시 띄워질지 지정

```python
from django.contrib import admin
from django.urls import path
import App.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', App.views.index, name = "index"),  # views.py 불러오기
]
```

## Pk 지정하기 (특정 게시물 보여주기)
- models.py
```python
from django.db import models

class Test_Model(models.Model):
    title       = models.CharField(max_length=200)
    contents    = models.TextField()

    # model에 의해 새로운 객체가 생성될 때 이름을 title로 지정한다.
    def __str__(self):
        return self.title
```
- urls.py
```python
from django.contrib import admin
from django.urls import path
import App.views

urlpatterns = [
    # path_fomat = path('url이름', 함수, path이름)
    # path의 첫번째 인자 즉, 'url이름'은 험수에 즉, views 전달되는 파라미터이다.
    path('admin/', admin.site.urls),
    path('', App.views.home, name = 'home'),
    path('test/<int:user_id>', App.views.detail, name = "detail"),
    # path converter <type : 이름>
]
```
- views.py + get_object_or_404
get_object_or_404(어떤 클래스, 검색조건)
```python
from django.shortcuts import render, get_object_or_404
from .models import Test_Model

def detail(request, user_id):
    detail_ = get_object_or_404(Test_Model, pk = user_id)
    return render (request, 'detail.html', {'detail_' : detail_})
```
- index.html
```html
<!-- Query Set Method애 관해 찾아보기 -->
{% for i in Test_Model.all %}
    <h1> {{Test_Model.title}} </h1>
    <h2> {{Test_Model.contents}} </h2>
    <a herf = "{% url 'detail_' Test_Model.id ">...clik</a>
{% endfor %}
```

## APP에서 URL 관리하기
- Project/urls.py
```python
from django.contrib import admin
from django.urls import path, include   # import include


urlpatterns = [
    path('', include('App.urls')),  # include() 함수를 통해 다른 app에 url을 불러온다
    path('accounts/', include('accounts.urls')),  # include() 함수를 통해 다른 app에 url을 불러온다
    path('admin/', admin.site.urls),
]
```