#from lib.apis.variables import *
from lib.apis import variables
from lib.apis.create_endpoint import *
from lib.apis.list_endpoint import *
from lib.apis.update_endpoint import *
from lib.apis.destroy_endpoint import *
from lib.apis.show_endpoint import *
from lib.apis.user.user_get_roles_endpoint import *

class user():

	def runner(self):

		variables.url_path = "api/v1/users"
		#variables.token = "8n2pb2w5k27jtp97dzwf55nb"

		list_end = list_endpoint()
		list_end.list_operation()	
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"user": {"name" : "test89", "email" : "retest_89@gmail.com", "role": 0 }}
		#This module creates organization.
		create_end = create_endpoint()
                variables.user_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"user": {"name" : "ttttt89", "email" : "restte_98@gmail.com", "role": 0 }}
                #This module updates organization.
		update_end = update_endpoint()
                update_end.update_operation(variables.user_id)

		#This module gives details of specific organization
		variables.url_path = "api/v1/user"
		show_end = show_endpoint()
                show_end.show_operation(variables.user_id)
		variables.url_path = "api/v1/users"

		#This module gets details of roles for user API
	        #variables.url_path = "api/v1/organizations"
		user_get_roles_end = user_get_roles_endpoint()
		user_get_roles_end.get_roles_operation()
		#variables.url_path = "api/v1/users"

		#This module deletes organization
                destroy_end = destroy_endpoint()
                #destroy_end.destroy_operation(variables.user_id)

