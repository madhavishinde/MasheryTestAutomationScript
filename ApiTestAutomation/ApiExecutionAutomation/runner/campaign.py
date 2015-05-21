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
from lib.apis.campaign.campaign_get_ads_endpoint import *
from lib.apis.campaign.campaign_remove_ad_endpoint import *
from lib.apis.campaign.campaign_clone_endpoint import *
from lib.apis.campaign.campaign_impressions_download_endpoint import *

class campaign():

	def runner(self):

		#This url_path variable sets endpoint path for campaign API
		variables.url_path = "api/v1/campaigns"

		list_end = list_endpoint()
		#This will execute list endpoint of campaign API
		list_end.list_operation()
        	
		#This is the payload information which is required for showing details of organization.
                variables.payload = {"user_id":"%s" %variables.user_id,"organization_id":"%s" %variables.org_id}
                new_end = new_endpoint()
		#This will execute new endpoint of campaign API
                new_end.new_operation()
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"campaign" : {"name" : "test_campaing123", "budget" : "12" , "bidder_id" : "%s" %variables.bidder_id, "adtype_id" : "%s" %variables.adtype_id, "start_date": "2015-02-14" , "end_date": "2015-02-26", "status" : "active"}}
		create_end = create_endpoint()
		#This will execute create endpoint of campaign API
                variables.campaign_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"campaign" : {"name" : "test_campaing321", "budget" : "12" , "bidder_id" : "%s" %variables.bidder_id, "adtype_id" : "%s" %variables.adtype_id, "start_date": "2015-02-14" , "end_date": "2015-02-26", "status" : "active"}}
		update_end = update_endpoint()
		#This will execute update endpoint of campaign API
                update_end.update_operation(variables.campaign_id)

		show_end = show_endpoint()
		#This will execute show endpoint of campaign API
                show_end.show_operation(variables.campaign_id)

	        variables.payload = {}
		pause_end = pause_endpoint()
		#This will execute pause endpoint of campaign API
        	pause_end.pause_operation(variables.campaign_id)

        	variables.payload = {}
		resume_end = resume_endpoint()
		#This will execute resume endpoint of campaign API
	        resume_end.resume_operation(variables.campaign_id)

		variables.payload = {"ad" : "%s" % variables.ad_id}
	        campaign_add_ad_end = campaign_add_ad_endpoint()
		#This will execute add ad endpoint of campaign API
		campaign_add_ad_end.add_ad_operation()
        	
	        variables.payload = {"ad" : "%s" % variables.ad_id}
		campaign_remove_ad_end = campaign_remove_ad_endpoint()
		#This will execute remove ad endpoint of campaign API
		campaign_remove_ad_end.remove_ad_operation()
        	
		campaign_get_ads_end = campaign_get_ads_endpoint()
		#This will execute get ads endpoint of campaign API
	        campaign_get_ads_end.get_ads_operation()
	
	        variables.payload = {"campaign_name" : "test_client"}
		campaign_clone_end = campaign_clone_endpoint()
		#This will execute clone endpoint of campaign API
        	campaign_clone_end.clone_operation()

		campaign_impressions_download_end = campaign_impressions_download_endpoint()
		#This will execute impressions download endpoint of campaign API
        	campaign_impressions_download_end.impressions_download_operation()

                destroy_end = destroy_endpoint()
		#This will execute destroy endpoint of campaign API
                #destroy_end.destroy_operation(variables.campaign_id)


