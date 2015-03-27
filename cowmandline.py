import settings
import cow

# can also use 'http://httpbin.org/post' for testing
url = settings.WEBHOOK_URL

channel = '@mstringer'
user = 'mstringer'
text = 'testing'

print cow.post(text, channel=channel, username=user).text

