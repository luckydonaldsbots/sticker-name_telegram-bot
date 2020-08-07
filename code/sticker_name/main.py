#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from teleflask import Teleflask
from luckydonaldUtils.tg_bots.gitinfo import version_bp, version_tbp
from pytgbot.api_types.receivable.updates import Update, Message
from pytgbot.api_types.receivable.stickers import StickerSet

from .secrets import TG_API_KEY

__author__ = 'luckydonald'


app = Flask(__name__)
app.register_blueprint(version_bp)
bot = Teleflask(TG_API_KEY, app)
bot.register_tblueprint(version_tbp)


@bot.on_message('sticker')
def got_sticker(update: Update, msg: Message):
    pack: StickerSet = bot.bot.get_sticker_set(msg.sticker.set_name)
    return f"t.me/addstickers/{pack.name}\n{pack.title}"
# end def
