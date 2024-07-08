import os

from .settings import *

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ["weitravel.herokuapp.com"]

DEBUG = False

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
