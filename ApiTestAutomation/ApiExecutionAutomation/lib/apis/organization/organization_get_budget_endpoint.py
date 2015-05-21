from .. import variables 
import requests

class organization_get_budget_endpoint:

        ###############################################################
        #NAME OF MODULE : get_budget_operation
        #DESCRIPTION    : This module gives budget details for organization
        #                 API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ################################################################

        def get_budget_operation(self):

                print '\n-----------------Get Budget endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        response = requests.get('%s/%s/budget' %(variables.base_url, variables.url_path), verify=False, headers=headers)
                        status_code = response.status_code
                        print "\nResponse Status_code : %s" %status_code
                        print response.text
                        response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e
