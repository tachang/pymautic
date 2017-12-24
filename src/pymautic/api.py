import requests
from bs4 import BeautifulSoup
import base64
import logging

log = logging.getLogger(__name__)

VERBS = ["get","list","create","edit","delete"]

class MauticApi(object):

    def __init__(self, url, username, password):

        self.url = url
        self.username = username
        self.password = password
        
        mautic_basic = 'Basic %s' % base64.b64encode(username + ':' + password)
        self.headers = {'Authorization': mautic_basic}
        self.session = requests.Session()

    def remove_contact_from_segment(self, segment, contact):

        url = self.url + '/api/segments/{}/contact/{}/remove'.format(segment, contact)
        r = self.session.post(url, headers=self.headers)
        return r.json()

    def call_api(self, attrname):
        # The attrname is basically what the name of the method call is
        # So if you call MauticApi.get_segments the attrname is get_segments


        print attrname
        def custom_getattr(*args, **kwargs):

            if attrname.startswith("get_"):

                pieces = attrname.split("_")
                resource = pieces[1]

                url = self.url + '/api/{}/{}'.format(resource, *args)

                print url

                r = self.session.get(url, headers=self.headers)
                data = r.json()
            
                return data
            elif attrname.startswith("list_"):
                pieces = attrname.split("_")
                resource = pieces[1]

                url = self.url + '/api/{}'.format(resource)

                r = self.session.get(url, headers=self.headers)
                data = r.json()
                return data

            else:
                return None

        return custom_getattr

    # Reflection
    def __getattr__(self, attrname):
        self.data = None
        return self.call_api(attrname)