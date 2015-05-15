#Includes BaseClassApi class
import BaseClassApi
#For json operation
import json
#To disable warnings
import requests

class Audiences(BaseClassApi.Api):

	###############################################################
        #NAME OF MODULE : add_records_operation
        #DESCRIPTION    : This module adds records for Audiences API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def add_records_operation(self):

                print '\n-----------------Add Records Endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %BaseClassApi.Api.token}
                try:
                        if not BaseClassApi.Api.audience_id:
                                print "No audience id found.\nPlease first execute Create endpoint function to generate its id.\n"
                                #exit(0)
                        elif not BaseClassApi.Api.payload:
                                print "No payload data found to post.\n"
                        else:
                                response = requests.post('%s/%s/%s/addrecords' %(BaseClassApi.Api.base_url, BaseClassApi.Api.url_path, BaseClassApi.Api.audience_id), verify=False, headers=headers, data=json.dumps(BaseClassApi.Api.payload))
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

        #print "This is Audiences api class: \n"

def execute_audiences_api():

        BaseClassApi.Api.url_path = "api/v1/audiences"
        audiences_api = Audiences()
        #This module gives list of organizations available.
        audiences_api.list_operation()
        #This module uploads file i.e. json data and returns upload id.
        #BaseClassApi.Api.upload_id = aug_api.upload_file_operation(json_file_name)
        #This is the payload information which is required for creating organization.
     ##   #BaseClassApi.Api.payload = {"organization": {"name": "New organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        BaseClassApi.Api.payload = {"audience": {"name" : "audience name" , "upload_id":"%s" %BaseClassApi.Api.upload_id}}
        #This module creates organization.
        BaseClassApi.Api.audience_id = audiences_api.create_operation()
        #BaseClassApi.Api.general_id = ""
        #This is the payload information which is required for updating organization.
    ##  BaseClassApi.Api.payload = {"organization": {"name": "Rename organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        BaseClassApi.Api.payload = {"audience": {"name" : "audience rename" , "upload_id":"%s" %BaseClassApi.Api.upload_id}}
        #This module updates organization.
        audiences_api.update_operation(BaseClassApi.Api.audience_id)
        #This module gives details of specific organization
        audiences_api.show_operation(BaseClassApi.Api.audience_id)
	#This module adds records to audience API
	BaseClassApi.Api.payload = {"upload_id": "%s" %BaseClassApi.Api.upload_id}
        audiences_api.add_records_operation()
        #This module deletes organization
        ########################audiences_api.destroy_operation(BaseClassApi.Api.audience_id)

