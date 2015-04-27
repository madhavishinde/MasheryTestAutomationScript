#Builds OAuth2 client and send HTTP requests
from requests_oauthlib import OAuth2Session
#For converting string to dictionary
import ast
#For json operation
import json
#For handling exceptions
import sys
#To disable warnings
import requests

class Api:
	
	#'Common base class for all apis'
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
	#Id of specific API
	general_id = ""	
	#URL of specific API
	url_path = ""
	#Upload_id of image uploaded
	upload_id = ""
	#Data to be send with post request
	payload = {}

	def fetch_token_operation(self):

		###############################
		#NAME OF MODULE : fetch_token_operation
		#DESCRIPTION : This module does OAuth authentication 
		#and gives access token required to process REST APIs of Rubicon
		#INPUT/OUTPUT : Input is nothing and Output is Access token
		###############################

		print '\n-----------------Authentication step-----------------\n'
		#To disable verification of HTTPS requests
		requests.packages.urllib3.disable_warnings()
		mashery = OAuth2Session(Api.client_id, redirect_uri=Api.redirect_uri)
		authorization_url, state = mashery.authorization_url(Api.authorization_base_url)
		#Conversion between http and https is required because OAuth2.0 support only
		#SSL connections (https) and Application uses http connection 
		authorization_url = authorization_url.replace("https", "http", 1)
		print '\nPlease open this URL in browser and authorize,', authorization_url
		redirect_response = raw_input('\nCopy the full redirect URL here:')
		redirect_response = redirect_response.replace("http", "https", 1)
		tokenStr = str(mashery.fetch_token(Api.token_url, client_secret=Api.client_secret,authorization_response=redirect_response, verify=False))
		#print "\n\nAccess token information :" + tokenStr + "\n\n"
		tokenStr = ast.literal_eval(tokenStr)
 		return tokenStr.get('access_token')

	def list_operation(self):

		###############################
                #NAME OF MODULE : list_operation
                #DESCRIPTION : This module gives list of entities
		#specific to particular API
                #INPUT/OUTPUT : Input is nothing and Output is List of entities
                ###############################
	
		print '\n-----------------List endpoint-----------------\n'
		requests.packages.urllib3.disable_warnings()
		headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
		try:
			response = requests.get('https://api.dspbuilder.rubiconproject.com/%s' %Api.url_path, verify=False, headers=headers)
			status_code = response.status_code
	        	print "\nStatus_code for response is %s" %status_code
			print response.text
			response.raise_for_status()
	        except requests.HTTPError, e:
        	        print 'HTTP ERROR occured'
                	print e

	def show_operation(self):

		###############################
                #NAME OF MODULE : show_operation
                #DESCRIPTION : This module gives Details of entity
                #specific to particular API
                #INPUT/OUTPUT : Input is nothing and Output is Details of specific entity of specific API
                ###############################

		print '\n-----------------Show endpoint-----------------\n'
	        requests.packages.urllib3.disable_warnings()
        	headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
		try:
			if not Api.general_id:
	                        print "No id found.\nplease first execute Create endpoint function to generate its id.\n"
				#exit(0)
			else:
				response = requests.get('https://api.dspbuilder.rubiconproject.com/%s/%s' %(Api.url_path, Api.general_id), verify=False, headers=headers)
				status_code = response.status_code
				print "\nStatus_code for response is %s" %status_code
				print response.text
				response.raise_for_status()
		except requests.HTTPError, e:
			print 'HTTP ERROR occured'
			print e


	def upload_file_operation(self, json_file_name, image_file_name):

		###############################
                #NAME OF MODULE : upload_file_operation
                #DESCRIPTION : This module uploads json file and image file to database
                #INPUT/OUTPUT : Input is json file and image file and Output is upload id of uploaded file
                ###############################

        	print '\n-----------------Upload File endpoint-----------------\n'
	        requests.packages.urllib3.disable_warnings()
        	headers = {'Accept': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
		files = {'file': open(json_file_name, 'rb'), 'file': open(image_file_name, 'rb')}
        	try:
                	response = requests.post('https://api.dspbuilder.rubiconproject.com/api/v1/uploadfile', verify=False, headers=headers, files=files)
	                status_code = response.status_code
        	        print "\nStatus_code for response is %s" %status_code
			response_str = response.text
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

	def create_operation(self):

		###############################
                #NAME OF MODULE : create_operation
                #DESCRIPTION : This module creates entity for specific API
                #INPUT/OUTPUT : Input is nothing and Output is id of created entity
                ###############################

        	print '\n-----------------Create endpoint-----------------\n'
	        requests.packages.urllib3.disable_warnings()
        	headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
		try:
			if not Api.payload:
                                print "No payload data available to pass to post function\n"
                                #exit(0)
			else:
                		response = requests.post('https://api.dspbuilder.rubiconproject.com/%s' %Api.url_path, verify=False, headers=headers, data=json.dumps(Api.payload))
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


	def update_operation(self):

		###############################
                #NAME OF MODULE : update_operation
                #DESCRIPTION : This module updates entity for specific API
                #INPUT/OUTPUT : Input is nothing and Output is 200 response of updated sucessfully
                ###############################

        	print '\n-----------------Update endpoint-----------------\n'
	        requests.packages.urllib3.disable_warnings()
        	headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
        	try:
			if not Api.general_id:
                                print "No id found.\nplease first execute Create endpoint function to generate its id.\n"
                                #exit(0)
			else:
		                response = requests.put('https://api.dspbuilder.rubiconproject.com/%s/%s' %(Api.url_path, Api.general_id), verify=False, headers=headers, data=json.dumps(Api.payload))
        		        status_code = response.status_code
                		print "\nStatus_code for response is %s" %status_code
	                	print response.text
	        	        response.raise_for_status()
	        except requests.HTTPError, e:
        	        print 'HTTP ERROR occured'
                	print e

	def destroy_operation(self):

		###############################
                #NAME OF MODULE : destroy_operation
                #DESCRIPTION : This module deletes entity for specific API
                #INPUT/OUTPUT : Input is nothing and Output is 200 response of deleted sucessfully
                ###############################
	
        	print '\n-----------------Destroy endpoint-----------------\n'
	        requests.packages.urllib3.disable_warnings()
        	headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
	        try:
			if not Api.general_id:
                                print "No id found to destroy.\nplease first execute Create endpoint function to generate id.\n"
                                #exit(0)
        		else:
			        response = requests.delete('https://api.dspbuilder.rubiconproject.com/%s/%s' %(Api.url_path, Api.general_id), verify=False, headers=headers)
        	        	status_code = response.status_code
	        	        print "\nStatus_code for response is %s" %status_code
        	        	print response.text
				if response.status_code == 204 :
					print "Deleted successfully"
	                	response.raise_for_status()
        	except requests.HTTPError, e:
                	print 'HTTP ERROR occured'
	                print e


class Organization(Api):
	#This is an organization api class which extends Api class.

        def get_budget_operation(self):

		###############################
                #NAME OF MODULE : get_budget_operation
                #DESCRIPTION : This module gives budget details for organization API
                #INPUT/OUTPUT : Input is nothing and Output is details of budget
                ###############################

                print '\n-----------------Get Budget endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
                try:
                        response = requests.get('https://api.dspbuilder.rubiconproject.com/api/v1/organizations/budget', verify=False, headers=headers)
                        status_code = response.status_code
                        print "\nStatus_code for response is %s" %status_code
                        print response.text
                        response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR occured'
                        print e

        def add_budget_operation(self):

		###############################
                #NAME OF MODULE : add_budget_operation
                #DESCRIPTION : This module adds budget for organization API
                #INPUT/OUTPUT : Input is nothing and Output is 200 response of budget added sucessfully
                ###############################

                print '\n-----------------Add Budget endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
                try:
			if not Api.payload:
                                print "No payload data available to pass to post function\n"
                                #exit(0)
			else:
	                        response = requests.post('https://api.dspbuilder.rubiconproject.com/api/v1/organizations/budget', verify=False, headers=headers, data=json.dumps(Api.payload))
        	                status_code = response.status_code
                	        print "\nStatus_code for response is %s" %status_code
                        	print response.text
	                        response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR occured'
                        print e


if __name__ == '__main__':

	org_api = Organization()
	Api.url_path = "api/v1/organizations"	
	json_file_name = "/home/ubuntu/Mashery/jsonData.txt"
	image_file_name = "/home/ubuntu/Mashery/new2.png"
	budget_value = 59
	Api.token = org_api.fetch_token_operation()
	#Api.token = u'5wz42cujan5tb6wc87ndgrtg'
	org_api.list_operation()
	Api.upload_id = org_api.upload_file_operation(json_file_name, image_file_name)
	#Api.upload_id = "553ddfed70726f725d1e0000"
	Api.payload = {"organization": {"name": "New organization1", "url": "www.test1.com", "upload_id": "%s" %Api.upload_id }}	
	Api.general_id = org_api.create_operation()
	Api.payload = {"organization": {"name": "Rename organization1", "url": "www.test1.com", "upload_id": "%s" %Api.upload_id }}
	org_api.update_operation()
	org_api.show_operation()
	org_api.destroy_operation()
	org_api.get_budget_operation()
	payload = {"budget" : budget_value}
	org_api.add_budget_operation()
