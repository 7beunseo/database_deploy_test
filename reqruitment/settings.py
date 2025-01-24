"""
Django settings for reqruitment project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files root directory for collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-u7dk%*kho+8xaqoz+a)th+=#@)-9efv0-$f=x7ee)fol03im2$"

# 아래 부분은 로컬에서 secret_key.json 읽는 부분입니다. Docker image를 올리고자 할 때에는 아래 부분을 주석처리 해주세요.
secret_file_path = os.path.join(BASE_DIR, 'secret_key.json')

try:
    with open(secret_file_path) as secret_file:
        secrets = json.load(secret_file)
        SECRET_KEY = secrets['SECRET_KEY']
except FileNotFoundError:
    raise Exception("secret_key.json 파일을 찾을 수 없습니다. 프로젝트 루트에 secret_key.json 파일을 생성하세요.")
except KeyError:
    raise Exception("secret_key.json 파일에 'SECRET_KEY' 키가 존재하지 않습니다.")

# 아래 부분은 Docker에서 secret_key.json 읽는 부분입니다. 로컬에서 실행할 때는, 아래 부분을 주석처리 해주세요.
'''
secret_file_path = os.getenv('SECRET_KEY_FILE', '/reqruitment/secret_key.json')

with open(secret_file_path) as secret_file:
    secrets = json.load(secret_file)
    SECRET_KEY = secrets['SECRET_KEY']
'''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    "board",
    "check",
    "qna",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 모든 도메인에서 API 접근 허용 (주의: 개발 단계에서만 사용, 프로덕션에서는 제한적으로 사용하는 것이 좋습니다)
CORS_ALLOW_ALL_ORIGINS = True


ROOT_URLCONF = "reqruitment.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "reqruitment.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'likelion', # DB이름
        'USER': 'admin', # DB 유저 아이디
        'PASSWORD': 'likelion', # 비밀번호
        'HOST': 'localhost', # 또는 자신이 설정한 호스트
        'PORT': '3306', # db가 연결된 포트(여기서는 기본 포트)
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
