from lib.apis import variables
from lib.apis.create_endpoint import *
from lib.apis.list_endpoint import *
from lib.apis.update_endpoint import *
from lib.apis.destroy_endpoint import *
from lib.apis.show_endpoint import *

class augmentor():

	def runner(self):

		#This url_path variable sets endpoint path for augmentor API
		variables.url_path = "api/v1/augmentors"

		list_end = list_endpoint()
		#This will execute list endpoint of augmentor API
		list_end.list_operation()	
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"augmentor": {"name" : "audience name" , "upload_id":"%s" %variables.upload_id}}
		create_end = create_endpoint()
		#This will execute create endpoint of augmentor API
                variables.aug_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"augmentor": {"name" : "audience name" , "upload_id":"%s" %variables.upload_id}}
		update_end = update_endpoint()
		#This will execute update endpoint of augmentor API
                update_end.update_operation(variables.aug_id)

		show_end = show_endpoint()
		#This will execute show endpoint of augmentor API
                show_end.show_operation(variables.aug_id)

                destroy_end = destroy_endpoint()
                #This will execute destroy endpoint of augmentor API
		#destroy_end.destroy_operation(variables.aug_id)

