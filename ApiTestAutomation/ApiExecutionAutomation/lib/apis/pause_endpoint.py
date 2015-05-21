import requests
import variables
import json

class pause_endpoint:

        ###############################################################
        #NAME OF MODULE : pause_operation
        #DESCRIPTION    : This module pauses entity for specific API
        #INPUT          : self object used to give a reference to the
        #                 current object
        #OUTPUT         : NA
        ###############################################################

        def pause_operation(self, general_id):

                print '\n-----------------Pause endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        if not general_id:
                                print "No id found.\nPlease first execute Create endpoint function to generate id.\n"
                        else:
                                response = requests.post('%s/%s/%s/pause' %(variables.base_url, variables.url_path, general_id), verify=False, headers=headers, data=json.dumps(variables.payload))
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

