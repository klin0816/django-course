# Django proj

## Description

本專案將會根據官網經典 Django 架構產生前後端合一的 project，但整體架構再簡化一點

[官網範例](https://docs.djangoproject.com/en/3.2/intro/overview/)

## Getting Start

講 Django 安裝起來, 目前 stable 版本未 3.2

```bash
# install django
$ pip3 install django
```

安裝完後就會將 `django-admin` 這個 Django 的 CLI 給安裝起來，官方的開啟專案流程為使用這個 CLI 將專案給啟動，但我不打算這麼做，我的作法會是

```bash
# start project
$ mkdir django-project
$ cd django-project

# create projects and configs
$ django-admin startproject [project_name] [dir]

$ django-admin startproject proj .
```

之後整個資料結構就會長這樣

```
# django-project/
.
├── manage.py
└── proj
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   ├── settings.cpython-36.pyc
    │   └── urls.cpython-36.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

專案的根目錄已經創建好了，接下來就是把我們的應用給加入這個專案

```bash
# django-project/
# django-admin startapp app

.
├── app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── proj

```

到目前為止整個基礎架構就已經設定完了

## Setting

### Project Basic Setting

首先要先對 `proj` 做一些設定，把 `app` 加入 `proj` 的設定中

```python
# proj/setting.py
...
INSTALLED_APPS = [
    'app',
    'django.contrib.admin',
...
```

### Database

Django 專案預設是使用 `sqlite`，但實際上官方可以支援的有：
* PostgreSQL
* MariaDB
* MySQL
* Oracle
* SQLite
[Supported Database](https://docs.djangoproject.com/en/3.2/ref/databases/#databases)

在 `setting.py` 裡面也可以看到相關的設定，若是要改 database 的話也是改這邊就可以了，若不需要更改的話就直接放著不改就可以了。

```python
# proj/setting.py
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
...
```

可是你會發現，其實 `sqlite` 的 db 還不存在，那是因為現在只有將設定做好而已，還沒有將專案和 DB 連結起來，所以這時候必須要先 migrate 資料庫
migrate 這個動作會讓 ORM 直接對 DB 做一些操作，也會將我們設計好的表格都在 DB 給創建好，但在這一步還沒有設計任何表格，所以不會有任何 table 被創建出來

```bash
# /django-project/
$ ./manage.py migrate

.
├── app
├── db.sqlite3
├── manage.py
└── proj

```

`sqlite` 如果不存在就會幫你創建好，但如果是其他 DB 的話就必須先保證資料庫存在。

## Quick Start

既然 DB 和專案設定都處理好了，那就可以可以開始 demo 了

```bash
# django-project/
# runserver, default port 8000
$ ./manage.py runserver [ip:port]
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 28, 2021 - 08:20:09
Django version 3.1, using settings 'proj.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

打開 localhost:8000 就可以看到一個 Django 的預設網頁了

## Start

有以下幾個事情需要做
1. 設計表格，寫入 `app/models.py`，
2. 設定 `app/admin.py`，讓資料可以用後台顯示
3. 創建 `superuser`
4. 寫一個網頁將結果呈現出來
5. 寫 `app/views.py`，可以回傳設計好的網頁
6. 設定 `proj/urls.py`，定讓網頁瀏覽 `[url]/index` 的時候對應的動作
很多吧，一樣一樣來

### Tables

首先是設計表格

```python
# app/models.py

# Create your models here.
class Students(models.Model):
    name = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
```

這是一個名為 `Students` 的 table，裡面只有
1. 存 Text 的 `name` column
2. 存 Integer 的 `age` column

儲存後就要對資料庫做異動

```bash
# /django-project/
$ ./manage.py makemigrations
System check identified some issues:

Migrations for 'app':
  app/migrations/0001_initial.py
    - Create model Students

$ ./manage.py migrate
System check identified some issues:

Operations to perform:
  Apply all migrations: admin, app, auth, contenttypes, sessions
Running migrations:
  Applying app.0001_initial... OK
```

上面的 `makemigrations` 就是根據 `models.py` 產生一個如何更改的菜單，`migrate` 才是根據菜單來製作
例如說客人跟服務生點餐，服務生再把訂單給廚師出菜
在 `/app/migrations/` 裡面的每個檔案都是異動的紀錄，會一直疊加上去。

到這裡你就可以開始新增資料了

```bash
# /django-project/
$ ./manage.py shell
Python 3.6.8 (default, Jul 28 2020, 14:18:35)
[GCC 4.2.1 Compatible Apple LLVM 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

# import Students models
>>> from app.models import Student

# check Students table, should be empty
>>> Students.objects.all()
<QuerySet []>

# create a new Student
>>> student = Students(name="klin", age=26)

# save this new Student
>>> student.save()

# check whether 'klin' is saved
>>> Students.objects.all()
<QuerySet [<Students: klin>]>

# save another Student
>>> student = Students(name="peter", age=26)
>>> student.save()

# filter Student(can get multiple cantidates)
>>> Students.object.filter(age=26)
<QuerySet [<Students: klin>, <Students: peter>]>

# get first Student candidate(get only one)
>>> Students.object.get(name="klin")
<Students: klin>
```

### Admin

為了方便觀察 tables，可以選擇將 models 用 Django 預設的 admin 介面來呈現
首先要將 models 註冊到 admin 介面

```python
# app/admin.py
from django.contrib import admin

from .models import Students

# Register your models here.
admin.site.register(Students)
```

然後要註冊一組 `superuser` 帳號
```bash
# /django-project/
$ ./manage.py createsuperuser
System check identified some issues:
Username (leave blank to use 'klin'): root
Email address:
Password:
Password (again):
Superuser created successfully.
```

這時候將 Django 啟動後訪問 `localhost:8000/admin` 就可以登入 admin 介面了

### Rest of all

剩下的就根據 repo 內的操作吧
我累了...
