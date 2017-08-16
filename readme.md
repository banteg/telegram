# telegram

Minimal [telegram api](https://core.telegram.org/bots/api) wrapper

## Installation
```
pip install tgb
```

## Usage
```python
>>> from telegram import TelegramApi
>>> tg = TelegramApi('your bot token')
>>> tg.send_message(chat_id=123, text='hi')  # note snake_case
```
## Webhooks
Example based on Flask
```python
from telegram import TelegramApi
from flask import Flask, request, jsonify

tg = TelegramApi('your bot token')
app = Flask(__name__)
certificate = open('/path/to/your/certificate.crt', 'rb')

tg.delete_webhook()
tg.set_webhook(url='https://yourdomain/bot_token',
               files={'certificate': certificate})	# used for self-signed certificates


@app.route(settings.WEBHOOK_URL, methods=['GET', 'POST'])
def webhook():
    message = request.json.get('message', {})
    chat_id = message.get('chat', {}).get('id')
    message_id = message.get('message_id')
    message_text = message.get('text', 'Hello!')

    return jsonify(method='sendMessage', chat_id=chat_id,
                   text=message_text, reply_to_message_id=message_id)

```
