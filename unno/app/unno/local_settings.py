import os
from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "DEBUG_SECRET_KEY",
    "django-insecure-@po6py(s9n$e_8ez!-#71()+xqzn=+$j10@(7r%ew*e%9-!it#",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS.extend(
    [
        "django_extensions",
    ]
)
