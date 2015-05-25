import requests
from .. import variables
import json

class audiences_add_records_endpoint:

	###############################################################
        #NAME OF MODULE : add_records_operation
        #DESCRIPTION    : This module adds records for Audiences API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def add_records_operation(self):

                print '\n-----------------Add Records Endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        if not variables.audience_id:
                                print "No audience id found.\nPlease first execute Create endpoint function to generate its id.\n"
                        elif not variables.payload:
                                print "No payload data found to post.\n"
                        else:
                                response = requests.post('%s/%s/%s/addrecords' %(variables.base_url, variables.url_path, variables.audience_id), verify=False, headers=headers, data=json.dumps(variables.payload))
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e
