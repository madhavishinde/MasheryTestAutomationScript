#from lib.apis.variables import *
from lib.apis import variables
from lib.apis.create_endpoint import *
from lib.apis.list_endpoint import *
from lib.apis.update_endpoint import *
from lib.apis.destroy_endpoint import *
from lib.apis.show_endpoint import *

class ad_type():

	def runner(self):

		#This url_path variable sets endpoint path for adtype API
		variables.url_path = "api/v1/adtypes"
		
		list_end = list_endpoint()
		#This will execute list endpoint of adtype API
		list_end.list_operation()	
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"adtype" : {"name" : "Simple", "status" : "active"}}
		create_end = create_endpoint()
		#This will execute create endpoint of adtype API
                variables.adtype_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"adtype" : {"name" : "Simpleupdate", "status" : "active"}}
		update_end = update_endpoint()
		#This will execute update endpoint of adtype API
                update_end.update_operation(variables.adtype_id)

		show_end = show_endpoint()
		#This will execute show endpoint of adtype API
                show_end.show_operation(variables.adtype_id)

                destroy_end = destroy_endpoint()
		#This will execute destroy endpoint of adtype API
                #destroy_end.destroy_operation(variables.adtype_id)

