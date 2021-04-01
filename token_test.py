import adal
import os

authentication_endpoint = 'https://login.microsoftonline.com/'
resource  = 'https://management.core.windows.net/'
tenant_id = os.environ.get('TENANT_ID')
application_id = os.environ.get('APP_ID')
application_secret = os.environ.get('CLIENT_SECRET')

# get an Azure access token using the adal library
context = adal.AuthenticationContext(authentication_endpoint + tenant_id)
token_response = context.acquire_token_with_client_credentials(resource, application_id, application_secret)

access_token = token_response.get('accessToken')
print(access_token)