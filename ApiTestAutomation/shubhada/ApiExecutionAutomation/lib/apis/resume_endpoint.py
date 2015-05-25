#To disable warnings
import requests
#For json operation
import json
#to access common variables
import variables

class resume_endpoint:


        ###############################################################
        #NAME OF MODULE : resume_operation
        #DESCRIPTION    : This module resumes entity for specific API
        #INPUT          : self object used to give a reference to the
        #                 current object
        #OUTPUT         : NA
        ###############################################################

        def resume_operation(self, general_id):

                print '\n-----------------Resume endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        if not general_id:
                                print "No id found.\nPlease first execute Create endpoint function to generate id.\n"
                        else:
                                response = requests.post('%s/%s/%s/resume' %(variables.base_url, variables.url_path, general_id), verify=False, headers=headers, data=json.dumps(variables.payload))
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

