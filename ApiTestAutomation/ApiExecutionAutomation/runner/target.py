#from lib.apis.variables import *
from lib.apis import variables
from lib.apis.create_endpoint import *
from lib.apis.list_endpoint import *
from lib.apis.update_endpoint import *
from lib.apis.destroy_endpoint import *
from lib.apis.show_endpoint import *

class target():

	def runner(self):

		variables.url_path = "targets"
		#variables.token = "8n2pb2w5k27jtp97dzwf55nb"
		#variables.campaign_id = "5552e63169702d5b72000000"

		list_end = list_endpoint()
		list_end.list_operation()	
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"target": {"name" : "target name2", "price" : "20",  "segmentrules" : [{"app.name": { "include": [ "^Casino" ]}}]}}
		#This module creates organization.
		create_end = create_endpoint()
                variables.target_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"target": {"name" : "target name2", "price" : "20",  "segmentrules" : [{"app.name": { "include": [ "^Casino" ]}}]}}
                #This module updates organization.
		update_end = update_endpoint()
                update_end.update_operation(variables.target_id)

		#This module gives details of specific organization
		show_end = show_endpoint()
                show_end.show_operation(variables.target_id)

		#This module deletes organization
                destroy_end = destroy_endpoint()
                destroy_end.destroy_operation(variables.target_id)

