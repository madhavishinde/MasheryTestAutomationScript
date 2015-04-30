#Builds OAuth2 client and send HTTP requests
from requests_oauthlib import OAuth2Session
#For converting string to dictionary
import ast
#For json operation
import json
#For handling exceptions
import sys
#To disable warnings
import requests
#To calculate time required to run program
import time
#to include credentials of oauth2.0
import ConfigFile
#To use login automation function
import seleniumLoginAutomation
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

def main():
	#Start time of program
	start_time = time.time()
	
	api = BaseClassApi.Api()
	json_file_name = "InputJsonForUpload.txt"
	
	#This module does OAuth authentication and returns access token.
	BaseClassApi.Api.token = api.fetch_token_operation()
	#This module uploads file i.e. json data and returns upload id.
	BaseClassApi.Api.upload_id = api.upload_file_operation(json_file_name)
	
	OrganizationApi.execute_organization_api()

	BidderApi.execute_bidder_api()

	AugmentorApi.execute_augmentor_api()

	TargetApi.execute_target_api()

	AudiencesApi.execute_audiences_api()

	AdtypeApi.execute_adtype_api()

	AdsizeApi.execute_adsize_api()

	UserApi.execute_user_api()

	CampaignApi.execute_campaign_api()

	AdApi.execute_ad_api()

	#Finish time of program
	finish_time = time.time()
	
	print "\n--- Completion time : %s seconds--" % (finish_time - start_time)


if __name__ == '__main__':
        main()
