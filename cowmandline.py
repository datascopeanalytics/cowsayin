#!/usr/bin/env python
"""Script for testing cowsay/slack integration.
"""
import sys

import settings
import cow

# can also use 'http://httpbin.org/post' for testing
url = settings.WEBHOOK_URL

channel = '@mstringer'
user = 'mstringer'
text = sys.argv[1]

print cow.post(text, channel=channel, username=user)
