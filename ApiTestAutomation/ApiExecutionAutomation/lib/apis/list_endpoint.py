import requests
import variables

class list_endpoint:

        #################################################################
        #NAME OF MODULE : list_operation
        #DESCRIPTION    : This module gives list of entities
        #                 specific to particular API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        #################################################################

        def list_operation(self):

                print '\n-----------------List endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        if "targets" in variables.url_path:
                                response = requests.get('%s/api/v1/campaigns/%s/targets' %(variables.base_url, variables.campaign_id), verify=False, headers=headers)
                        else:
                                response = requests.get('%s/%s' %(variables.base_url, variables.url_path), verify=False, headers=headers)
                        status_code = response.status_code
                        print "\nResponse status code : %s" %status_code
			if 200 == status_code or 204 == status_code:
                                variables.total_count += 1
                                variables.pass_count += 1
                        else:
                                variables.total_count += 1
                                variables.fail_count += 1
                        print response.text
                        response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

