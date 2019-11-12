from util.type_relation_enum import *

class Relation:
    
    def __init__(self, caller, type_relation, callee):
        self.caller = caller
        self.type_relation = type_relation
        self.callee = callee
    
    def get_caller(self):
        return self.caller
    
    def get_callee(self):
        return self.callee
        
    def get_type_relation(self):
        return self.type_relation

    def get_caller_str(self):
        return self.caller.get_name()
    
    def get_callee_str(self):
        return self.callee.get_name()    

    def get_str_relation(self):
        return self.caller.get_name() + \
         " " + self.type_relation + " " + self.callee.get_name()
