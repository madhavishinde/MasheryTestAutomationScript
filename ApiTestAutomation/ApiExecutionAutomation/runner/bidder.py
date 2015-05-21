from lib.apis import variables
from lib.apis.create_endpoint import *
from lib.apis.list_endpoint import *
from lib.apis.update_endpoint import *
from lib.apis.destroy_endpoint import *
from lib.apis.show_endpoint import *

class bidder():

	def runner(self):

		#This url_path variable sets endpoint path for bidder API
		variables.url_path = "api/v1/bidders"

		list_end = list_endpoint()
		#This will execute list endpoint of bidder API
		list_end.list_operation()	
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"bidder" : {"name" :"testbidder", "upload_id": "%s" %variables.upload_id, "status": "active"  }}
		create_end = create_endpoint()
		#This will execute create endpoint of bidder API
                variables.bidder_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"bidder" : {"name" :"update bidder", "upload_id": "%s" %variables.upload_id, "status": "active"  }}
		update_end = update_endpoint()
		#This will execute update endpoint of bidder API
                update_end.update_operation(variables.bidder_id)

		show_end = show_endpoint()
		#This will execute show endpoint of bidder API
                show_end.show_operation(variables.bidder_id)

                destroy_end = destroy_endpoint()
                #This will execute destroy endpoint of bidder API
		#destroy_end.destroy_operation(variables.bidder_id)

