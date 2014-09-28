#r = requests.post('http://0.0.0.0/api/action/resource_create',
#              data={"package_id": "datasetfromap"},
#              headers={"X-CKAN-API-Key": "beb82c05-2581-4ba2-82d6-9a73dfdab64b"},
#              files=[('upload', file('/home/vagrant/scrpttst.txt'))])
import requests
import urllib2
import urllib
import json
import pprint

dataset_dict = {
    'name': 'testdataset_api',
    'notes': 'A long description of my dataset',
}
json_dict = urllib.quote(json.dumps(dataset_dict))
header_dict = {
        'Authorization': 'beb82c05-2581-4ba2-82d6-9a73dfdab64b',
        'Content-Type': 'application/x-www-form-urlencoded'
        }
d_url = 'http://0.0.0.0/api/action/package_create'
f = [('upload', file('/home/vagrant/scrpttst.txt'))]

r = requests.post(d_url, data=json_dict, headers=header_dict)
