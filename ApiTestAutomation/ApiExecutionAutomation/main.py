#from ApiExecutionAutomation.runner.organization_execution import *
import sys
#For cmd line arguments
import getopt
#To disable warnings
import requests
import time
#from lib.apis.variables import *
from lib.apis import variables
from lib.apis.fetch_token import *
from lib.apis.upload_operation import *
from runner.organization import *
from runner.ad import *
from runner.ad_size import *
from runner.audiences import *
from runner.bidder import *
from runner.target import *
from runner.ad_type import *
from runner.augmentor import *
from runner.user import *
from runner.campaign import *

def main(argv):

	global ConfigFile
        #Start time of program
        start_time = time.time()

        instance_name = ""

        try:
                opts, args = getopt.getopt(argv,"hi:",["inst_name="])
        except getopt.GetoptError:
                print 'python main.py -i <instance_name>'
                sys.exit(2)
        for opt, arg in opts:
                if opt == '-h':
                        print 'python main.py -i <instance_name>'
                        sys.exit()
                elif opt in ("-i", "--inst_name"):
                         instance_name = arg
        #print 'Instance name is ', instance_name

        if instance_name == "production":
                #print "Inserting production values"
                #ConfigFile = __import__('ConfigFileProduction')
		variables.ConfigFile = __import__('lib.apis.ConfigFileProduction')
                #shutil.copyfile('ConfigFileProduction.py', 'ConfigFile.py')
                #shutil.copy2('ConfigFileProduction.py', 'ConfigFile.py')
        elif instance_name == "staging":
                #print "Inserting staging values"
                #ConfigFile = __import__('ConfigFileStaging')
		variables.ConfigFile = __import__('ConfigFileStaging')

	#print type(variables.ConfigFile)
	#print type(ConfigFile)
	#print ConfigFile.client_id
 	#print variables.ConfigFile.client_id
	#print variables.ConfigFile.base_url
        #url = ConfigFile.base_url
        variables.base_url = variables.ConfigFile.base_url
        #print variables.base_url
	#api = BaseClassApi.Api()
        json_file_name = "InputJsonForUpload.txt"

        #json_file_name = "abc.txt"

        requests.packages.urllib3.disable_warnings()
        #This module does OAuth authentication and returns access token.
        fetch_token_operation()
	upload_file_operation(json_file_name)

	print "\n************************ORGANIZATION API************************** \n"
	org_obj = organization()
	org_obj.runner()	

	print "\n************************AD API************************** \n"
	ad_obj = ad()
        ad_obj.runner()

	print "\n************************ADSIZE API************************** \n"
	adsize_obj = ad_size()
	adsize_obj.runner()

	print "\n************************AUDIENCES API************************** \n"
	audiences_obj = audiences()
	audiences_obj.runner()

	print "\n************************BIDDER API************************** \n"
	bidder_obj = bidder()
	bidder_obj.runner()

	print "\n************************ADTYPE API************************** \n"
	ad_type_obj = ad_type()
	ad_type_obj.runner()

	print "\n************************AUGMENTOR API************************** \n"
	augmentor_obj = augmentor()
	augmentor_obj.runner()

	print "\n************************USER API************************** \n"
	user_obj = user()
        user_obj.runner()

	print "campaign api"
	campaign_obj = campaign()
        campaign_obj.runner()

        target_obj = target()
        target_obj.runner()

	#Finish time of program
        finish_time = time.time()

        print "\n--- Completion time : %s seconds--" % (finish_time - start_time)


if __name__ == '__main__':
        main(sys.argv[1:])

