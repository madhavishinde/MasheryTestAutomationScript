import requests
from .. import variables
import json

class ad_approve_endpoint():

        ###############################################################
        #NAME OF MODULE : approve_operation
        #DESCRIPTION    : This module approves ad for AD API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def approve_operation(self):

                print '\n-----------------Approve endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        response = requests.post('%s/%s/%s/approve' %(variables.base_url, variables.url_path, variables.ad_id), verify=False, headers=headers, data=json.dumps(variables.payload))
                        status_code = response.status_code
                        print "\nResponse Status_code : %s" %status_code
                        print response.text
                        response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

