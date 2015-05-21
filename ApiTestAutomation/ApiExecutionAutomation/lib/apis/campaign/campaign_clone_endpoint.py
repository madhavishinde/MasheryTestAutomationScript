import requests
from .. import variables
import json

class campaign_clone_endpoint:

        ###############################################################
        #NAME OF MODULE : clone_operation
        #DESCRIPTION    : This module clones campaign for Campaign API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def clone_operation(self):

                print '\n-----------------Clone endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        if not variables.campaign_id:
                                print "No campaign id found.\nPlease first execute Create endpoint function to generate its id.\n"
                        else:
                                response = requests.post('%s/%s/%s/clone' %(variables.base_url, variables.url_path, variables.campaign_id), verify=False, headers=headers, data=json.dumps(variables.payload))
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e


