from lib.apis import variables
from lib.apis.create_endpoint import *
from lib.apis.list_endpoint import *
from lib.apis.update_endpoint import *
from lib.apis.destroy_endpoint import *
from lib.apis.show_endpoint import *
from lib.apis.user.user_get_roles_endpoint import *

class user():

	def runner(self):

		#This url_path variable sets endpoint path for user API
		variables.url_path = "api/v1/users"

		list_end = list_endpoint()
		#This will execute list endpoint of user API
		list_end.list_operation()	
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"user": {"name" : "56test89", "email" : "est_879@gmail.com", "role": 0 }}
		create_end = create_endpoint()
		#This will execute create endpoint of user API
                variables.user_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"user": {"name" : "test1289", "email" : "tte_9778@gmail.com", "role": 0 }}
		update_end = update_endpoint()
		#This will execute update endpoint of user API
                update_end.update_operation(variables.user_id)

		#This will set url_path to api/v1/user for executing show endpoint
		variables.url_path = "api/v1/user"
		show_end = show_endpoint()
		#This will execute show endpoint of user API
                show_end.show_operation(variables.user_id)
		#This will set url_path to api/v1/users for executing rest endpoint
		variables.url_path = "api/v1/users"

		user_get_roles_end = user_get_roles_endpoint()
		#This will execute get roles endpoint of user API
		user_get_roles_end.get_roles_operation()

                destroy_end = destroy_endpoint()
		#This will execute destroy endpoint of user API
                #destroy_end.destroy_operation(variables.user_id)

