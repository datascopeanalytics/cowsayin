import sys

from flask import Flask
from flask import request

import settings
import cow

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def moo():
    if request.method == 'GET':
        return cow.say("Moo")
    else:
        text = request.form.get('text')
        channel = request.form.get('channel_id')
        user = request.form.get('user_name')
        cow.post(text, channel=channel, username=user)
        return ''

if __name__ == "__main__":
    app.run(debug=settings.DEBUG)
