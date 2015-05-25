from lib.apis import variables
from lib.apis.create_endpoint import *
from lib.apis.list_endpoint import *
from lib.apis.update_endpoint import *
from lib.apis.destroy_endpoint import *
from lib.apis.show_endpoint import *
from lib.apis.audiences.audiences_add_records_endpoint import *

class audiences():

	def runner(self):

		variables.url_path = "api/v1/audiences"

		list_end = list_endpoint()
		#This will execute list endpoint of audiences API
		list_end.list_operation()
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"audience": {"name" : "audience name" , "upload_id":"%s" %variables.upload_id}}
		create_end = create_endpoint()
		#This will execute create endpoint of audiences API
                variables.audience_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"audience": {"name" : "audience rename" , "upload_id":"%s" %variables.upload_id}}
		update_end = update_endpoint()
		#This will execute update endpoint of audiences API
                update_end.update_operation(variables.audience_id)

		show_end = show_endpoint()
		#This will execute show endpoint of audiences API
                show_end.show_operation(variables.audience_id)

	        variables.payload = {"upload_id": "%s" %variables.upload_id}
		audiences_add_records_end = audiences_add_records_endpoint()
		#This will execute add records endpoint of audiences API
        	audiences_add_records_end.add_records_operation()

                destroy_end = destroy_endpoint()
                #This will execute destroy endpoint of audiences API
		#destroy_end.destroy_operation(variables.audience_id)

