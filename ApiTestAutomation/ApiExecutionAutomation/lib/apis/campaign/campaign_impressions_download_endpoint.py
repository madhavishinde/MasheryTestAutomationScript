import requests
from .. import variables

class campaign_impressions_download_endpoint:


        ###############################################################
        #NAME OF MODULE : impressions_download_operation
        #DESCRIPTION    : This module downloads impressions for Campaign API
        #INPUT          : self object used to give a reference to the
        #                 current object.
        #OUTPUT         : NA
        ###############################################################

        def impressions_download_operation(self):

                print '\n-----------------Impressions Download endpoint-----------------\n'
                requests.packages.urllib3.disable_warnings()
                headers = {'Accept': 'application/json', 'Content-type': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
                try:
                        if not variables.campaign_id:
                                print "No campaign id found.\nPlease first execute Create endpoint function to generate its id.\n"
                        else:
                                response = requests.get('%s/%s/%s/impressions' %(variables.base_url, variables.url_path, variables.campaign_id), verify=False, headers=headers)
                                status_code = response.status_code
                                print "\nResponse Status_code : %s" %status_code
                                print response.text
                                response.raise_for_status()
                except requests.HTTPError, e:
                        print 'HTTP ERROR.'
                        print e

