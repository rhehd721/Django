# Django
![Django](./Django/Image/Django_Framework.png)

# 구성
- [Views](./Django/Views/README.md)
- [URL](./Django/Urls/README.md)
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
