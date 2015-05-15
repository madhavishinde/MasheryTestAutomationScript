#Includes BaseClassApi class
import BaseClassApi
import requests

class User(BaseClassApi.Api):

        ###############################################################
        #NAME OF MODULE : get_roles_operation
        #DESCRIPTION    : This module gives roles details for organization
        #                 API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ################################################################

        def get_roles_operation(self):

                print '\n-----------------Get Roles endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %BaseClassApi.Api.token}
                try:
                        if not BaseClassApi.Api.org_id:
                                print "No organization id found.\nPlease first execute Create endpoint function to generate its id.\n"
                        else:
                                response = requests.get('%s/%s/roles' %(BaseClassApi.Api.base_url, BaseClassApi.Api.url_path), verify=False, headers=headers)
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e


def execute_user_api():

        BaseClassApi.Api.url_path = "api/v1/users"
        user_api = User()
        #This module gives list of organizations available.
        user_api.list_operation()
        #This module uploads file i.e. json data and returns upload id.
        #BaseClassApi.Api.upload_id = aug_api.upload_file_operation(json_file_name)
        #This is the payload information which is required for creating organization.
     ##   #BaseClassApi.Api.payload = {"organization": {"name": "New organization1", "url": "www.test1.com", "upload_id": "%s" %BaseClassApi.Api.upload_id }}
        BaseClassApi.Api.payload = {"user": {"name" : "test_test", "email" : "test_test@gmail.com", "role": 0 }}
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
	#BaseClassApi.Api.url_path = "api/v1/user"
        #user_api.show_operation(BaseClassApi.Api.user_id)
	BaseClassApi.Api.url_path = "api/v1/users"
        #This module deletes organization
        ########################user_api.destroy_operation(BaseClassApi.Api.user_id)
	#This module gets details of roles for user API
        user_api.get_roles_operation()
