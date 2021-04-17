# Django
![Django](./Django/Image/Django_Framework.png)

# 구성
- [Views - HTML이 어떻게 작용할지 입력하는 함수](./Django/Views/README.md)
- [URL - 특정 URL 입력시 HTML 연결](./Django/Urls/README.md)
- [Setting](./Django/Setting/README.md)
- [Models](./Django/Models/README.md)

## Project 시작
- Project 만들기
    - django-admin startproject <project Name>
- Server 실행
    - python3 manage.py runserver <port Num>
- App 만들기
    - python3 manage.py startapp <app Name>
- DB
    - python3 manage.py migrate
    - python3 manage.py makemigrations <app Name>


## 가상환경 vevn
- 가상환경 설치
```cmd
python3 -m vevn <vevn_name>
```
- 가상환경 실행
```cmd
source activate <vevn_name>
```
- 가상환경 종료
```cmd
deactivate
```

## Project의 구성
- Project
    - __pycache__
    - __init__.py
    - wsgi.py
    - setting.py
    - url.py

## APP(Project 구성 단위)의 구성
- APP
    - migration
    - templates (직접생성)
    - __init__.py
    - admin.py
    - apps.py
    - models.py
    - test.py
    - views.py

## 템플릿 언어
- Django에서 HTML문법 안에서 Python코드가 돌아갈 수 있게 해주는 문법
- 템플릿 변수
    - {{ Python-Variable }} : Python_Variable을 HTML화면에 출력해라
- 템플릿 필터
    - {{ Python-Variable | filter }}
    - Ex. {{ Value | length }} : Value의 길이 반환
    - Ex. {{ Value | lower }} : Value를 소문자로 출력
- 템플릿 태그
    - HTML상 Python문법 사용, URL생성 등의 기능 제공
    - {% tag %} ... tag 내용 ... {% endtag %}
- EX_1
```python
# Python File
Aclass = ["a", "b", "c"]

# HTML FIle
num = {{ class | length }}
{% for i in class %}
    {{i}}
{{% endfor %}}
```
- EX_2
```python
{% url 'url_name'%}
```