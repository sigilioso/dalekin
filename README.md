# Dalekin

Just a toy telegram bot


## How to configure the webhook

```bash
pipenv install --dev

http POST https://api.telegram.org/bot<BOT_TOKEN>/setWebhook url='https://dalekin.herokuapp.com/<BOT_TOKEN>' max_connections=<MAX_CONNECTIONS>
```


## Notes

Convert mp3 to ogg compatible with telegram voice messages:

```bash
ffmpeg -i test.mp3 -ac 1 -map 0:a -codec:a opus -b:a 128k -vbr off -ar 24000 test.ogg
```
