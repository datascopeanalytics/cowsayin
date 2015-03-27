import sys
import json

from flask import Flask
from flask import request
import requests

import settings
import cowsay

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def moo():
    if request.method == 'GET':
        return "Moo.\n"
    else:
        text = request.form.get('text')
        channel = request.form.get('channel_id')
        user = request.form.get('user_name')
        requests.post(
            settings.WEBHOOK_URL,
            data={
                'payload': json.dumps({
                    'channel': channel,
                    'username': user,
                    'text': '```%s```\n' % cowsay.cowsay(text),
                    'icon_emoji': ':cow:',
                }),
            },
        )
        return ''

if __name__ == "__main__":
    app.run(debug=settings.DEBUG)
