#from lib.apis.variables import *
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

		variables.url_path = "api/v1/ads"
		#variables.token = "8n2pb2w5k27jtp97dzwf55nb"

		list_end = list_endpoint()
		list_end.list_operation()
        	
                
		#This is the payload information which is required for creating organization.
                variables.payload = {"ad" : {"label" : "ad" , "upload_id" : "%s" %variables.upload_id , "alttext" : "sd", "url" : "ww.test.url.com", "width": "100" , "height": "120"}}
		#This module creates organization.
		create_end = create_endpoint()
                variables.ad_id = create_end.create_operation()

		#This is the payload information which is required for updating organization.
                variables.payload = {"ad" : {"label" : "ad" , "upload_id" : "%s" %variables.upload_id , "alttext" : "sd", "url" : "ww.test.url.com", "width": "200" , "height": "120"}}
                #This module updates organization.
		update_end = update_endpoint()
                update_end.update_operation(variables.ad_id)

		#This module gives details of specific organization
		show_end = show_endpoint()
                show_end.show_operation(variables.ad_id)

		#This module pauses endpoint of specific ad
	        variables.payload = {}
		pause_end = pause_endpoint()
        	pause_end.pause_operation(variables.ad_id)

		#This module resumes endpoint of specific ad
	        variables.payload = {}
		resume_end = resume_endpoint()
                resume_end.resume_operation(variables.ad_id)

		#This module shows list of unapproved ads
		ad_list_unapproved_end = ad_list_unapproved_endpoint()
	        ad_list_unapproved_end.list_unapproved_operation()

		#This module approves ads
	        variables.payload = {}
		ad_approve_end = ad_approve_endpoint()
        	ad_approve_end.approve_operation()

		#This module deletes organization
                destroy_end = destroy_endpoint()
                #destroy_end.destroy_operation(variables.ad_id)

def main():
	print "fi"
	ad_obj = ad()
	ad_obj.runner()
	#m1.print1()

if __name__ == '__main__':
        main()

