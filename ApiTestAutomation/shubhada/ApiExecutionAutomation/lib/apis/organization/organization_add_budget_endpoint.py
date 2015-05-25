from .. import variables
import requests
import json

class organization_add_budget_endpoint:


        ###############################################################
        #NAME OF MODULE : add_budget_operation
        #DESCRIPTION    : This module adds budget for organization API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################


        def add_budget_operation(self):

                print '\n-----------------Add Budget endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        if not variables.payload:
                                print "No payload data available to pass to post function\n"
                        else:
                                response = requests.post('%s/%s/budget' %(variables.base_url, variables.url_path), verify=False, headers=headers, data=json.dumps(variables.payload))
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

