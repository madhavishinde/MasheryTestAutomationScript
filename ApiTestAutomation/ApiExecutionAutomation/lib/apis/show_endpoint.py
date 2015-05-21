#To disable warnings
import requests
#To access common variable
import variables

class show_endpoint:

        ##################################################################
        #NAME OF MODULE : show_operation
        #DESCRIPTION    : This module gives Details of entity
        #                 specific to particular API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ##################################################################

        def show_operation(self, general_id):

                print '\n-----------------Show endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        if not general_id:
                                print "No id found.\nPlease first execute Create endpoint Api to generate the id.\n"
                        else:
                                if "targets" in variables.url_path:
                                        response = requests.get('%s/api/v1/campaigns/%s/targets/%s' %(variables.base_url, variables.campaign_id, general_id), verify=False, headers=headers)
				elif "user" in variables.url_path:
					response = requests.get('%s/%s' %(variables.base_url, variables.url_path), verify=False, headers=headers)
                                else:
                                        response = requests.get('%s/%s/%s' %(variables.base_url, variables.url_path, general_id), verify=False, headers=headers)
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e



