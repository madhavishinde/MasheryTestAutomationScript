#To disable warnings
import requests
#To use common variables
import variables
#For json operation
import json
#For converting string to dictionary
import ast

class create_endpoint:
	###############################################################
	#NAME OF MODULE : create_operation
	#DESCRIPTION    : This module creates entity for specific API
	#INPUT          : self object used to give a reference to the
	#                 current object
	#OUTPUT         : id i.e. id of created entity
	###############################################################

	def create_operation(self):

	        print '\n-----------------Create endpoint-----------------\n'
        	requests.packages.urllib3.disable_warnings()
	        headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
        	try:
	                if not variables.payload:
        	                print "No payload data available to pass to post function\n"
	                else:
        	                if "targets" in variables.url_path:
	                                response = requests.post('%s/api/v1/campaigns/%s/targets' %(variables.base_url, variables.campaign_id), verify=False, headers=headers, data=json.dumps(variables.payload))
        	                else:
                	                response = requests.post('%s/%s' %(variables.base_url, variables.url_path), verify=False, headers=headers, data=json.dumps(variables.payload))
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

