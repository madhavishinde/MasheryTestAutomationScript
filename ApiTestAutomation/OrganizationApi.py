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
import ConfigFile
#To use login automation function
import seleniumLoginAutomation
#Includes BaseClassApi class
import BaseClassApi

class Organization(BaseClassApi.Api):

        ###############################################################
        #NAME OF MODULE : get_budget_operation
        #DESCRIPTION    : This module gives budget details for organization
        #                 API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ################################################################

        def get_budget_operation(self):

                print '\n-----------------Get Budget endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %BaseClassApi.Api.token}
                try:
                        response = requests.get('%s/%s/budget' %(BaseClassApi.Api.base_url, BaseClassApi.Api.url_path), verify=False, headers=headers)
                        status_code = response.status_code
                        print "\nResponse Status_code : %s" %status_code
                        print response.text
                        response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

        ###############################################################
        #NAME OF MODULE : add_budget_operation
        #DESCRIPTION    : This module adds budget for organization API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################


        def add_budget_operation(self):

                print '\n-----------------Add Budget endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %BaseClassApi.Api.token}
                try:
                        if not BaseClassApi.Api.payload:
                                print "No payload data available to pass to post function\n"
                                #exit(0)
                        else:
                                response = requests.post('%s/%s/budget' %(BaseClassApi.Api.base_url, BaseClassApi.Api.url_path), verify=False, headers=headers, data=json.dumps(BaseClassApi.Api.payload))
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e


def execute_organization_api():

	BaseClassApi.Api.url_path = "api/v1/organizations"
	org_api = Organization()
	budget_value = 59
	#This module gives list of organizations available.
        org_api.list_operation()
	#This module uploads file i.e. json data and returns upload id.
        #BaseClassApi.Api.upload_id = org_api.upload_file_operation(json_file_name)
        #This is the payload information which is required for creating organization.
        BaseClassApi.Api.payload = {"organization": {"name": "New organization123", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}   
        #This module creates organization.
        BaseClassApi.Api.org_id = org_api.create_operation()
	#BaseClassApi.Api.org_id = "5541632370726f725d3e0000"
        #This is the payload information which is required for updating organization.
        BaseClassApi.Api.payload = {"organization": {"name": "Rename organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        #This module updates organization.
        org_api.update_operation(BaseClassApi.Api.org_id)
        #This module gives details of specific organization
        org_api.show_operation(BaseClassApi.Api.org_id)
        #This module deletes organization
        ########################
	org_api.destroy_operation(BaseClassApi.Api.org_id)
        #This module gives budget details
        org_api.get_budget_operation()
        #This is the payload information which is required for adding budget.
        BaseClassApi.Api.payload = {"budget" : budget_value}
        #This module adds budget
        org_api.add_budget_operation()
