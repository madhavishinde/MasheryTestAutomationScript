#To disable warnings
import requests
#To access common variables
import variables

class new_endpoint:


        ###############################################################
        #NAME OF MODULE : new_operation
        #DESCRIPTION    : This module details for specific API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ##############################################################

        def new_operation(self):

                print '\n-----------------New endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        response = requests.get('%s/%s/new' %(variables.base_url, variables.url_path), verify=False, headers=headers)
                        status_code = response.status_code
                        print "\nResponse Status_code : %s" %status_code
                        print response.text
                        response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

