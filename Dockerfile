# The main container
# FROM luckydonald/telegram-bot:python3.6-stretch-2019-05-04-6ef7dd58f7745e750533139bbde28fe448bbd740
# not using the onbuild (:python3.7-stretch*-onbuild) version as it would always
# run the install after copying the code, thus without caching.
FROM tiangolo/meinheld-gunicorn:python3.7

COPY $FOLDER/requirements.txt   /config/
RUN pip uninstall pytgbot -y ; pip install --no-cache-dir -r /config/requirements.txt
COPY $FOLDER/code /app
