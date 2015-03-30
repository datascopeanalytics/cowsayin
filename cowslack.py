"""Main file with Flask app for the cowsay/slack integration.

"""
from flask import Flask
from flask import request, render_template

import settings
import cow

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def moo():
    """Handles POST request from slack integration. GET request just
    returns a cow saying moo.

    """
    # render the moo template for GET request
    if request.method == 'GET':
        return render_template(
            'moo.html',
            text=cow.cow.milk_random_cow('Moo.'),
        )

    # do slack stuff on POST request
    else:
        # get values (or None) from POST
        text = request.form.get('text')
        channel = request.form.get('channel_id')
        user = request.form.get('user_name')

        # if --help is given, have slackbot return a help message (and
        # don't post anything to room)
        if text.strip().startswith('--help'):
            return cow.help_text()

        # use webhook to post message to room and return empty string
        # so that slackbot doesn't say anything
        else:
            return cow.post(text, channel=channel, username=user)

if __name__ == "__main__":
    app.run(debug=settings.DEBUG)
