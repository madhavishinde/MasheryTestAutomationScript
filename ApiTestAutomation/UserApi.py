#Includes BaseClassApi class
import BaseClassApi

class User(BaseClassApi.Api):
        print "This is user api class: \n"

def execute_user_api():

        BaseClassApi.Api.url_path = "api/v1/users"
        user_api = User()
        #This module gives list of organizations available.
        user_api.list_operation()
        #This module uploads file i.e. json data and returns upload id.
        #BaseClassApi.Api.upload_id = aug_api.upload_file_operation(json_file_name)
        #This is the payload information which is required for creating organization.
     ##   #BaseClassApi.Api.payload = {"organization": {"name": "New organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        BaseClassApi.Api.payload = {"user": {"name" : "test", "email" : "test_user+1@gmail.com", "role": 0 }}
        #This module creates organization.
        BaseClassApi.Api.user_id = user_api.create_operation()
        #BaseClassApi.Api.general_id = ""
        #This is the payload information which is required for updating organization.
    ##  BaseClassApi.Api.payload = {"organization": {"name": "Rename organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        BaseClassApi.Api.payload = {"user": {"name" : "retest", "email" : "test_user+1@gmail.com", "role": 0 }}
        #This module updates organization.
        user_api.update_operation(BaseClassApi.Api.user_id)
        #This module gives details of specific organization
	#This requires extra modifications

        #user_api.show_operation(BaseClassApi.Api.user_id)
        #This module deletes organization
        ########################user_api.destroy_operation(BaseClassApi.Api.user_id)

