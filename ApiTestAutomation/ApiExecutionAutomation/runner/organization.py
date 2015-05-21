#from lib.apis.variables import *
from lib.apis import variables
from lib.apis.create_endpoint import *
from lib.apis.list_endpoint import *
from lib.apis.update_endpoint import *
from lib.apis.destroy_endpoint import *
from lib.apis.show_endpoint import *
from lib.apis.organization.organization_get_budget_endpoint import *
from lib.apis.organization.organization_add_budget_endpoint import *

class organization():

	def runner(self):

		variables.url_path = "api/v1/organizations"
		#variables.token = "8n2pb2w5k27jtp97dzwf55nb"
		budget_value = 59

		list_end = list_endpoint()
		list_end.list_operation()
        	
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"organization": {"name": "New organization123", "url": "www.test1.com", "upload_id": "%s" %variables.upload_id }}
		#This module creates organization.
		create_end = create_endpoint()
                variables.org_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"organization": {"name": "Rename organization1", "url": "www.test1.com", "upload_id": "%s" %variables.upload_id }}
                #This module updates organization.
		update_end = update_endpoint()
                update_end.update_operation(variables.org_id)

		#This module gives details of specific organization
		show_end = show_endpoint()
                show_end.show_operation(variables.org_id)

		#This module deletes organization
		destroy_end = destroy_endpoint()
                #destroy_end.destroy_operation(variables.org_id)

		#This module gives budget details
		org_get_budget_end = organization_get_budget_endpoint()
                org_get_budget_end.get_budget_operation()
	
		#This is the payload information which is required for adding budget.
                variables.payload = {"budget" : budget_value}
		#This module adds budget
		org_add_budget_end = organization_add_budget_endpoint()
                org_add_budget_end.add_budget_operation()


