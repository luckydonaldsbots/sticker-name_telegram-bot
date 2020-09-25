#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json

from html import escape
from flask import Flask
from teleflask import Teleflask
from teleflask.messages import PlainMessage
from luckydonaldUtils.tg_bots.gitinfo import version_bp, version_tbp
from luckydonaldUtils.tg_bots.peer.user.rights import is_admin
from luckydonaldUtils.logger import logging
from pytgbot.exceptions import TgApiException
from pytgbot.api_types.receivable.updates import Update, Message
from pytgbot.api_types.receivable.stickers import StickerSet
from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup, InlineKeyboardButton

from .secrets import TG_API_KEY, GETSTICKERS_API_KEY, GETSTICKERS_DOMAIN

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


app = Flask(__name__)
app.register_blueprint(version_bp)
bot = Teleflask(TG_API_KEY, app)
bot.register_tblueprint(version_tbp)

LABEL_NSFW = 'NSFW'
LABEL_SFW = 'SFW'
LABEL_DELETE = 'Delete'

CALLBACK_DATA_RATING_PREFIX = "rating_"
CALLBACK_DATA_RATING_SFW = CALLBACK_DATA_RATING_PREFIX + "sfw"
CALLBACK_DATA_RATING_NSFW = CALLBACK_DATA_RATING_PREFIX + "nsfw"
CALLBACK_DATA_DELETE = "action_delete"

REPLACEMENT_TEXT_NSFW = '#nsfw'
REPLACEMENT_TEXT_SFW = '#sfw'

LABEL_TO_TEXT_MAPPING = {
    CALLBACK_DATA_RATING_NSFW: REPLACEMENT_TEXT_NSFW,
    CALLBACK_DATA_RATING_SFW: REPLACEMENT_TEXT_SFW,
}


@bot.on_message('sticker')
def got_sticker(update: Update, msg: Message):
    pack: StickerSet = bot.bot.get_sticker_set(msg.sticker.set_name)
    text = f"t.me/addstickers/{escape(pack.name)}\n{escape(pack.title)}"
    is_nsfw = False

    if GETSTICKERS_API_KEY:
        try:
            requests.put(
                GETSTICKERS_DOMAIN + '/api/v3/submit/sticker',
                params={
                    "key": GETSTICKERS_API_KEY,
                },
                data={
                    "bot_id": bot.user_id,
                    "message": json.dumps(msg.to_array()),
                },
                timeout=1.0
            )
        except requests.HTTPError as e:
            try:
                result = repr(e.response.json())
            except:
                result = e.response.text
            # end try
            logger.warning(f'Submitting sticker to getstickers.me failed with error code {e.response.status_code}: {result}')
        except:
            logger.warning('Submitting sticker to getstickers.me failed.', exc_info=True)
        # end try
        try:

            data = requests.get(
                GETSTICKERS_DOMAIN + '/api/v3/is_nsfw',
                params={
                    "key": GETSTICKERS_API_KEY,
                    "pack": pack.name,
                    # "sticker": msg.sticker.file_unique_id,
                },
                timeout=2.0,
            ).json()
            is_nsfw = data['data']['pack']['pack']['nsfw']
        except requests.HTTPError as e:
            try:
                result = repr(e.response.json())
            except:
                result = e.response.text
            # end try
            logger.warning(f'NSFW check via API failed with error code {e.response.status_code}: {result}')
        except:
            logger.warning('NSFW check via API failed.', exc_info=True)
        # end try
    # end if

    if is_nsfw:
        return PlainMessage(
            text=text + "\n" + REPLACEMENT_TEXT_NSFW
        )
    else:
        return PlainMessage(
            text=text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(LABEL_SFW, callback_data=CALLBACK_DATA_RATING_SFW)],
                [InlineKeyboardButton(LABEL_NSFW, callback_data=CALLBACK_DATA_RATING_NSFW)]
            ]),
        )
    # end if
# end def


@bot.on_update('callback_query')
def process_create_channel_done(update: Update):
    """
    Does the button editing.
    :param update:
    :return:
    """
    new_data = update.callback_query.data
    original_poster = update.callback_query.message.reply_to_message.from_peer
    allowed = True
    if update.callback_query.from_peer.id != original_poster.id:
        allowed = False
        # check for admin if it's not the OP.
        try:
            chat_member = bot.bot.get_chat_member(
                chat_id=update.callback_query.message.chat.id,
                user_id=update.callback_query.from_peer.id,
            )
            allowed = is_admin(chat_member=chat_member, right=None)
        except TgApiException:
            logger.warning('Failed to get chat membership.', exc_info=True)
        # end try
    # end if

    if not allowed:
        try:
            bot.bot.answer_callback_query(
                callback_query_id=update.callback_query.id,
                text="Only the original poster or an admin can do that.",
                show_alert=True,
            )
        except TgApiException:
            logger.warning('Failed to answer callback query with .', exc_info=True)
        # end try
        return
    # end if

    if new_data in (CALLBACK_DATA_RATING_NSFW, CALLBACK_DATA_RATING_SFW):
        try:
            bot.bot.edit_message_text(
                text=update.callback_query.message.text + "\n" + LABEL_TO_TEXT_MAPPING[new_data],
                chat_id=update.callback_query.message.chat.id,
                message_id=update.callback_query.message.message_id,
                reply_markup=None,
            )
            return
        except TgApiException:
            logger.warning('Failed to edit the message', exc_info=True)
        # end try
    elif new_data == CALLBACK_DATA_DELETE:
        try:
            bot.bot.delete_message(
                chat_id=update.callback_query.message.chat.id,
                message_id=update.callback_query.message.message_id,
            )
            return
        except TgApiException:
            logger.warning('Failed to delete the message.', exc_info=True)
        # end try
    else:
        try:
            bot.bot.answer_callback_query(
                callback_query_id=update.callback_query.id,
                text="Unrecognized button.",
                show_alert=True,
            )
            return
        except TgApiException:
            logger.warning('Failed to answer callback query telling about unknown button.', exc_info=True)
        # end try
    # end if
    try:
        bot.bot.answer_callback_query(
            callback_query_id=update.callback_query.id,
            text="The action could not be completed.",
            show_alert=True,
        )
    except TgApiException:
        logger.warning('Failed to answer callback query with fail message.', exc_info=True)
    # end try
# end def


@bot.on_command('start')
@bot.on_command('help')
def got_sticker(update: Update, text: str):
    return f"Thanks for using @{bot.username}.\nSimply add this to any chat you like, it will reply to a sent sticker with the title of the pack and a link.\n\nPart of the @luckydonaldsbots network."
# end def
