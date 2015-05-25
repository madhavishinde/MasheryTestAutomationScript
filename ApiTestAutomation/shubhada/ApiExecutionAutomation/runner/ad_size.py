from lib.apis import variables
from lib.apis.create_endpoint import *
from lib.apis.list_endpoint import *
from lib.apis.update_endpoint import *
from lib.apis.destroy_endpoint import *
from lib.apis.show_endpoint import *

class ad_size():

	def runner(self):

		#This url_path variable sets endpoint path for ad API
		variables.url_path = "api/v1/adsizes"

		list_end = list_endpoint()
		#This module executes list endpoint of adsize API
		list_end.list_operation()	
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"adsize" : {"width" : 120, "height": 20 , "format" : "png", "status" : "active"}}
		create_end = create_endpoint()
		#This module executes create endpoint of adsize API
                variables.adsize_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"adsize" : {"width" : 140, "height": 20 , "format" : "png", "status" : "active"}}
		update_end = update_endpoint()
		#This module executes update endpoint of adsize API
                update_end.update_operation(variables.adsize_id)

		show_end = show_endpoint()
		#This module executes show endpoint of adsize API
                show_end.show_operation(variables.adsize_id)

                destroy_end = destroy_endpoint()
		#This module executes destroy endpoint of adsize API
                #destroy_end.destroy_operation(variables.adsize_id)

