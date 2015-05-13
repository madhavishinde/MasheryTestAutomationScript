#Includes BaseClassApi class
import requests
import json
import BaseClassApi

class Ad(BaseClassApi.Api):

	###############################################################
        #NAME OF MODULE : list_unapproved_operation
        #DESCRIPTION    : This module shows list of unapproved for AD API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def list_unapproved_operation(self):

                print '\n-----------------List Unapproved endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %BaseClassApi.Api.token}
                try:
                        response = requests.get('%s/%s/unapproved' %(BaseClassApi.Api.base_url, BaseClassApi.Api.url_path), verify=False, headers=headers)
                        status_code = response.status_code
                        print "\nResponse Status_code : %s" %status_code
                        print response.text
                        response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

        ###############################################################
        #NAME OF MODULE : approve_operation
        #DESCRIPTION    : This module approves ad for AD API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def approve_operation(self):

                print '\n-----------------Approve endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %BaseClassApi.Api.token}
                try:
                        response = requests.post('%s/%s/%s/approve' %(BaseClassApi.Api.base_url, BaseClassApi.Api.url_path, BaseClassApi.Api.ad_id), verify=False, headers=headers, data=json.dumps(BaseClassApi.Api.payload))
                        status_code = response.status_code
                        print "\nResponse Status_code : %s" %status_code
                        print response.text
                        response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e


        #print "This is AdApi class: \n"

def execute_ad_api():

        BaseClassApi.Api.url_path = "api/v1/ads"
        ad_api = Ad()
        #This module gives details of ads.
        ad_api.new_operation()
	#This module gives list of organizations available.
        ad_api.list_operation()
        #This module uploads file i.e. json data and returns upload id.
        #BaseClassApi.Api.upload_id = aug_api.upload_file_operation(json_file_name)
        #This is the payload information which is required for creating organization.
        BaseClassApi.Api.payload = {"ad" : {"label" : "ad" , "upload_id" : "%s" %BaseClassApi.Api.upload_id , "alttext" : "sd", "url" : "ww.test.url.com", "width": "100" , "height": "120"}}
        #This module creates organization.
        BaseClassApi.Api.ad_id = ad_api.create_operation()
        #BaseClassApi.Api.general_id = ""
        #This is the payload information which is required for updating organization.
    ##  BaseClassApi.Api.payload = {"organization": {"name": "Rename organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        BaseClassApi.Api.payload = {"ad" : {"label" : "ad" , "upload_id" : "%s" %BaseClassApi.Api.upload_id , "alttext" : "sd", "url" : "ww.test.url.com", "width": "200" , "height": "120"}}
        #This module updates organization.
        ad_api.update_operation(BaseClassApi.Api.ad_id)
        #This module gives details of specific organization
        ad_api.show_operation(BaseClassApi.Api.ad_id)
	#This module pauses endpoint of specific ad
        BaseClassApi.Api.payload = {}
        ad_api.pause_operation(BaseClassApi.Api.ad_id)
        #This module resumes endpoint of specific ad
        BaseClassApi.Api.payload = {}
        ad_api.resume_operation(BaseClassApi.Api.ad_id)
	#This module shows list of unapproved ads
        ad_api.list_unapproved_operation()
	#This module approves ads
        BaseClassApi.Api.payload = {}
        ad_api.approve_operation()
        #This module deletes ad
        ########################
	#ad_api.destroy_operation(BaseClassApi.Api.ad_id)

