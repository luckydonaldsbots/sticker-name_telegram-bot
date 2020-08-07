# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
from luckydonaldUtils.interactions import string_is_yes
import os


__author__ = 'luckydonald'
logger = logging.getLogger(__name__)

# # CELERY WORKER # #

IS_WORKER = string_is_yes(os.getenv('IS_WORKER', 'yes'))


RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', None)
assert RABBITMQ_HOST is not None  # $RABBITMQ_HOST environment variable

RABBITMQ_USER = os.getenv('RABBITMQ_USER', None)
assert RABBITMQ_USER is not None  # $RABBITMQ_USER environment variable

RABBITMQ_PASS = os.getenv('RABBITMQ_PASS', None)
assert RABBITMQ_PASS is not None  # $RABBITMQ_PASS environment variable

RABBITMQ_VHOST = os.getenv('RABBITMQ_VHOST', None)
assert RABBITMQ_VHOST is not None  # $RABBITMQ_VHOST environment variable

# # BOT SETTINGS # #
TG_API_KEY = os.getenv('TG_API_KEY', None)
assert(TG_API_KEY is not None)  # TG_TG_API_KEY environment variable

TG_FEED_CHANNEL_ID = os.getenv('TG_FEED_CHANNEL_ID', None)
assert TG_FEED_CHANNEL_ID is not None  # TG_FEED_CHANNEL_ID environment variable
TG_FEED_CHANNEL_ID = int(TG_FEED_CHANNEL_ID)


# # WEBHOOK SETTINGS # #

HOSTNAME = os.getenv('URL_HOSTNAME', None)
# can be None

URL_PATH = os.getenv('URL_PATH', None)
assert(URL_PATH is not None)  # URL_PATH environment variable

# # IMGUR API # #

IMGUR_CLIENT_ID = os.getenv('IMGUR_CLIENT_ID', None)
assert(IMGUR_CLIENT_ID is not None)  # IMGUR_CLIENT_ID environment variable

IMGUR_CLIENT_SECRET = os.getenv('IMGUR_CLIENT_SECRET', None)
assert(IMGUR_CLIENT_SECRET is not None)  # IMGUR_CLIENT_SECRET environment variable


# # REDDIT API # #

REDDIT_APP_PLATFORM = os.getenv('REDDIT_APP_PLATFORM', None)
assert(REDDIT_APP_PLATFORM is not None)  # REDDIT_APP_PLATFORM environment variable

REDDIT_APP_NAME = os.getenv('REDDIT_APP_NAME', None)
assert(REDDIT_APP_NAME is not None)  # REDDIT_APP_NAME environment variable

REDDIT_APP_CREATOR_USERNAME = os.getenv('REDDIT_APP_CREATOR_USERNAME', None)
assert(REDDIT_APP_CREATOR_USERNAME is not None)  # REDDIT_APP_CREATOR_USERNAME environment variable

REDDIT_APP_CLIENT_ID = os.getenv('REDDIT_APP_CLIENT_ID', None)
assert(REDDIT_APP_CLIENT_ID is not None)  # REDDIT_APP_CLIENT_ID environment variable

REDDIT_APP_CLIENT_SECRET = os.getenv('REDDIT_APP_CLIENT_SECRET', None)
assert(REDDIT_APP_CLIENT_SECRET is not None)  # REDDIT_APP_CLIENT_SECRET environment variable

REDDIT_ACCOUNT_NAME = os.getenv('REDDIT_ACCOUNT_NAME', None)
assert(REDDIT_ACCOUNT_NAME is not None)  # REDDIT_ACCOUNT_NAME environment variable

REDDIT_ACCOUNT_PASSWORD = os.getenv('REDDIT_ACCOUNT_PASSWORD', None)
assert(REDDIT_ACCOUNT_PASSWORD is not None)  # REDDIT_ACCOUNT_PASSWORD environment variable


# # S3 STORAGE # #

S3_HOST = os.getenv('S3_HOST', None)
assert S3_HOST is not None  # $S3_HOST environment variable

S3_PORT = os.getenv('S3_PORT', None)
assert S3_PORT is not None  # $S3_PORT environment variable

S3_BUCKET = os.getenv('S3_BUCKET', None)
assert S3_BUCKET is not None  # $S3_BUCKET environment variable

S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY', None)
assert S3_ACCESS_KEY is not None  # $S3_ACCESS_KEY environment variable

S3_SECRET_KEY = os.getenv('S3_SECRET_KEY', None)
assert S3_SECRET_KEY is not None  # $S3_SECRET_KEY environment variable

SENTRY_DSN = os.getenv('SENTRY_DSN', None)
# is optional
