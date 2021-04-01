from O365 import Account
import os

client_id = os.environ.get('CLIENT_ID')

client_secret = os.environ.get('CLIENT_SECRET')

credentials = (client_id, client_secret)
account = Account(credentials)
account.authenticate(scopes=['basic', 'message_all'])


