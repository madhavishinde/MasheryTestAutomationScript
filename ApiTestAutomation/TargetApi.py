#Includes BaseClassApi class
import BaseClassApi

class Target(BaseClassApi.Api):
        print "This is target api class: \n"

def execute_target_api():

        BaseClassApi.Api.url_path = "api/v1/targets"
        target_api = Target()
        #This module gives list of organizations available.
        target_api.list_operation()
        #This module uploads file i.e. json data and returns upload id.
        #BaseClassApi.Api.upload_id = aug_api.upload_file_operation(json_file_name)
        #This is the payload information which is required for creating organization.
     ##   #BaseClassApi.Api.payload = {"organization": {"name": "New organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        BaseClassApi.Api.payload = {"target": {"name" : "target name1", "price" : "20",  "segmentrules" : {"app.name": { "include": [ "^Casino" ]}}}}
        #This module creates organization.
        BaseClassApi.Api.target_id = target_api.create_operation()
        #BaseClassApi.Api.general_id = ""
        #This is the payload information which is required for updating organization.
    ##  BaseClassApi.Api.payload = {"organization": {"name": "Rename organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        BaseClassApi.Api.payload = {"target": {"name" : "target name1", "price" : "20",  "segmentrules" : {"app.name": { "include": [ "^Casino" ]}}}}
	# This requires extra modifications
        target_api.update_operation(BaseClassApi.Api.target_id)
        #This module gives details of specific organization

	#This module updates organization.

        target_api.show_operation(BaseClassApi.Api.target_id)
        #This module deletes organization
        ########################aug_api.destroy_operation(BaseClassApi.Api.target_id)

