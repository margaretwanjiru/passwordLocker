class Users:
    """
    Class that generates new instances of users
    """
    user_list = [] #Empty user list

    def __init__(self,user_name,password):
    
        '''
        __init__ method that helps us define properties for our users.
        '''
        self.user_name = user_name
        self.password = password
    
    def save_user(self):
            
        '''
        save_user method saves user objects into user_list
        '''
            
        Users.user_list.append(self)
    
class Credentials:
    """
    Class that generates new instances of user credentials
    """
    credential_list = [] #Empty credential list
    
    def __init__(self, user_name, account, account_username, account_password):
    
        '''
        __init__ method that helps us define properties from our user credentials.
        '''
        self.user_name = user_name
        self.account = account
        self.account_username = account_username
        self.account_password = account_password
        
    def save_credential(self):
         
        '''
        saves the inputed credentials
        '''
        
        Credentials.credential_list.append(self)
    
    
    