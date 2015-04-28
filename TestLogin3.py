import requests
import sys
#import urllib3

EMAIL = ''
PASSWORD = ''

#URL = 'https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1'
URL = 'http://dspbuilder.rubiconproject.com/login?response_type=code&client_id=zfupgaj4k7ashk2wx635zptm&redirect_uri=http%3A%2F%2Frubiconproject.mashery.com%2Fio-docs%2Foauth2callback&state=8QjwcARDDNDGkUgr9rfQ25aFL3hz99'


def main():

	requests.packages.urllib3.disable_warnings()
    	# Start a session so we can have persistant cookies
	session = requests.session()# config={'verbose': sys.stderr})
	
   	 # This is the form data that the page sends when logging in
	#    login_data = {
	#        'loginemail': 'mchowla@rubiconproject.com',
	#        'loginpswd': 'Mike2015!',
	#        'submit': 'login',
	#    }
	"""

	    login_data = {
        	'user[email]': 'madhavi.shinde@gslab.com',
	        'user[password]': 'pp@gslab23',
        	'commit': 'Sign In'
	    }
	

	# Authenticate
	r = session.post(URL, data=login_data, verify=False) # , config={'verbose': sys.stderr})

	print r.status_code
	print r.history
	print r.url

	# Try accessing a page that requires you to be logged in
	r = session.get('http://dspbuilder.rubiconproject.com/switch-organization', verify=False) # , config={'verbose': sys.stderr})
	#r = session.get('https://mail.google.com/mail/u/0/?pli=1#inbox/14cfec94c6741669', verify=False)
	#print r.text
	print r.status_code
	print r.history
	print r.url

	login_data = {
	       'organization': 'Rename organization'
	
	"""
	login_data = {
		'user[email]': 'mchowla@rubiconproject.com',
		'user[password]': 'Mike2015!',
		'commit': 'Sign In',
		'organization': 'Rename organization'
	}


	r = session.post(URL, verify=False, data=login_data) # , config={'verbose': sys.stderr})
    	#r = session.get('https://mail.google.com/mail/u/0/?pli=1#inbox/14cfec94c6741669', verify=False)
    	#print r.text
    	print r.status_code
    	print r.history
    	print r.url



if __name__ == '__main__':
    main()
