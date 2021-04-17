# Views
- path = App/views.py
- App안에 들어있는 Templates(HTML)이 언제 어떻게 처리될지 알려주는 함수를 작성하는 곳

## request
```python
from django.shortcuts import render

def index(request):
    return render (request, './html/index.html')
```