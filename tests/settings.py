"""
Django settings for testing django-inngest.
"""

from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "test-secret-key-for-django-inngest"

DEBUG = True

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

USE_TZ = True

# Django Inngest Configuration
DJANGO_INNGEST_APP_ID = "test-django-app"
DJANGO_INNGEST_IS_PRODUCTION = False
INNGEST_EVENT_KEY = None
INNGEST_SIGNING_KEY = None
INNGEST_IS_PRODUCTION = False
DJANGO_INNGEST_CLIENT_LOGGER = None
DJANGO_INNGEST_AUTO_DISCOVER_FUNCTIONS = True
DJANGO_INNGEST_INACTIVE_FUNCTION_IDS = []
