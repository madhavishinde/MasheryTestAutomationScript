#Builds OAuth2 client and send HTTP requests
from requests_oauthlib import OAuth2Session
#For converting string to dictionary
import ast
#For json operation
import json
#For handling exceptions
import sys
#Usign selenium
import seleniumLoginAutomation
import requests
import variables

###############################################################
#NAME OF MODULE : fetch_token_operation
#DESCRIPTION    : This module does OAuth authentication
#                 and gives access token required to
#                 process REST APIs of Rubicon
#INPUT          : self object used to give a reference to the
#                 current object.
#OUTPUT         : Access token
###############################################################

def fetch_token_operation():

        print '\n-----------------Authentication-----------------\n'
	#To disable verification of HTTPS requests
        #requests.packages.urllib3.disable_warnings()
        #print type(variables.ConfigFile)
        mashery = OAuth2Session(variables.ConfigFile.client_id, redirect_uri=variables.ConfigFile.redirect_uri)
        authorization_url, state = mashery.authorization_url(variables.ConfigFile.authorization_base_url)
        #Conversion between http and https is required because OAuth2.0 supports only
        #SSL connection (https) and Application uses http connection
        authorization_url = authorization_url.replace("https", "http", 1)
        print "Fetching access token...."
        #This function does login, selects grant type and returns redirected url containing access code
        redirect_response = seleniumLoginAutomation.login_automation(authorization_url)
        print '\nConfigFile.client_id : ' + variables.ConfigFile.client_id + '\nConfigFile.client_secret : ' + variables.ConfigFile.client_secret
        #redirect_response = raw_input('\nRedirect URL : ')
        redirect_response = redirect_response.replace("http", "https", 1)
        tokenStr = str(mashery.fetch_token(variables.ConfigFile.token_url, client_secret=variables.ConfigFile.client_secret,authorization_response=redirect_response, verify=False))
        tokenStr = ast.literal_eval(tokenStr)
        variables.token = tokenStr.get('access_token')
        if not variables.token:
                print "Error while fetching access token."
                exit(0)
        print "\nAccess token : " + variables.token
