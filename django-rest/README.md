# Django proj

## Description

本專案會依據前一個專案，使用 django rest framework 來實作 restful api

[官網範例](https://docs.djangoproject.com/en/3.2/intro/overview/)

## Getting Start

```bash
# install django, drf, drf-yasg
$ pip3 install django djangorestframework drf-yasg

# for CORS
$ pip3 install django-cors-headers
```

* `setting.py`
```python
...
ALLOWED_HOSTS = [*]

INSTALLED_APPS = [
    'app',
    'corsheaders',
    'drf_yasg',
    'rest_framework',
    ...
]
...
```

