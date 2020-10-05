

class URLException(Exception):
    '''
    Created on Oct 3, 2020
    
    @author: Sangeeta-Laptop
    '''
    
    
    def __init__(self, message_id):
        super().__init__(self.__get_message(message_id))


    def __get_message(self,message_id):
        
        if message_id == "APP_NAME_NF":  # App Name not found        
            return "Application name not found."
        
        