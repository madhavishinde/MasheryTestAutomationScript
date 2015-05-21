from lib.apis import variables
from lib.apis.create_endpoint import *
from lib.apis.list_endpoint import *
from lib.apis.update_endpoint import *
from lib.apis.destroy_endpoint import *
from lib.apis.show_endpoint import *

class target():

	def runner(self):

		#This url_path variable sets endpoint path for target API
		variables.url_path = "targets"

		list_end = list_endpoint()
		#This will execute list endpoint of target API
		list_end.list_operation()	
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"target": {"name" : "target name2", "price" : "20",  "segmentrules" : [{"app.name": { "include": [ "^Casino" ]}}]}}
		create_end = create_endpoint()
		#This will execute create endpoint of target API
                variables.target_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"target": {"name" : "target name2", "price" : "20",  "segmentrules" : [{"app.name": { "include": [ "^Casino" ]}}]}}
		update_end = update_endpoint()
		#This will execute update endpoint of target API
                update_end.update_operation(variables.target_id)

		show_end = show_endpoint()
		#This will execute show endpoint of target API
                show_end.show_operation(variables.target_id)

                destroy_end = destroy_endpoint()
		#This will execute destroy endpoint of target API
                destroy_end.destroy_operation(variables.target_id)

