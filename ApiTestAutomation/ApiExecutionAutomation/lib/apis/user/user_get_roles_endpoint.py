import requests
from .. import variables

class user_get_roles_endpoint:


        ###############################################################
        #NAME OF MODULE : get_roles_operation
        #DESCRIPTION    : This module gives roles details for user
        #                 API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ################################################################

        def get_roles_operation(self):

                print '\n-----------------Get Roles endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        response = requests.get('%s/%s/roles' %(variables.base_url, variables.url_path), verify=False, headers=headers)
                        status_code = response.status_code
                        print "\nResponse Status_code : %s" %status_code
                       	print response.text
                        response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

