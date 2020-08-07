# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
from luckydonaldUtils.interactions import string_is_yes
import os


__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


# # BOT SETTINGS # #

TG_API_KEY = os.getenv('TG_API_KEY', None)
assert(TG_API_KEY is not None)  # TG_TG_API_KEY environment variable

# # WEBHOOK SETTINGS # #

HOSTNAME = os.getenv('URL_HOSTNAME', None)
# can be None

URL_PATH = os.getenv('URL_PATH', None)
assert(URL_PATH is not None)  # URL_PATH environment variable

# # ERROR COLLECTION # #

SENTRY_DSN = os.getenv('SENTRY_DSN', None)
# is optional

# # @StickerTagBot API # #
GETSTICKERS_API_KEY = os.getenv('GETSTICKERS_API_KEY', None)
# is optional
