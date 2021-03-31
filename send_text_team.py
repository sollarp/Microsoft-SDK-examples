import pymsteams
import os

ms_webhook_url = os.environ.get('MS_WEBHOOK')

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard(ms_webhook_url)

# Add text to the message.
myTeamsMessage.text("this is my text")

# send the message.
myTeamsMessage.send()

last_status_code = myTeamsMessage.last_http_status.status_code
print(last_status_code)