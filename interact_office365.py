from O365 import Account
import os

client_id = os.environ.get('CLIENT_ID')

client_secret = os.environ.get('CLIENT_SECRET')

credentials = (client_id, client_secret)

account = Account(credentials)

m = account.new_message()
m.to.add('szpitor@gmail.com')
m.subject = 'Test env.'
m.body = "George Best quote: I'vfdgsdfgsdfgle I'm asleep."
m.send()