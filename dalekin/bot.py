# -*- coding: utf-8 -*-
import random

from sanic import Sanic
from sanic.response import json

from .config import BOT_TOKEN
from .config import HOST, PORT
from .config import EXTERMINATE_VOICE
from .api import telegram_request


WHAT_SENTENCES = ('qué', 'what', 'cómo')


app = Sanic()
app.config.keep_alive = False


@app.route("/")
async def test(request):
    return json({"DalekinBot status": "Up and running!"})


@app.post('/{}'.format(BOT_TOKEN))
async def webhook(request):
    data = request.json
    if 'message' in data:
        text = data['message'].get('text', '').lower()
        chat_id = data['message']['chat']['id']

        if any(what in text.lower() for what in WHAT_SENTENCES):
            await telegram_request(
                'sendVoice',
                {
                    'chat_id': chat_id,
                    'voice': EXTERMINATE_VOICE,
                    'caption': 'Exterminate!',
                }
            )
        else:
            text = random.choice(('Exterminate!', '*Exterminate!*', '💥 *EXTERMINATE!!!* 💥'))
            await telegram_request(
                'sendMessage',
                {
                    'chat_id': chat_id,
                    'text': text,
                    'parse_mode': 'Markdown'
                }
            )
    return json({}, status=200)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
