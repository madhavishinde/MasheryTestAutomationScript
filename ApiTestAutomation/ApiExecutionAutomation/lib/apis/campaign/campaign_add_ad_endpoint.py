#from variables import * 
import requests
from .. import variables
import json

class campaign_add_ad_endpoint:

        ###############################################################
        #NAME OF MODULE : add_ad_operation
        #DESCRIPTION    : This module adds ad for Campaign API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def add_ad_operation(self):

                print '\n-----------------Add ad endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        if not variables.campaign_id:
                                print "No campaign id found.\nPlease first execute Create endpoint function to generate its id.\n"
                                #exit(0)
                        elif not variables.ad_id:
                                print "No ad id found.\nPlease first execute Create endpoint function to generate its id.\n"
                        else:
                                response = requests.post('%s/%s/%s/add_ad' %(variables.base_url, variables.url_path, variables.campaign_id), verify=False, headers=headers, data=json.dumps(variables.payload))
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e


