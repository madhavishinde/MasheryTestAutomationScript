#from variables import * 
import requests
import variables

class destroy_endpoint:

        ###############################################################
        #NAME OF MODULE : destroy_operation
        #DESCRIPTION    : This module deletes entity for specific API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ##############################################################

        def destroy_operation(self, general_id):

                print '\n-----------------Destroy endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        if not general_id:
                                print "No id found to destroy.\nPlease first execute Create endpoint function to generate id.\n"
                                #exit(0)
                        else:
                                if "targets" in variables.url_path:
                                        #Api.url_path = "/api/v1/campaigns"
                                        response = requests.delete('%s/api/v1/campaigns/%s/targets/%s' %(variables.base_url, variables.campaign_id, general_id), verify=False, headers=headers)
                                else:
                                        response = requests.delete('%s/%s/%s' %(variables.base_url, variables.url_path, general_id), verify=False, headers=headers)
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                #print response.text
                                if response.status_code == 204 :
                                        print "Deleted successfully"
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e


