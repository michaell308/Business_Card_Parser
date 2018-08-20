from BusinessCardParser import BusinessCardParser
import sys
import unittest


test1 = '''Entegra Systems
John Doe
Senior Software Engineer
(410)555-1234
john.doe@entegrasystems.com'''

test2='''Acme Technologies
Analytic Developer
Jane Doe
1234 Roadrunner Way
Columbia, MD 12345
Phone: 410-555-1234
Fax: 410-555-4321
jane.doe@acmetech.com'''

test3='''Bob Smith
Software Engineer
Decision & Security Technologies
ABC Technologies
123 North 11th Street
Suite 229
Arlington, VA 22209
Tel: +1 (703) 555-1259
Fax: +1 (703) 555-1200
bsmith@abctech.com'''

test4='''Smith Technologies
Rob James Smith
Software Engineer
(410) - 555 - 1234
rsmith@smithtech.com'''

class TestBCP(unittest.TestCase):
	def test1(self):
		res = BusinessCardParser.getContactInfo(test1)
		self.assertEqual(res.getName(),"John Doe")
		self.assertEqual(res.getPhoneNumber(),"4105551234")
		self.assertEqual(res.getEmailAddress(),"john.doe@entegrasystems.com")
	def test2(self):
		res = BusinessCardParser.getContactInfo(test2)
		self.assertEqual(res.getName(),"Jane Doe")
		self.assertEqual(res.getPhoneNumber(),"4105551234")
		self.assertEqual(res.getEmailAddress(),"jane.doe@acmetech.com")
	def test3(self):
		res = BusinessCardParser.getContactInfo(test3)
		self.assertEqual(res.getName(),"Bob Smith")
		self.assertEqual(res.getPhoneNumber(),"17035551259")
		self.assertEqual(res.getEmailAddress(),"bsmith@abctech.com")
	def test4(self):
		res = BusinessCardParser.getContactInfo(test4)
		self.assertEqual(res.getName(),"Rob James Smith")
		self.assertEqual(res.getPhoneNumber(),"4105551234")
		self.assertEqual(res.getEmailAddress(),"rsmith@smithtech.com")



if __name__ == '__main__':
	unittest.main()