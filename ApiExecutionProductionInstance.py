#Builds OAuth2 client and send HTTP requests
from requests_oauthlib import OAuth2Session
#
#from StringIO import StringIO
#For converting string to dictionary
import ast
#For json operation
import json

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


def fetch_token():

	print '\n-----------------Authentication step-----------------\n'
	#To disable verification of HTTPS requests
	requests.packages.urllib3.disable_warnings()
	mashery = OAuth2Session(client_id, redirect_uri=redirect_uri)
	authorization_url, state = mashery.authorization_url(authorization_base_url)
	#Conversion between http and https is required because OAuth2.0 support only
	#SSL connections (https) and Application uses http connection 
	authorization_url = authorization_url.replace("https", "http", 1)
	print 'Please open this URL in browser and authorize,', authorization_url
	redirect_response = raw_input('Copy the full redirect URL here:')
	redirect_response = redirect_response.replace("http", "https", 1)
	tokenStr = str(mashery.fetch_token(token_url, client_secret=client_secret,authorization_response=redirect_response, verify=False))
	print "\n\nAccess token information :" + tokenStr + "\n\n"
	tokenStr = ast.literal_eval(tokenStr)
 	return tokenStr.get('access_token')

def list_opr(token):

	print '\n-----------------List endpoint-----------------\n'
	requests.packages.urllib3.disable_warnings()
	headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %token}
	try:
		response = requests.get('https://api.dspbuilder.rubiconproject.com/api/v1/organizations', verify=False, headers=headers)
		status_code = response.status_code
        	print "\nStatus_code for response is %s" %status_code
		print response.text
		response.raise_for_status()
        except requests.HTTPError, e:
                print 'HTTP ERROR occured'
                print e

def show_opr(token, general_id):

	print '\n-----------------Show endpoint-----------------\n'
        requests.packages.urllib3.disable_warnings()
        headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %token}
	try:
		response = requests.get('https://api.dspbuilder.rubiconproject.com/api/v1/organizations/%s' %general_id, verify=False, headers=headers)
		status_code = response.status_code
		print "\nStatus_code for response is %s" %status_code
		print response.text
		response.raise_for_status()
	except requests.HTTPError, e:
		print 'HTTP ERROR occured'
		print e

def get_budget_opr(token):

	print '\n-----------------Get Budget endpoint-----------------\n'
        requests.packages.urllib3.disable_warnings()
        headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %token}
        try:
                response = requests.get('https://api.dspbuilder.rubiconproject.com/api/v1/organizations/budget', verify=False, headers=headers)
                status_code = response.status_code
                print "\nStatus_code for response is %s" %status_code
                print response.text
                response.raise_for_status()
        except requests.HTTPError, e:
                print 'HTTP ERROR occured'
                print e

def upload_file_opr(token):

        print '\n-----------------Upload File endpoint-----------------\n'
        requests.packages.urllib3.disable_warnings()
        headers = {'Accept': 'application/json', 'Authorization': 'Bearer %s' %token}
	files = {'file': open('/home/ubuntu/Mashery/jsonData2.txt', 'rb'), 'file': open('/home/ubuntu/Mashery/new2.png', 'rb')}
        try:
                response = requests.post('https://api.dspbuilder.rubiconproject.com/api/v1/uploadfile', verify=False, headers=headers, files=files)
                status_code = response.status_code
                print "\nStatus_code for response is %s" %status_code
		response_str = response.text
		#print r.json()
                print response_str
		if response.status_code == requests.codes.ok :
			response_str = str(response.text)
			response_str = ast.literal_eval(response_str)
			return response_str.get('id')
                response.raise_for_status()
        except requests.HTTPError, e:
                print 'HTTP ERROR occured'
                print e
	#finally:
		#return response.get('id')

def create_opr(token, upload_id):

        print '\n-----------------Create endpoint-----------------\n'
        requests.packages.urllib3.disable_warnings()
        headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %token}
        payload = {"organization": {"name": "New organization1", "url": "www.test1.com", "upload_id": "%s" %upload_id }}
	try:
                response = requests.post('https://api.dspbuilder.rubiconproject.com/api/v1/organizations', verify=False, headers=headers, data=json.dumps(payload))
                status_code = response.status_code
                print "\nStatus_code for response is %s" %status_code
                print response.text
		if response.status_code == requests.codes.ok :
                        response_str = str(response.text)
                        response_str = ast.literal_eval(response_str)
                        return response_str.get('id')
                response.raise_for_status()
        except requests.HTTPError, e:
                print 'HTTP ERROR occured'
                print e


def update_opr(token, general_id, upload_id):

        print '\n-----------------Update endpoint-----------------\n'
        requests.packages.urllib3.disable_warnings()
        headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %token}
        payload = {"organization": {"name": "Rename organization1", "url": "www.test1.com", "upload_id": "%s" %upload_id }}
        try:
                response = requests.put('https://api.dspbuilder.rubiconproject.com/api/v1/organizations/%s' %general_id, verify=False, headers=headers, data=json.dumps(payload))
                status_code = response.status_code
                print "\nStatus_code for response is %s" %status_code
                print response.text
                response.raise_for_status()
        except requests.HTTPError, e:
                print 'HTTP ERROR occured'
                print e

def destroy_opr(token, general_id):

        print '\n-----------------Destroy endpoint-----------------\n'
        requests.packages.urllib3.disable_warnings()
        headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %token}
        try:
                response = requests.delete('https://api.dspbuilder.rubiconproject.com/api/v1/organizations/%s' %general_id, verify=False, headers=headers)
                status_code = response.status_code
                print "\nStatus_code for response is %s" %status_code
                print response.text
		if response.status_code == 204 :
			print "Deleted successfully"
                response.raise_for_status()
        except requests.HTTPError, e:
                print 'HTTP ERROR occured'
                print e

def add_budget_opr(token, budget_value):

        print '\n-----------------Add Budget endpoint-----------------\n'
        requests.packages.urllib3.disable_warnings()
        headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %token}
        payload = {"budget" : budget_value}
        print payload, type(payload)
        try:
                response = requests.post('https://api.dspbuilder.rubiconproject.com/api/v1/organizations/budget', verify=False, headers=headers, data=json.dumps(payload))
                status_code = response.status_code
                print "\nStatus_code for response is %s" %status_code
                print response.text
                response.raise_for_status()
        except requests.HTTPError, e:
                print 'HTTP ERROR occured'
                print e


def organization_api():
	
	token = u'5wz42cujan5tb6wc87ndgrtg'
        general_id = '552f02746f642d2fd2020000'
        upload_id = '5538b9bb70726f725d160000'
        budget_value = 55
        print '-----------------Organization API endpoint-----------------'
        try:
		#token = fetch_token()
	        #upload_id = upload_file_opr(token)
        	#general_id = create_opr(token, upload_id)
	        show_opr(token, general_id)
        	#update_opr(token, general_id, upload_id)
	        get_budget_opr(token)
        	#add_budget_opr(token, budget_value)
	        list_opr(token)
        	#destroy_opr(token, general_id)
        except :
                print "Unexpected error:", sys.exc_info()[0]
                print e


if __name__ == '__main__':

	organization_api()


