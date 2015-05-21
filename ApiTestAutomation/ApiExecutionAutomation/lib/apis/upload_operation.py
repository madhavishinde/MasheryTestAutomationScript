import requests
import variables
import ast

####################################################################
#NAME OF MODULE : upload_file_operation
#DESCRIPTION    : This module uploads json file and image file to
#                 database
#INPUT          : self object used to give a reference to the current
#                 object,json_file_name i.e. name of file containing
#                 json data for upload api
#OUTPUT         : NA
####################################################################

def upload_file_operation(json_file_name):

	print '\n-----------------Upload File operation-----------------\n'
        headers = {'Accept': 'application/json', 'Authorization': 'Bearer %s' %variables.token}
        files = {'file': open(json_file_name, 'rb')}
        try:
        	response = requests.post('%s/api/v1/uploadfile' %(variables.base_url), verify=False, headers=headers, files=files)
                status_code = response.status_code
                print "\nResponse Status_code : %s" %status_code
                response_str = response.text
                print response_str
                if response.status_code == requests.codes.ok :
                	response_str = str(response.text)
                        response_str = ast.literal_eval(response_str)
                        variables.upload_id = response_str.get('id')
                response.raise_for_status()
        except requests.HTTPError, e:
                print 'HTTP ERROR.'
		print e

