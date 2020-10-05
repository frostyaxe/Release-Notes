'''
Created on Oct 3, 2020

@author: Sangeeta-Laptop
'''
from exceptions.URLException import URLException

class URLManager(object):
    
    def __init__(self):
        self.__jira_base_url = 'http://192.168.99.101:8080'
        self.__teamcity_base_url = 'http://192.168.99.100:8111'
        
    
    def get(self, app_name):
        
        if app_name.lower() == 'jira':
            return self.__jira_base_url
        elif app_name.lower() == 'teamcity':
            return self.__teamcity_base_url
        else:
            raise URLException("APP_NAME_NF")
            
        
    
    def set(self,app_name, url):
        
        if app_name.lower() == 'jira':
            self.__jira_base_url = url
        elif app_name.lower() == 'teamcity':
            self.__teamcity_base_url = url
        else:
            raise URLException("APP_NAME_NF")
    


    