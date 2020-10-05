'''
Created on Oct 3, 2020

@author: Sangeeta-Laptop
'''
from support.SessionManager import SessionManager
from support.url_manager import URLManager
from utilities.RestUtils import RestUtils

class Teamcity(object):
    
    def __init__(self):
        self.__url_manager = URLManager()
        self.__session_manager = SessionManager()
        self.__restutil = RestUtils()
        self.__builds_by_type_path = '/app/rest/builds/?locator=buildType:'
    
    
    
    
    def authenticate(self,username, password):
        self.__session_manager.set_teamcity_username(username)
        self.__session_manager.set_teamcity_password(password)
        self.__session_manager.teamcity_session()
        self.__default_headers = { "Accept": "application/json", "Content-Type": "application/json", "Cookie" : str(self.__session_manager.get_teamcity_session()) }
        return self
    
    def get_changes(self, build_id):
        path = '/app/rest/changes?locator=build:(id:'+str(build_id)+')'
        return self.__get(path)
    
    def get_last_successful_build(self, build_config_id):
        return self.__get(self.__builds_by_type_path + str(build_config_id)+',status:SUCCESS,count:1')
    
    def get_last_build(self,build_config_id):
        return self.__get(self.__builds_by_type_path + str(build_config_id)+',count:1')
    
    def get_all_versions(self, build_config_id):
        return self.__get(self.__builds_by_type_path + str(build_config_id))
    
    def get_commit_details(self, change_id):
        return self.__get('/app/rest/changes/id:' + str(change_id))
    
    def __get(self, path):
        base_url = self.__url_manager.get("teamcity")
        url = base_url+path
        return str(self.__restutil.get(url, self.__default_headers).data.decode('utf-8'))
            
        