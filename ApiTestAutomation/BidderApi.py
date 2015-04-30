#Includes BaseClassApi class
import BaseClassApi

class Bidder(BaseClassApi.Api):
	print "This is bidder api class: \n"

def execute_bidder_api():

	BaseClassApi.Api.url_path = "api/v1/bidders"
        bidder_api = Bidder()
        #This module gives list of organizations available.
        bidder_api.list_operation()
        #This module uploads file i.e. json data and returns upload id.
        #BaseClassApi.Api.upload_id = bidder_api.upload_file_operation(json_file_name)
        #This is the payload information which is required for creating organization.
     ##   #BaseClassApi.Api.payload = {"organization": {"name": "New organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
	BaseClassApi.Api.payload = {"bidder" : {"name" :"testbidder", "upload_id": "%s" %BaseClassApi.Api.upload_id, "status": "active"  }}
        #This module creates organization.
        BaseClassApi.Api.general_id = bidder_api.create_operation()
        #BaseClassApi.Api.general_id = ""
        #This is the payload information which is required for updating organization.
    ##  BaseClassApi.Api.payload = {"organization": {"name": "Rename organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        BaseClassApi.Api.payload = {"bidder" : {"name" :"update bidder", "upload_id": "%s" %BaseClassApi.Api.upload_id, "status": "active"  }}
 	#This module updates organization.
        bidder_api.update_operation()
        #This module gives details of specific organization
        bidder_api.show_operation()
        #This module deletes organization
        ########################org_api.destroy_operation()
