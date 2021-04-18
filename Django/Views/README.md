# Views
- path = App/views.py
- App안에 들어있는 Templates(HTML)이 언제 어떻게 처리될지 알려주는 함수를 작성하는 곳

## request
```python
from django.shortcuts import render

def index(request):
    return render (request, './html/index.html')
```

## 회원가인, 로그인, 로그아웃
- Views.py
```python
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

# 회원 가입
def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST['password'] == request.POST['confirm']:
            # user 객체를 새로 생성
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, './html/signup.html')

# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, '/html/login.html', {'error' : 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, './html/login.html')

# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, './html/login.html')
```
- HTML
```html
<body>
    <!-- 요청방식을 POST로 지정해준다 -->
    <form method="POST" action="{% url 'login' %}">
        <!-- 보안 -->
        {% csrf_token %}
        <p>username</p>
        <input type="text" name="username">
        <br>
        <p>password</p>
        <input type="text" name="password">
        <br>
        <input type="submit" value="로그인">
    </form>
</body>
```

## Pagination
- 1. 무슨 객체를 한페이지당 몇개씩? : Paginator(object, num)
- 2. 내가 원하는 페이지 가져오기 : PaginatorObject.get_page(가지고 오고싶은 페이지 번호)
- 3. 가지고온 페이지 html에 띄우기 : 페이지객체 메소드 함수 + template 언어

### Paginator Class VS Page Class
- Class Paginator(object_list, per_page, orphans = 0, allow_empty_first_page = True)
- Class Page(object_list, number, paginator)
- page 객체 메소드 함수
    - page.count() : 총 객체 수
    - page_num_pages() : 총 페이지 갯수
    - page.page(n) : n번째 페이지 return
    - page.page_range() : 페이지 리스트 반환
- Request받은 페이지 번호
    - page = request.GET.get('page')
- 실제 page 가져오기
    - paginator.get_page(page)

### Paginator Views.py
```python
from django.core.paginator import Paginator
from .model import Blog

def home(request):
    # 블로그의 모든 글을 가져온다
    blog_list = Blog.objects.all()
    # 블로그 객체 3개를 한 패이지로 자른다
    paginator = Paginator(blog_list, 3)
    # request된 페이지가 무엇인지 알아낸다
    page = request.GET.get('page')
    # request된 페이지를 알아낸뒤 return한다.
    posts = paginator.get_page(page)
    
    return render(request, 'home.html' {'posts' : posts})
```
### Paginator HTML
```html
<!-- 정해진 갯수만큼 게시물 출력 -->
{% for i in posts %}
    <h2>i.title</h2>
{% endfor %}

<!-- First Previous 3 of 4 Next Last -->
{% if posts.has_previous %}
<a herf = "?page=1">First</a>
<a herf = "?page={{posts.previous_page_number}}">Previous</a>
{% endif %}

<span>{{posts.number}}</span>
<span>of</span>
<span>{{posts.paginator.num_pages}}</span>

{% if posts.has_next %}
<a herf = "?page={{posts.next_page_number}}">Next</a>
<a herf = "?page={{posts.paginator.num_pages}}">Last</a>
{% endif %}
```