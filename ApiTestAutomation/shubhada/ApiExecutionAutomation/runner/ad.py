from lib.apis import variables
from lib.apis.create_endpoint import *
from lib.apis.list_endpoint import *
from lib.apis.update_endpoint import *
from lib.apis.destroy_endpoint import *
from lib.apis.show_endpoint import *
from lib.apis.resume_endpoint import *
from lib.apis.pause_endpoint import *
from lib.apis.ad.ad_approve_endpoint import *
from lib.apis.ad.ad_list_unapproved_endpoint import *

class ad():

	def runner(self):

		#This url_path variable sets endpoint path for ad API 
		variables.url_path = "api/v1/ads"

		list_end = list_endpoint()
		#This will execute list endpoint of ad API
		list_end.list_operation()
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"ad" : {"label" : "ad" , "upload_id" : "%s" %variables.upload_id , "alttext" : "sd", "url" : "ww.test.url.com", "width": "100" , "height": "120"}}
		create_end = create_endpoint()
		#This will execute create endpoint of ad API
                variables.ad_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"ad" : {"label" : "ad" , "upload_id" : "%s" %variables.upload_id , "alttext" : "sd", "url" : "ww.test.url.com", "width": "200" , "height": "120"}}
		update_end = update_endpoint()
		#This will execute update endpoint of ad API
                update_end.update_operation(variables.ad_id)

		show_end = show_endpoint()
		#This will execute show endpoint of ad API
                show_end.show_operation(variables.ad_id)

	        variables.payload = {}
		pause_end = pause_endpoint()
		#This will execute pause endpoint of ad API
        	pause_end.pause_operation(variables.ad_id)

	        variables.payload = {}
		resume_end = resume_endpoint()
		#This will execute resume endpoint of ad API
                resume_end.resume_operation(variables.ad_id)

		ad_list_unapproved_end = ad_list_unapproved_endpoint()
		#This will execute list_unapproved endpoint of ad API
	        ad_list_unapproved_end.list_unapproved_operation()

	        variables.payload = {}
		ad_approve_end = ad_approve_endpoint()
		#This will execute approve endpoint of ad API
        	ad_approve_end.approve_operation()

                destroy_end = destroy_endpoint()
		#This will execute destroy endpoint of ad API
                #destroy_end.destroy_operation(variables.ad_id)

