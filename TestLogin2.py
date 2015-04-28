import requests
url = 'http://dspbuilder.rubiconproject.com/login?response_type=code&client_id=zfupgaj4k7ashk2wx635zptm&redirect_uri=http%3A%2F%2Frubiconproject.mashery.com%2Fio-docs%2Foauth2callback&state=8QjwcARDDNDGkUgr9rfQ25aFL3hz99'
values = {'username': 'mchowla@rubiconproject.com',
          'password': 'Mike2015!'}

#r = requests.post(url, data=values,allow_redirects=True)
r = requests.post('http://dspbuilder.rubiconproject.com/login', auth=('mchowla@rubiconproject.com', 'Mike2015!'))
print r.status_code
print r.history

url = 'http://dspbuilder.rubiconproject.com/switch-organization'
r = requests.get(url,allow_redirects=True)
#print r.content
print r.status_code
print r.history
