"""Utility functions for cowsay/slack integration.

"""
import json

import cowsay
import requests

import settings


def say(text):
    """Return some cowsayed text."""
    return '```%s```\n' % cowsay.cowsay(text)


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
