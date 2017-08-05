import requests
from functools import partial


class TelegramApi:

    def __init__(self, token):
        self.url = 'https://api.telegram.org/bot{}/'.format(token)
        self.session = requests.Session()

    def __getattr__(self, name):
        method = self.snake_to_camel(name)
        return partial(self.call, method)

    def call(self, method, **params):
        response = self.session.get(self.url + method, params=params)
        response.raise_for_status()
        return response.json()

    def snake_to_camel(self, text):
        words = text.split('_')
        return words[0] + ''.join([w.title() for w in words[1:]])
