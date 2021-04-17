# Model
- DB를 다루는 파일

## 기본적인 Model 작성 Ex
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
- admin.py
```python
# 아래 작업을 통해 admin 페이지에서 우리가 만든 model을 관리 할 수 있다.
from django.contrib import admin
from .models import Test_Model

admin.site.register(Test_Model)
```

## Model에 내용을 HTML위에 출력하기
- 과정 : models.py -> views.py -> HTML
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
- views.py
```python
from django.shortcuts import render
from .models import Test_Model

def home(request):
    modle = Test_Model.objects    # Query Set
    return render (request, 'home.html', {"Test_Model" : modle})
```
- home.html
```html
<!-- Query Set Method애 관해 찾아보기 -->
{{Test_Model.all()}}
{% for i in Test_Model.all %}
    <h1> {{Test_Model.title}} </h1>
    <h2> {{Test_Model.contents}} </h2>
{% endfor %}
```