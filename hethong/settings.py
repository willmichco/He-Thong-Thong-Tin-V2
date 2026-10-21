"""Cấu hình Django cho khu quản trị (Đặc tả 3.2, mục 21).

Bản mẫu giao diện chạy bằng dữ liệu minh họa trong mã (quantri/demo.py) nên chưa cần
cơ sở dữ liệu; PostgreSQL, đăng nhập hai lớp và hàng đợi công việc thêm từ Lát 1.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "chi-dung-cho-ban-mau-khong-dung-khi-chay-that")
DEBUG = os.environ.get("DJANGO_DEBUG", "1") == "1"
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,testserver").split(",")

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "quantri",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "quantri.middleware.NoIndexMiddleware",
]

ROOT_URLCONF = "hethong.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "quantri.context.chung",
            ],
        },
    },
]

WSGI_APPLICATION = "hethong.wsgi.application"

DATABASES = {}

LANGUAGE_CODE = "vi"
TIME_ZONE = "Asia/Ho_Chi_Minh"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
