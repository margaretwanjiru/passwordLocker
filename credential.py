import string
import random

class Credentials:
    """
    Class that generates new instances of user credentials
    """
    credential_list = [] #Empty credential list
    @classmethod
    def check_user(cls,user_name,password):
        '''
        method that checks if the credential entered matches entry in the user_list
        '''
        for user in Users.user-list:
            if(user.user_name == user_name and user.password == password):
                current_user = user.user_name
        return current_user
    def __init__(self, user_name, account, account_username, password):
    
        '''
        __init__ method that helps us define properties from our user credentials.
        '''
        self.user_name = user_name
        self.account = account
        self.account_username = account_username
        self.password = password
        
    def save_credential(self):
         
        '''
        saves the inputed credentials
        '''
        
        Credentials.credential_list.append(self)
    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate an 8 character password
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass
    
    @classmethod
    def display_credential(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
         
        
    @classmethod
    def find_by_username(cls,name):
        '''
        method that takes in a username and returns the user credentials that matches the username.
        
        Args:
            name: user name to search for credential
        Return :
            Credential of person that matches the username.    
        '''
        for credential in cls.credential_list:
            if credential.user_name == name:
                return credential
            
    def delete_credential(self):
        
        '''
        delete-credential method deletes a saved credential from the credential_list
        '''
        
        Credentials.credential_list.remove(self)
    
    @classmethod
    def credential_exist(cls,account_name):
        '''
        Method that checks if the credentials exist from the credential_list.
        
        Args:
           account-name: account_name to search if credentials exist
        Returns :
            Boolean: True or false depending if the credentials exist
        '''    
        for account in cls.credential_list:
            if account.account_username == account_name:
                return True
            
        return False