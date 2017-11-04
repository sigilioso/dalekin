# -*- coding: utf-8 -*-
import os

BOT_TOKEN = os.environ['BOT_TOKEN']

HOST = os.environ.get('HOST', '0.0.0.0')
PORT = os.environ['PORT']

METHOD_PLACEHOLDER = '{method}'
TELEGRAM_BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/{METHOD_PLACEHOLDER}'

EXTERMINATE_VOICE = os.environ['EXTERMINATE_VOICE_URL']
