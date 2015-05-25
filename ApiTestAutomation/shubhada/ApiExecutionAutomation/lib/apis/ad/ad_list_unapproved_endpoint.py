import requests
from .. import variables


class ad_list_unapproved_endpoint():

        ###############################################################
        #NAME OF MODULE : list_unapproved_operation
        #DESCRIPTION    : This module shows list of unapproved for AD API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def list_unapproved_operation(self):

                print '\n-----------------List Unapproved endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        response = requests.get('%s/%s/unapproved' %(variables.base_url, variables.url_path), verify=False, headers=headers)
                        status_code = response.status_code
                        print "\nResponse Status_code : %s" %status_code
                        print response.text
                        response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e


