import unittest # Importing the unittest module
from password import Users, Credentials # Importing the user and credential class

class TestUsers(unittest.TestCase):
    
    '''
    Test class that defines test cases for the user class behaviours.
    
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Users("MaggyIrungu", "teragram") # create new user
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"MaggyIrungu")
        self.assertEqual(self.new_user.password,"teragram")
        
            
        
class TestCredentials(unittest.TestCase):
    
    '''
    Test class that defines test cases for the credential behaviours.
    
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_credential = Credentials("MaggyIrungu", "Instagram", "MaggyIrungu", "teragram") # create credentials object
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.user_name,"MaggyIrungu")
        self.assertEqual(self.new_credential.account,"Instagram")
        self.assertEqual(self.new_credential.account_username,"MaggyIrungu")
        self.assertEqual(self.new_credential.account_password,"teragram")

if __name__== '__main__':
    unittest.main()        
        
    
    