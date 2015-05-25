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
		budget_value = 59

		list_end = list_endpoint()
		#This will execute list endpoint of organization API
		list_end.list_operation()
        	
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"organization": {"name": "New organization123", "url": "www.test1.com", "upload_id": "%s" %variables.upload_id }}
		create_end = create_endpoint()
                #This will execute create endpoint of organization API
		variables.org_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"organization": {"name": "Rename organization1", "url": "www.test1.com", "upload_id": "%s" %variables.upload_id }}
		update_end = update_endpoint()
		#This will execute update endpoint of organization API
                update_end.update_operation(variables.org_id)

		show_end = show_endpoint()
		#This will execute show endpoint of organization API
                show_end.show_operation(variables.org_id)

		destroy_end = destroy_endpoint()
		#This will execute destroy endpoint of organization API
                #destroy_end.destroy_operation(variables.org_id)

		org_get_budget_end = organization_get_budget_endpoint()
		#This will execute get budget endpoint of organization API
                org_get_budget_end.get_budget_operation()
	
		#This is the payload information which is required for adding budget.
                variables.payload = {"budget" : budget_value}
		org_add_budget_end = organization_add_budget_endpoint()
		#This will execute add budget endpoint of organization API
                org_add_budget_end.add_budget_operation()


