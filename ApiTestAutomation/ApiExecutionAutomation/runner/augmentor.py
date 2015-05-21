#from lib.apis.variables import *
from lib.apis import variables
from lib.apis.create_endpoint import *
from lib.apis.list_endpoint import *
from lib.apis.update_endpoint import *
from lib.apis.destroy_endpoint import *
from lib.apis.show_endpoint import *

class augmentor():

	def runner(self):

		variables.url_path = "api/v1/augmentors"
		#variables.token = "8n2pb2w5k27jtp97dzwf55nb"

		list_end = list_endpoint()
		list_end.list_operation()	
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"augmentor": {"name" : "audience name" , "upload_id":"%s" %variables.upload_id}}
		#This module creates organization.
		create_end = create_endpoint()
                variables.aug_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"augmentor": {"name" : "audience name" , "upload_id":"%s" %variables.upload_id}}
                #This module updates organization.
		update_end = update_endpoint()
                update_end.update_operation(variables.aug_id)

		#This module gives details of specific organization
		show_end = show_endpoint()
                show_end.show_operation(variables.aug_id)

		#This module deletes organization
                destroy_end = destroy_endpoint()
                #destroy_end.destroy_operation(variables.aug_id)

