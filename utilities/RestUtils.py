'''
Created on Oct 3, 2020

@author: Sangeeta-Laptop
'''

from urllib3 import PoolManager

class RestUtils(object):
    
    
    def __init__(self):
        self.__http = PoolManager()
        
    
    def basic_authentication(self : object, url, headers = None) -> object:
        
        '''
        Description :  This method returns the auth python object based on the request of a user.
        
        @author Abhishek Prajapati
        '''
        
        http =  PoolManager()
        
        resp = http.request('GET', url,headers=headers)
        
        return resp.headers.get('Set-Cookie')
    
    
    def get(self, url : str, headers = None):
      
        response = self.__http.request('GET', url, headers = headers)
        
        return response
    
    def post(self, url : str, headers = None):
      
        response = self.__http.request('POST', url, headers = headers)
        
        return response
