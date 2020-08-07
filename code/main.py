from luckydonaldUtils.logger import logging
logging.add_colored_handler(level=logging.DEBUG)

from sticker_name.secrets import SENTRY_DSN

if SENTRY_DSN:
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration
    from luckydonaldUtils.tg_bots.gitinfo import VERSION_STR

    sentry_sdk.init(SENTRY_DSN, integrations=[FlaskIntegration()], release=VERSION_STR)
    logging.getLogger(__name__).success(f'Start with version {VERSION_STR}.')
# end def

from sticker_name.main import app
