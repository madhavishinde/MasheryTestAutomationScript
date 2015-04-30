#Includes BaseClassApi class
import BaseClassApi

class Ad(BaseClassApi.Api):
        print "This is AdApi class: \n"

def execute_ad_api():

        BaseClassApi.Api.url_path = "api/v1/ads"
        ad_api = Ad()
        #This module gives list of organizations available.
        ad_api.list_operation()
        #This module uploads file i.e. json data and returns upload id.
        #BaseClassApi.Api.upload_id = aug_api.upload_file_operation(json_file_name)
        #This is the payload information which is required for creating organization.
     ##   #BaseClassApi.Api.payload = {"organization": {"name": "New organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        BaseClassApi.Api.payload = {"ad" : {"label" : "ad" , "upload_id" : "%s" %BaseClassApi.Api.upload_id , "alttext" : "sd", "url" : "ww.test.url.com", "width": "100" , "height": "120"}}
        #This module creates organization.
        BaseClassApi.Api.general_id = ad_api.create_operation()
        #BaseClassApi.Api.general_id = ""
        #This is the payload information which is required for updating organization.
    ##  BaseClassApi.Api.payload = {"organization": {"name": "Rename organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        BaseClassApi.Api.payload = {"ad" : {"label" : "ad" , "upload_id" : "%s" %BaseClassApi.Api.upload_id , "alttext" : "sd", "url" : "ww.test.url.com", "width": "200" , "height": "120"}}
        #This module updates organization.
        ad_api.update_operation()
        #This module gives details of specific organization
        ad_api.show_operation()
        #This module deletes organization
        ########################aug_api.destroy_operation()

