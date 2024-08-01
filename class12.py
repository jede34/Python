from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        return value in self.data.values()
    
        
            
                