# Setups
## Install Django
`> python3 -m pip install django`

## Check Available Tasks
`> django-admin`

## Setup Django Project
`> django-admin startproject [폴더명] [디렉토리]`<br>
ex) django-admin startproject myproject .

## How to run
    - to check for available tasks
        > python3 manage.py
    - run server (default port = 8000)
        > python3 manage.py runserver
    - to run server with different port
        > python3 manage.py runserver [port_number]

## Setup Django App
`> django-admin startapp [폴더명]`<br>

<br>

# Django Structure
![django structure](images/structure.png)
- Routing : Client Request -> project route -> app route -> app view -> (처리) -> Client Response (HttpResponse)

<br><br>
※ 더 공부할 것
- db 연동
- Django Model
- 웹 보안 (security)
- Template Engine - 파이썬 코드와 html 코드를 분리하기 위해