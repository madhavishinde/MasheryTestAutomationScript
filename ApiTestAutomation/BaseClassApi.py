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
#To calculate time required to run program
import time
#to include credentials of oauth2.0
#import ConfigFileProduction
#import ConfigFileStaging
import ConfigFile
#To use login automation function
import seleniumLoginAutomation

#Common base class for all apis

class Api:
	
	#Id of specific API
	#general_id = ""	
	#Id of campaign API
	campaign_id = ""
 	#Id of ad API
        ad_id = ""
	#Id of audience API
	audience_id  = ""
	#Id of organization API
        org_id  = ""
	#Id of adsize API
	adsize_id = ""
	#Id of adtype API
	adtype_id = ""
	#Id of target API
	target_id = ""
	#Id of augmentor API
	aug_id = ""
	#Id of bidder API
	bidder_id = ""
	#Id of user API
	user_id = ""
	#URL of specific API
	url_path = ""
	#Upload_id of image uploaded
	upload_id = ""
	#Data to be send with post request
	payload = {}
	#Base url of APIs
	#base_url = "https://api.dspbuilder.rubiconproject.com"
	#base_url = "https://api-staging.dspbuilder.rubiconproject.com"
	base_url = '' #ConfigFile.base_url
	#Access token
	token = u''
	###############################################################
        #NAME OF MODULE : fetch_token_operation
        #DESCRIPTION    : This module does OAuth authentication
        #                 and gives access token required to 
	#		  process REST APIs of Rubicon
        #INPUT		: self object used to give a reference to the 
	#		  current object.
	#OUTPUT		: Access token
        ###############################################################

	def fetch_token_operation(self):

		print '\n-----------------Authentication-----------------\n'
		#To disable verification of HTTPS requests
		#requests.packages.urllib3.disable_warnings()
		mashery = OAuth2Session(ConfigFile.client_id, redirect_uri=ConfigFile.redirect_uri)
		authorization_url, state = mashery.authorization_url(ConfigFile.authorization_base_url)
		#Conversion between http and https is required because OAuth2.0 supports only
		#SSL connection (https) and Application uses http connection 
		authorization_url = authorization_url.replace("https", "http", 1)
		print "Fetching access token...."
		#This function does login, selects grant type and returns redirected url containing access code
		redirect_response = seleniumLoginAutomation.login_automation(authorization_url)
		print '\nConfigFile.client_id' + ConfigFile.client_id + '\nConfigFile.client_secret : ' + ConfigFile.client_secret  
		#redirect_response = raw_input('\nRedirect URL : ')
		redirect_response = redirect_response.replace("http", "https", 1)
		tokenStr = str(mashery.fetch_token(ConfigFile.token_url, client_secret=ConfigFile.client_secret,authorization_response=redirect_response, verify=False))
		tokenStr = ast.literal_eval(tokenStr)
		Api.token = tokenStr.get('access_token')
		if not Api.token:
			print "Error while fetching access token."
			exit(0)
		print "\nAccess token : " + Api.token	

	#################################################################
        #NAME OF MODULE : list_operation
        #DESCRIPTION    : This module gives list of entities
        #                 specific to particular API
        #INPUT          : self object used to give a reference to the
	#		  current object.
        #OUTPUT         : NA
        #################################################################

	def list_operation(self):

		print '\n-----------------List endpoint-----------------\n'
		requests.packages.urllib3.disable_warnings()
		headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
		try:
			response = requests.get('%s/%s' %(Api.base_url, Api.url_path), verify=False, headers=headers)
			status_code = response.status_code
	        	print "\nResponse status code : %s" %status_code
			print response.text
			response.raise_for_status()
	        except requests.HTTPError, e:
        	        print 'HTTP ERROR.'
                	print e

	##################################################################
        #NAME OF MODULE : show_operation
        #DESCRIPTION    : This module gives Details of entity
        #                 specific to particular API
        #INPUT          : self object used to give a reference to the 
	#		  current object.
        #OUTPUT         : NA
        ##################################################################

	def show_operation(self, general_id):

		print '\n-----------------Show endpoint-----------------\n'
	        requests.packages.urllib3.disable_warnings()
        	headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
		try:
			if not general_id:
	                        print "No id found.\nPlease first execute Create endpoint Api to generate the id.\n"
				#exit(0)
			else:
				response = requests.get('%s/%s/%s' %(Api.base_url, Api.url_path, general_id), verify=False, headers=headers)
				status_code = response.status_code
				print "\nResponse Status_code : %s" %status_code
				print response.text
				response.raise_for_status()
		except requests.HTTPError, e:
			print 'HTTP ERROR.'
			print e


	####################################################################
        #NAME OF MODULE : upload_file_operation
        #DESCRIPTION    : This module uploads json file and image file to
        #                 database
        #INPUT	        : self object used to give a reference to the current
	#		  object,json_file_name i.e. name of file containing 
	#		  json data for upload api
	#OUTPUT         : upload_id
        ####################################################################

	def upload_file_operation(self, json_file_name):

        	print '\n-----------------Upload File endpoint-----------------\n'
	        #requests.packages.urllib3.disable_warnings()
        	headers = {'Accept': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
		files = {'file': open(json_file_name, 'rb')}
        	try:
                	response = requests.post('https://api.dspbuilder.rubiconproject.com/api/v1/uploadfile', verify=False, headers=headers, files=files)
	                status_code = response.status_code
        	        print "\nResponse Status_code : %s" %status_code
			response_str = response.text
        	        print response_str
			if response.status_code == requests.codes.ok :
				response_str = str(response.text)
				response_str = ast.literal_eval(response_str)
				return response_str.get('id')
	                response.raise_for_status()
        	except requests.HTTPError, e:
                	print 'HTTP ERROR.'
	                print e
		#finally:
			#return response.get('id')

	###############################################################
        #NAME OF MODULE : create_operation
        #DESCRIPTION    : This module creates entity for specific API
        #INPUT          : self object used to give a reference to the
        #                 current object
 	#OUTPUT         : general_id i.e. id of created entity
        ###############################################################

	def create_operation(self):

        	print '\n-----------------Create endpoint-----------------\n'
	        requests.packages.urllib3.disable_warnings()
        	headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
		try:
			if not Api.payload:
                                print "No payload data available to pass to post function\n"
                                #exit(0)
			else:
                		response = requests.post('%s/%s' %(Api.base_url, Api.url_path), verify=False, headers=headers, data=json.dumps(Api.payload))
	                	status_code = response.status_code
	        	        print "\nResponse Status_code : %s" %status_code
        	        	print response.text
				if response.status_code == requests.codes.ok :
        	        	        response_str = str(response.text)
                	        	response_str = ast.literal_eval(response_str)
	                        	return response_str.get('id')
		                response.raise_for_status()
        	except requests.HTTPError, e:
               		print 'HTTP ERROR.'
	                print e	

	###############################################################
        #NAME OF MODULE : update_operation
        #DESCRIPTION    : This module updates entity for specific API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

	def update_operation(self, general_id):

        	print '\n-----------------Update endpoint-----------------\n'
	        requests.packages.urllib3.disable_warnings()
        	headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
        	try:
			if not general_id:
                                print "No id found.\nPlease first execute Create endpoint function to generate its id.\n"
                                #exit(0)
			else:
		                response = requests.put('%s/%s/%s' %(Api.base_url, Api.url_path, general_id), verify=False, headers=headers, data=json.dumps(Api.payload))
        		        status_code = response.status_code
                		print "\nResponse Status_code : %s" %status_code
	                	print response.text
	        	        response.raise_for_status()
	        except requests.HTTPError, e:
        	        print 'HTTP ERROR.'
                	print e

	###############################################################
        #NAME OF MODULE : destroy_operation
        #DESCRIPTION    : This module deletes entity for specific API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ##############################################################

	def destroy_operation(self, general_id):

        	print '\n-----------------Destroy endpoint-----------------\n'
	        requests.packages.urllib3.disable_warnings()
        	headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
	        try:
			if not general_id:
                                print "No id found to destroy.\nPlease first execute Create endpoint function to generate id.\n"
                                #exit(0)
        		else:
			        response = requests.delete('%s/%s/%s' %(Api.base_url, Api.url_path, general_id), verify=False, headers=headers)
        	        	status_code = response.status_code
	        	        print "\nResponse Status_code : %s" %status_code
        	        	#print response.text
				if response.status_code == 204 :
					print "Deleted successfully"
	                	response.raise_for_status()
        	except requests.HTTPError, e:
                	print 'HTTP ERROR.'
	                print e

        ###############################################################
        #NAME OF MODULE : new_operation
        #DESCRIPTION    : This module details for specific API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ##############################################################

        def new_operation(self):

                print '\n-----------------New endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
                try:
                     	response = requests.get('%s/%s/new' %(Api.base_url, Api.url_path), verify=False, headers=headers)
                        status_code = response.status_code
                        print "\nResponse Status_code : %s" %status_code
                        print response.text
                        response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

        ###############################################################
        #NAME OF MODULE : pause_operation
        #DESCRIPTION    : This module pauses entity for specific API
        #INPUT          : self object used to give a reference to the
        #                 current object
        #OUTPUT         : NA
        ###############################################################

        def pause_operation(self, general_id):

                print '\n-----------------Pause endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
                try:
                        if not general_id:
				print "No id found.\nPlease first execute Create endpoint function to generate id.\n"
                                #exit(0)
                        else:
                        	response = requests.post('%s/%s/%s/pause' %(Api.base_url, Api.url_path, general_id), verify=False, headers=headers, data=json.dumps(Api.payload))
                        	status_code = response.status_code
                        	print "\nResponse Status_code : %s" %status_code
                        	print response.text
                        	response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

        ###############################################################
        #NAME OF MODULE : resume_operation
        #DESCRIPTION    : This module resumes entity for specific API
        #INPUT          : self object used to give a reference to the
        #                 current object
        #OUTPUT         : NA
        ###############################################################

        def resume_operation(self, general_id):

                print '\n-----------------Resume endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %Api.token}
                try:
                        if not general_id:
				print "No id found.\nPlease first execute Create endpoint function to generate id.\n"
                                #exit(0)
                        else:
	                        response = requests.post('%s/%s/%s/resume' %(Api.base_url, Api.url_path, general_id), verify=False, headers=headers, data=json.dumps(Api.payload))
        	                status_code = response.status_code
                	        print "\nResponse Status_code : %s" %status_code
                        	print response.text
	                        response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e


