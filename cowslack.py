import sys

from flask import Flask
from flask import request

import cowsay

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def moo():
    if request.method == 'GET':
        return "Moo."
    else:
        text = request.form.get('text', 'Moo.')
        return "```%s```\n" % cowsay.cowsay(text)

if __name__ == "__main__":
    app.run()
