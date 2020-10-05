'''
Created on Oct 3, 2020

@author: Sangeeta-Laptop
'''
from support.url_manager import URLManager
from utilities.RestUtils import RestUtils
from urllib3 import make_headers

class SessionManager:
    
    
    def __init__(self):
        
        self.__teamcity_username = None
        self.__teamcity_password = None
        self.__jira_username = None
        self.__jira_password = None
        self.__teamcity_cookie = None
        self.__jira_cookie = None
        self.__url_manager = URLManager()
        self.__rest_util = RestUtils()
    
    
    '''
    
        Setters for setting up the data related to the user's credentials
    
    '''    
        
    def set_teamcity_username(self , username : str) -> object:
        self.__teamcity_username = username
        return self
    
    def set_teamcity_password(self, password : str) -> object:
        self.__teamcity_password = password
        return self
    
    def set_jira_username(self, username : str) -> object:
        self.__jira_username = username
        return self
    
    def set_jira_password(self, password : str) -> object:
        self.__jira_password = password
        return self
    
    
    
    
    '''
    
        Functions to be used for the management of sessions for the various applications
    
    '''
               
       
   
    def teamcity_session(self):
        BASE_URL = self.__url_manager.get("teamcity")
        headers = make_headers(basic_auth= self.__teamcity_username + ':' + self.__teamcity_password)
        if( self.__teamcity_cookie is None):
            self.__teamcity_cookie = self.__rest_util.basic_authentication(BASE_URL, headers)
    
    
    def get_teamcity_session(self):
        return self.__teamcity_cookie
    
    
    def jira_session(self):
        pass
        
    
    def get_jira_session(self):
        pass
    
    
