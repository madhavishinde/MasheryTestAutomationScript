from requests import session
from requests_oauthlib import OAuth2Session
import requests
import Credentials

payload = {
    'action': 'login',
    'username': 'mchowla@rubiconproject.com',
    'password': 'Mike2015!'
}
"""
with session() as c:
	token = u""
        #Application's clientID required for OAuth2.0 authentication
        client_id='zfupgaj4k7ashk2wx635zptm'
        #Application's clientSecret required for OAuth2.0 authentication
        client_secret='MAQb9HGK67Y2DevGVMNssTTx'
        #Application's Authorization URL required for OAuth2.0 authentication
        authorization_base_url = 'https://dspbuilder.rubiconproject.com/login'
        #Application's token URL required for OAuth2.0 authentication
        token_url = 'https://api.dspbuilder.rubiconproject.com/accesstoken'
        #Application's Redirect URL required for OAuth2.0 authentication
        redirect_uri = 'http://rubiconproject.mashery.com/io-docs/oauth2callback'

	print '\n-----------------Authentication step-----------------\n'
        #To disable verification of HTTPS requests
        requests.packages.urllib3.disable_warnings()
        mashery = OAuth2Session(client_id, redirect_uri=redirect_uri)
        authorization_url, state = mashery.authorization_url(authorization_base_url)
        #Conversion between http and https is required because OAuth2.0 support only
        #SSL connections (https) and Application uses http connection
 	authorization_url = authorization_url.replace("https", "http", 1)
        print '\nAuthorize URL : ', authorization_url

	response = c.post(authorization_url, data=payload)
    	response = c.get('http://dspbuilder.rubiconproject.com/switch-organization')
    	print(response.headers)
	print response.status_code    
	print(response.text)

"""

print "1" + Credentials.client_id + "2"
