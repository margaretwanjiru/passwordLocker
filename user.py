import string
import random

# Global varaibles
global users_list
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
        
    def delete_user(self):
        
        '''
        delete_user method deletes a saved user from the user_list
        '''
        Users.user_list.remove(self)
    @classmethod
    def user_exist(cls,name):
        '''
        method that checks if a user exists from the user_list
        
        Args:
            name: username to search if the person exists
        Returns:
        Boolean: true or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.user_name == name:
                return True
            
        return False
            
