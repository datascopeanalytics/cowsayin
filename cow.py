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

def default():
    return r"""<!doctype html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang=""> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8" lang=""> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9" lang=""> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang=""> <!--<![endif]-->
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- page metadata -->
    <title>Moo</title>
    <meta name="description" content="Cows say moo.">

    <!-- steez -->
    <link href='http://fonts.googleapis.com/css?family=Anonymous+Pro:700' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">

    <!-- browser compatibility -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>

    <style>
      pre {
        background: white;
        font-family: 'Anonymous Pro', monospace;
        font-size: 14px;
        color: #444;
        border: 0;
      }
    </style>
  </head>
  <body>
    <!--[if lt IE 8]>
        <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->

    <div class="container">
      <pre> ______ 
< Moo. >
 ------ 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
      </pre>    
    </div>

  </body>
</html>
    """
