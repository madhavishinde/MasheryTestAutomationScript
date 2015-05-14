#Builds OAuth2 client and send HTTP requests
from requests_oauthlib import OAuth2Session
#For converting string to dictionary
import ast
#For json operation
import json
#For handling exceptions
import sys
#For cmd line arguments
import getopt
#To disable warnings
import requests
#To calculate time required to run program
import time
#to include credentials of oauth2.0
#import ConfigFileProduction
#import ConfigFileStaging
import ConfigFile
#To use login automation function
#import seleniumLoginAutomation
#Includes BaseClassApi class
import BaseClassApi
#Includes OrganizationApi class
import OrganizationApi
#Includes BidderApi class
import BidderApi
#Includes AugmentorApi class
import AugmentorApi	
#Includes AugmentorApi class
import TargetApi
#Includes AudiencesApi class
import AudiencesApi
#Includes AdtypeApi class
import AdtypeApi
#Includes AdsizeApi class
import AdsizeApi
#Includes UserApi class
import UserApi
#Includes CampaignApi class
import CampaignApi
#Includes AdApi class
import AdApi
#To copy file
import shutil

def main(argv):
	#Start time of program
	start_time = time.time()
	
	instance_name = ""

	try:
      		opts, args = getopt.getopt(argv,"hi:",["inst_name="])
	except getopt.GetoptError:
	      	print 'python ApiTestAutomation.py -i <instance_name>'
      		sys.exit(2)
	for opt, arg in opts:
	      	if opt == '-h':
			print 'python ApiTestAutomation.py -i <instance_name>'
         		sys.exit()
      		elif opt in ("-i", "--inst_name"):
		         instance_name = arg
	print 'Instance name is ', instance_name
	
	if instance_name == "production":
		print "Inserting production values"
		shutil.copyfile('ConfigFileProduction.py', 'ConfigFile.py')
		#shutil.copy2('ConfigFileProduction.py', 'ConfigFile.py')
	elif instance_name == "staging":
		print "Inserting staging values"
		shutil.copyfile('ConfigFileStaging.py', 'ConfigFile.py')
		#shutil.copy2('ConfigFileStaging.py', 'ConfigFile.py')

	print ConfigFile.base_url
	#url = ConfigFile.base_url
	BaseClassApi.Api.base_url = ConfigFile.base_url	
	print BaseClassApi.Api.base_url
	api = BaseClassApi.Api()
	json_file_name = "InputJsonForUpload.txt"
	
	#json_file_name = "abc.txt"

	requests.packages.urllib3.disable_warnings()
	#This module does OAuth authentication and returns access token.
	api.fetch_token_operation()
	#BaseClassApi.Api.token = "wje2tqpvdynk2unve89nc23s"
	#This module uploads file i.e. json data and returns upload id.
	#BaseClassApi.Api.upload_id = api.upload_file_operation(json_file_name)
	#BaseClassApi.Api.upload_id = "5549b2ff70726f7675010000"
	
	#OrganizationApi.execute_organization_api()

	#BidderApi.execute_bidder_api()

	#AugmentorApi.execute_augmentor_api()

	#TargetApi.execute_target_api()

	#AudiencesApi.execute_audiences_api()

	#AdtypeApi.execute_adtype_api()

	#AdsizeApi.execute_adsize_api()

	#UserApi.execute_user_api()

	#AdApi.execute_ad_api()

	#BaseClassApi.Api.ad_id = "5549b32270726f7675020000"

	#CampaignApi.execute_campaign_api()

	#Finish time of program
	finish_time = time.time()
	
	print "\n--- Completion time : %s seconds--" % (finish_time - start_time)


if __name__ == '__main__':
        main(sys.argv[1:])
