#from lib.apis.variables import *
from lib.apis import variables
from lib.apis.create_endpoint import *
from lib.apis.list_endpoint import *
from lib.apis.update_endpoint import *
from lib.apis.destroy_endpoint import *
from lib.apis.show_endpoint import *
from lib.apis.new_endpoint import *
from lib.apis.pause_endpoint import *
from lib.apis.resume_endpoint import *
from lib.apis.campaign.campaign_add_ad_endpoint import *
#campaign_add_ad_endpoint
from lib.apis.campaign.campaign_get_ads_endpoint import *
from lib.apis.campaign.campaign_remove_ad_endpoint import *
from lib.apis.campaign.campaign_clone_endpoint import *
from lib.apis.campaign.campaign_impressions_download_endpoint import *

class campaign():

	def runner(self):

		variables.url_path = "api/v1/campaigns"
		#variables.token = "8n2pb2w5k27jtp97dzwf55nb"

		list_end = list_endpoint()
		list_end.list_operation()
        	
		#This is the payload information which is required for showing details of organization.
                variables.payload = {"user_id":"%s" %variables.user_id,"organization_id":"%s" %variables.org_id}
                #This module creates organization.
                new_end = new_endpoint()
                new_end.new_operation()
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"campaign" : {"name" : "test_campaing123", "budget" : "12" , "bidder_id" : "%s" %variables.bidder_id, "adtype_id" : "%s" %variables.adtype_id, "start_date": "2015-02-14" , "end_date": "2015-02-26", "status" : "active"}}
		#This module creates organization.
		create_end = create_endpoint()
                variables.campaign_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"campaign" : {"name" : "test_campaing321", "budget" : "12" , "bidder_id" : "%s" %variables.bidder_id, "adtype_id" : "%s" %variables.adtype_id, "start_date": "2015-02-14" , "end_date": "2015-02-26", "status" : "active"}}
                #This module updates organization.
		update_end = update_endpoint()
                update_end.update_operation(variables.campaign_id)

		#This module gives details of specific organization
		show_end = show_endpoint()
                show_end.show_operation(variables.campaign_id)

		#This module pauses endpoint of specific organization
	        variables.payload = {}
		pause_end = pause_endpoint()
        	pause_end.pause_operation(variables.campaign_id)

	        #This module resumes endpoint of specific organization
        	variables.payload = {}
		resume_end = resume_endpoint()
	        resume_end.resume_operation(variables.campaign_id)

		#This module add ad to campaign
		variables.payload = {"ad" : "%s" % variables.ad_id}
	        campaign_add_ad_end = campaign_add_ad_endpoint()
		campaign_add_ad_end.add_ad_operation()
		#campaign_add_ad_end = campaign_add_ad_endpoint()
		#campaign_add_ad_end.add_ad_operation()
        	
		#This module remove ad from campaign
	        variables.payload = {"ad" : "%s" % variables.ad_id}
		campaign_remove_ad_end = campaign_remove_ad_endpoint()
		campaign_remove_ad_end.remove_ad_operation()
        	
		#This module displays ads attached
		campaign_get_ads_end = campaign_get_ads_endpoint()
	        campaign_get_ads_end.get_ads_operation()
	
        	#This module clones campaign
	        variables.payload = {"campaign_name" : "test_client"}
		campaign_clone_end = campaign_clone_endpoint()
        	campaign_clone_end.clone_operation()

	        #This module downloads impressions
		campaign_impressions_download_end = campaign_impressions_download_endpoint()
        	campaign_impressions_download_end.impressions_download_operation()

		#This module deletes organization
                destroy_end = destroy_endpoint()
                #destroy_end.destroy_operation(variables.campaign_id)


