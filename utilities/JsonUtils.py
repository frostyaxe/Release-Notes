'''
Created on Oct 3, 2020

@author: Sangeeta-Laptop
'''

from json import loads
class JsonUtils(object):
    
    def __init__(self):
        pass
    
    def convertStringToObject(self,jsonString : str) -> object:
        return loads(jsonString)
    
    
