import unittest2
import datetime

from google.appengine.ext import testbed

from datafeeds.datafeed_usfirst2 import DatafeedUsfirst2

class TestDatafeedFmsTeams(unittest2.TestCase):
    
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_urlfetch_stub()
        
        self.datafeed = DatafeedUsfirst2()
    
    def tearDown(self):
        self.testbed.deactivate()
    
    def test_getFmsTeamList(self):
        teams = self.datafeed.getFmsTeamList()
        self.find177(teams)
    
    def find177(self, teams):
        found_177 = False
        for team in teams:
            if team.team_number == 177:
                found_177 = True
                self.assertEqual(team.name, "UTC Power/Ensign Bickford Aerospace & Defense & South Windsor High School")
                self.assertEqual(team.address, u"South Windsor, CT, USA")
                self.assertEqual(team.nickname, "Bobcat Robotics")
        
        self.assertTrue(found_177)
        self.assertTrue(len(teams) > 0)

