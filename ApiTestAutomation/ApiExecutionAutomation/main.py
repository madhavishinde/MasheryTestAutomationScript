#For handling exceptions
import sys
#For cmd line arguments
import getopt
#To disable warnings
import requests
#To disable warnings
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

        if instance_name == "production":
		variables.ConfigFile = __import__('lib.apis.ConfigFileProduction')
        elif instance_name == "staging":
		variables.ConfigFile = __import__('ConfigFileStaging')

        variables.base_url = variables.ConfigFile.base_url
        json_file_name = "InputJsonForUpload.txt"

        requests.packages.urllib3.disable_warnings()
        #This module does OAuth authentication and returns access token.
        fetch_token_operation()
	#This module uploads file and gives upload id
	upload_file_operation(json_file_name)

	print "\n\n************************ORGANIZATION API************************** \n"
	#This will create organization class object
	org_obj = organization()
	#This will call runner module of organization API class and runner will execute 
	#endpoints of organization.
	org_obj.runner()	

	print "\n\n************************AD API************************** \n"
	#This will create ad class object
	ad_obj = ad()
	#This will call runner module of ad API class and runner will execute
        #endpoints of ad.
        ad_obj.runner()

	print "\n\n************************ADSIZE API************************** \n"
	#This will create ad_size class object
	adsize_obj = ad_size()
	#This will call runner module of ad_size API class and runner will execute
        #endpoints of ad_size.
	adsize_obj.runner()

	print "\n\n************************AUDIENCES API************************** \n"
	#This will create audiences class object
	audiences_obj = audiences()
	#This will call runner module of audiences API class and runner will execute
        #endpoints of audiences.
	audiences_obj.runner()

	print "\n\n************************BIDDER API************************** \n"
	#This will create bidder class object
	bidder_obj = bidder()
	#This will call runner module of bidder API class and runner will execute
        #endpoints of bidder.
	bidder_obj.runner()

	print "\n\n************************ADTYPE API************************** \n"
	#This will create ad_type class object
	ad_type_obj = ad_type()
	#This will call runner module of ad_type API class and runner will execute
        #endpoints of ad_type.
	ad_type_obj.runner()

	print "\n\n************************AUGMENTOR API************************** \n"
	#This will create augmentor class object
	augmentor_obj = augmentor()
	#This will call runner module of augmentor API class and runner will execute
        #endpoints of augmentor.
	augmentor_obj.runner()

	print "\n\n************************USER API************************** \n"
	#This will create user class object
	user_obj = user()
	#This will call runner module of user API class and runner will execute
        #endpoints of user.
        user_obj.runner()

	print "\n\n************************CAMPAIGN API************************** \n"
	#This will create campaign class object
	campaign_obj = campaign()
	#This will call runner module of campaign API class and runner will execute
        #endpoints of campaign.
        campaign_obj.runner()

	print "\n\n************************TARGET API************************** \n"
	#This will create target class object
        target_obj = target()
	#This will call runner module of target API class and runner will execute
        #endpoints of target.
        target_obj.runner()

	#Finish time of program
        finish_time = time.time()

        print "\n--- Completion time : %s seconds--" % (finish_time - start_time)


if __name__ == '__main__':
        main(sys.argv[1:])

