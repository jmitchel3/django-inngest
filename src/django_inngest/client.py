import logging

import inngest
from django.conf import settings

# Create an Inngest client

INNGEST_EVENT_KEY = settings.INNGEST_EVENT_KEY
INNGEST_SIGNING_KEY = settings.INNGEST_SIGNING_KEY

default_config = {
    "is_production": settings.INNGEST_IS_PRODUCTION,
}

# Only add event_key and signing_key in production
if settings.INNGEST_IS_PRODUCTION:
    if INNGEST_EVENT_KEY:
        default_config["event_key"] = INNGEST_EVENT_KEY
    if INNGEST_SIGNING_KEY:
        default_config["signing_key"] = INNGEST_SIGNING_KEY


inngest_client = inngest.Inngest(
    app_id="chapterkit", logger=logging.getLogger("gunicorn"), **default_config
)


# signing_key_fallback=settings.INNGEST_SIGNING_KEY_FALLBACK,
