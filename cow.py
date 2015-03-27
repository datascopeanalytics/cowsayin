"""Utility functions for cowsay/slack integration.

"""
import json

from cowpy import cow
import requests

import settings


def say(text):
    """Return some cowsayed text."""
    cowacter = cow.Cowacter()
    return '```%s\n\n```' % cowacter.milk(text)


def post(text, url=settings.WEBHOOK_URL, channel=None, username=None):
    """Post the proper request to a url to integrate with slack."""
    payload = {
        'text': say(text),
        'icon_emoji': ':cow:',
    }
    if channel is not None:
        payload['channel'] = channel
    if username is not None:
        payload['username'] = username

    return requests.post(url, data={'payload': json.dumps(payload)})
