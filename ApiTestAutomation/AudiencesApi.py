#Includes BaseClassApi class
import BaseClassApi

class Audiences(BaseClassApi.Api):
        print "This is Audiences api class: \n"

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
        BaseClassApi.Api.general_id = audiences_api.create_operation()
        #BaseClassApi.Api.general_id = ""
        #This is the payload information which is required for updating organization.
    ##  BaseClassApi.Api.payload = {"organization": {"name": "Rename organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        BaseClassApi.Api.payload = {"audience": {"name" : "audience rename" , "upload_id":"%s" %BaseClassApi.Api.upload_id}}
        #This module updates organization.
        audiences_api.update_operation()
        #This module gives details of specific organization
        audiences_api.show_operation()
        #This module deletes organization
        ########################aug_api.destroy_operation()

