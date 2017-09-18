from design.entity import Entity
from util.type_entity_enum import * 

class ClassNode(Entity):
	
    def __init__(self, name, ast_node, super_class=[], functions=[], \
     sub_class=[]):
        Entity.__init__(name, ast_node=ast_node)
        self.type_entity = EntityTypeEnum.CLASS
        self.super_class = super_class
        self.functions = functions 
        self.sub_class = sub_class
        
        if self.ast_node != {}:
            self.initialize_elements(super_class,functions,sub_class)
    
    def get_name(self):
        if self.ast_node == {}:
            self.name 
        return self.ast_node.name
        
    def initialize_elements(self,super_class,functions,sub_class):
        if super_class == []:
            self.initialize_super_class()
        if functions == []:
            self.initialize_functions()
        if sub_class == []:
            self.initialize_sub_class()  
            
    def initialize_super_class(self):
        bases = [base.id for base in ast_node.bases]
                          
        		
		
