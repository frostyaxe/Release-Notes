'''
Created on Oct 3, 2020

@author: Sangeeta-Laptop
'''
from services.teamcity.teamcity import Teamcity
from utilities.JsonUtils import JsonUtils
from datetime import datetime

class ReleaseNotesGenerator(object):
    
    def __init__(self):
        self.__teamcity_version_details_dict = {}
        self.__teamcity_service = Teamcity()
        self.__teamcity_auth_obj = self.__teamcity_service.authenticate('admin', 'admin')
        self.__jsonutils = JsonUtils()
        self.__teamcity_build_changes = {}
        self.__teamcity_changes_details = {}
    
    
    def fetch_all_build_versions_details(self):
        json_response_obj = self.__jsonutils.convertStringToObject(self.__teamcity_auth_obj.get_all_versions('ReleaseNotes_ReleaseNotesBuild'))
        if "build" in json_response_obj:
            for build_details in json_response_obj["build"]:
                if 'number' in build_details:
                    version_number = build_details['number']
                    build_id = []
                    if version_number in self.__teamcity_version_details_dict:
                        build_id = self.__teamcity_version_details_dict[version_number]
                        
                    build_id.append(build_details['id'])
                    self.__teamcity_version_details_dict[version_number] = build_id
                else:
                    pass
        else:
            pass
        
        
        return self.__teamcity_version_details_dict

    
    def get_change_ids(self, build_id):
        changes_response = self.__jsonutils.convertStringToObject(self.__teamcity_auth_obj.get_changes(build_id))
        change_ids = []
        if 'change' in changes_response:
            for change in changes_response['change']:
                change_ids.append(change['id'])
        else:
            pass 
        return change_ids
    
    def read_commit_details(self, change_id):
        
        data = {}
        change_details = self.__teamcity_auth_obj.get_commit_details(change_id)  
        data['author'] = self.__jsonutils.convertStringToObject(change_details)['username']
        data['date'] = self.__jsonutils.convertStringToObject(change_details)['date']
        # Validation for Jira Id existence in the comment is required
        comment = self.__jsonutils.convertStringToObject(change_details)['comment']
        data['jira_id'] = comment[comment.find('[')+1:comment.find(']')].strip()
        data['commit_message'] = comment[comment.find(']')+1:comment.find('(')].strip()
        self.__teamcity_changes_details[change_id] = data
       
        
        
    def generate(self):
        
        # Conditional versions logic will come here
        build_ids_dict = self.fetch_all_build_versions_details()
        
        for build_ids in build_ids_dict.values():
            for build_id in build_ids:
                self.__teamcity_build_changes[build_id] = self.get_change_ids(build_id)
                for change_id in self.get_change_ids(build_id):
                    self.read_commit_details(change_id)
                    
        self.__export_data_in_csv()
        
        
    def __export_data_in_csv(self):
        
        f = "%Y%m%dT%H%M%S" #%H:%M:%S.%fZ
        print("Build Version,Author,Jira ID,Commit Message","Date & Time")
        with open('release-notes.csv','a+') as file_obj:
            file_obj.write('Build Version,Author,Jira ID,Commit Message,Date & Time\n')
            for release_number, build_ids in self.__teamcity_version_details_dict.items():
                for build_id in build_ids:
                    for change_id in self.__teamcity_build_changes[build_id]:
                        print(release_number,self.__teamcity_changes_details[change_id]['author'],self.__teamcity_changes_details[change_id]['jira_id'],self.__teamcity_changes_details[change_id]['commit_message'],datetime.strptime(self.__teamcity_changes_details[change_id]['date'][:self.__teamcity_changes_details[change_id]['date'].find('+')], f),sep=',')
                        file_obj.write(release_number + ',' + self.__teamcity_changes_details[change_id]['author']+ ',' +self.__teamcity_changes_details[change_id]['jira_id'] + ',' +self.__teamcity_changes_details[change_id]['commit_message']+ ',' + str(datetime.strptime(self.__teamcity_changes_details[change_id]['date'][:self.__teamcity_changes_details[change_id]['date'].find('+')], f))+'\n')
            
    
ReleaseNotesGenerator().generate() 
        
        
        