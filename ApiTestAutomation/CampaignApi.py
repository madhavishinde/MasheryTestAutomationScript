#Includes BaseClassApi class
import requests
import json
import BaseClassApi

class Campaign(BaseClassApi.Api):

	###############################################################
        #NAME OF MODULE : add_ad_operation
        #DESCRIPTION    : This module adds ad for Campaign API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def add_ad_operation(self):

                print '\n-----------------Add ad endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %BaseClassApi.Api.token}
                try:
                        if not BaseClassApi.Api.campaign_id:
                                print "No campaign id found.\nPlease first execute Create endpoint function to generate its id.\n"
                                #exit(0)
			elif not BaseClassApi.Api.ad_id:
				print "No ad id found.\nPlease first execute Create endpoint function to generate its id.\n"
                        else:
                                response = requests.post('%s/%s/%s/add_ad' %(BaseClassApi.Api.base_url, BaseClassApi.Api.url_path, BaseClassApi.Api.campaign_id), verify=False, headers=headers, data=json.dumps(BaseClassApi.Api.payload))
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

        ###############################################################
        #NAME OF MODULE : remove_ad_operation
        #DESCRIPTION    : This module removes ad for Campaign API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def remove_ad_operation(self):

                print '\n-----------------Remove ad endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %BaseClassApi.Api.token}
                try:
                        if not BaseClassApi.Api.campaign_id:
                                print "No campaign id found.\nPlease first execute Create endpoint function to generate its id.\n"
                                #exit(0)
                        elif not BaseClassApi.Api.ad_id:
                                print "No ad id found.\nPlease first execute Create endpoint function to generate its id.\n"
                        else:
                                response = requests.post('%s/%s/%s/remove_ad' %(BaseClassApi.Api.base_url, BaseClassApi.Api.url_path, BaseClassApi.Api.campaign_id), verify=False, headers=headers)
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

        ###############################################################
        #NAME OF MODULE : get_ads_operation
        #DESCRIPTION    : This module displays ads attached to Campaign API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def get_ads_operation(self):

                print '\n-----------------Get ads endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %BaseClassApi.Api.token}
                try:
                        if not BaseClassApi.Api.campaign_id:
                                print "No campaign id found.\nPlease first execute Create endpoint function to generate its id.\n"
                                #exit(0)
                        else:
                                response = requests.get('%s/%s/%s/ads' %(BaseClassApi.Api.base_url, BaseClassApi.Api.url_path, BaseClassApi.Api.campaign_id), verify=False, headers=headers, data=json.dumps(BaseClassApi.Api.payload))
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

        ###############################################################
        #NAME OF MODULE : clone_operation
        #DESCRIPTION    : This module clones campaign for Campaign API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def clone_operation(self):

                print '\n-----------------Clone endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %BaseClassApi.Api.token}
                try:
                        if not BaseClassApi.Api.campaign_id:
                                print "No campaign id found.\nPlease first execute Create endpoint function to generate its id.\n"
                                #exit(0)
                        else:
                                response = requests.post('%s/%s/%s/clone' %(BaseClassApi.Api.base_url, BaseClassApi.Api.url_path, BaseClassApi.Api.campaign_id), verify=False, headers=headers, data=json.dumps(BaseClassApi.Api.payload))
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

        ###############################################################
        #NAME OF MODULE : impressions_download_operation
        #DESCRIPTION    : This module downloads impressions for Campaign API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def impressions_download_operation(self):

                print '\n-----------------Impressions Download endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %BaseClassApi.Api.token}
                try:
                        if not BaseClassApi.Api.campaign_id:
                                print "No campaign id found.\nPlease first execute Create endpoint function to generate its id.\n"
                                #exit(0)
                        else:
                                response = requests.get('%s/%s/%s/impressions' %(BaseClassApi.Api.base_url, BaseClassApi.Api.url_path, BaseClassApi.Api.campaign_id), verify=False, headers=headers, data=json.dumps(BaseClassApi.Api.payload))
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e


        #print "This is Campaign api class: \n"

def execute_campaign_api():

        BaseClassApi.Api.url_path = "api/v1/campaigns"
        camp_api = Campaign()
	#This module gives details of campaigns.
        camp_api.new_operation()
        #This module gives list of organizations available.
        camp_api.list_operation()
        #This module uploads file i.e. json data and returns upload id.
        #BaseClassApi.Api.upload_id = aug_api.upload_file_operation(json_file_name)
        #This is the payload information which is required for creating organization.
     ##   #BaseClassApi.Api.payload = {"organization": {"name": "New organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        #BaseClassApi.Api.payload = {"augmentor": {"name" : "audience name" , "upload_id":"%s" %BaseClassApi.Api.upload_id}}
        #This module creates organization.
        #BaseClassApi.Api.campaign_id = camp_api.create_operation()
        BaseClassApi.Api.campaign_id = "55471b8670726f10b00f0000"
        #This is the payload information which is required for updating organization.
    ##  BaseClassApi.Api.payload = {"organization": {"name": "Rename organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        #BaseClassApi.Api.payload = {"augmentor": {"name" : "audience name" , "upload_id":"%s" %BaseClassApi.Api.upload_id}}
        #This module updates organization.
        #camp_api.update_operation(BaseClassApi.Api.campaign_id)
        #This module gives details of specific organization
        camp_api.show_operation(BaseClassApi.Api.campaign_id)
	#This module pauses endpoint of specific organization
	BaseClassApi.Api.payload = {}
        camp_api.pause_operation(BaseClassApi.Api.campaign_id)
	#This module resumes endpoint of specific organization
        BaseClassApi.Api.payload = {}
        camp_api.resume_operation(BaseClassApi.Api.campaign_id)
	BaseClassApi.Api.payload = {"ad" : "%s" % BaseClassApi.Api.ad_id}
        camp_api.add_ad_operation()
	BaseClassApi.Api.payload = {"ad" : "%s" % BaseClassApi.Api.ad_id}
        camp_api.remove_ad_operation()
	#This module displays ads attached
	camp_api.get_ads_operation()

	#This module clones campaign
        BaseClassApi.Api.payload = {"campaign_name" : "test_client"}
        camp_api.clone_operation()
	#This module downloads impressions
	camp_api.impressions_download_operation()
 	#This module deletes organization
        ########################
	#camp_api.destroy_operation(BaseClassApi.Api.campaign_id)

