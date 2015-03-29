"""Utility functions for cowsay/slack integration.

"""
import json
import random

from cowpy import cow
import requests

import settings

COW_OPTIONS = set(cow.cow_options())


def say(text, name='default'):
    """Return some cowsayed text."""
    cowacter = cow.get_cow(name)()
    return cowacter.milk(text)


def parse_cowacter(text):
    """Parse out the name from the start only if it's a valid cow name at
    the start of the string with double dashes. Returns (name, text).

    """
    name = 'default'
    text = text.strip()

    # parse out the name from the start only if it's a valid cow name
    # at the start of the string with double dashes
    if text.startswith('--'):
        split = text.split(None, 1)
        if len(split) > 1:
            name_part, text_part = split
            name_part = name_part.strip('-')
            if name_part in COW_OPTIONS:
                name = name_part
                text = text_part
            elif name_part == 'random':
                name = random.choice(list(COW_OPTIONS))
                text = text_part

    return name, text


def post(text, url=settings.WEBHOOK_URL, channel=None, username=None):
    """Post the proper request to a url to integrate with slack."""

    # if it starts with --help, have slackbot return a help message
    # (and don't post anything to room)
    if text.strip().startswith('--help'):
        return help_text()

    # use webhook to post message to room and return empty string
    # so that slackbot doesn't say anything
    else:

        # parse optional cow name from text
        cowacter, text = parse_cowacter(text)

        payload = {
            'text': '```%s\n\n```' % say(text, name=cowacter),
            'icon_emoji': ':cow:',
        }
        if channel is not None:
            payload['channel'] = channel
        if username is not None:
            payload['username'] = username

        requests.post(url, data={'payload': json.dumps(payload)})
        return ''


def help_text():
    return """Moo. I am a cow that says things.

To choose your cowacter, start your message with --{cowacter} where {cowacter} is something from: %s

Or, if you are feeling adventurous, use --random to choose a random cowacter.""" % list(sorted(COW_OPTIONS))
    
