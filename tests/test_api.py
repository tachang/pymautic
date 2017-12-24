import unittest
import logging
import pymautic
import os


MAUTIC_URL = os.getenv('MAUTIC_URL', 'https://mautic.example.com')
MAUTIC_USERNAME = os.getenv('MAUTIC_USERNAME', 'mautic@example.com') 
MAUTIC_PASSWORD = os.getenv('MAUTIC_PASSWORD', 'example')

MAUTIC_URL = 'https://mauticdev.literatorapp.com'
MAUTIC_USERNAME = 'mautic@literatorapp.com'
MAUTIC_PASSWORD = 'dTUqTB4vagev2S2g'

log = logging.getLogger(__name__)

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.api = pymautic.MauticApi(MAUTIC_URL, MAUTIC_USERNAME, MAUTIC_PASSWORD)


    def testListSegments(self):
        segments = self.api.list_segments()
        print segments

    def testGetSegment(self):
        response = self.api.get_segments(1)
        print response

    def testRemoveContactFromSegment(self):
        """
        POST /segments/SEGMENT_ID/contact/CONTACT_ID/remove
        """

        response = self.api.remove_contact_from_segment(segment=1, contact=1)
        print response

    def testDeleteRole(self):
        """
        DELETE /roles/ID/delete        
        """
        pass

    def testDeleteContact(self):
        """
        DELETE /contacts/ID/delete
        """
        pass




