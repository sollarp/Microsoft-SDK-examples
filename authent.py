from O365 import Account

client_id = os.environ.get('CLIENT_ID')

client_secret = os.environ.get('CLIENT_SECRET')

credentials = (client_id, client_secret)

# the default protocol will be Microsoft Graph

account = Account(credentials, auth_flow_type='credentials', tenant_id='tenant_id')
if account.authenticate():
   print('Authenticated!')