import requests
import os
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# ruleid: python-requests-oauth-hardcoded-secret
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

# ok: python-requests-oauth-hardcoded-secret
auth = OAuth1(os.getenv('YOUR_APP_KEY'), os.getenv('YOUR_APP_SECRET'), os.getenv('USER_OAUTH_TOKEN'), os.getenv('USER_OAUTH_TOKEN_SECRET'))

from requests_oauthlib import OAuth2Session

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

client_secret = 'qwe1234567890'
# ruleid: python-requests-oauth-hardcoded-secret
token = oauth.fetch_token(
        'https://accounts.google.com/o/oauth2/token',
        authorization_response=authorization_response,
        client_secret=client_secret)

# ok: python-requests-oauth-hardcoded-secret
token = oauth.fetch_token(
        'https://accounts.google.com/o/oauth2/token',
        authorization_response=authorization_response,
        client_secret=os.env['SECRET'])
