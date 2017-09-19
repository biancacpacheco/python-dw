from design.entity import Entity
from util.type_entity_enum import EntityTypeEnum
from util.type_ast_entity_enum import AstEntityTypeEnum as ast_enum

class ClassNode(Entity):
	
    def __init__(self, name, ast_node, super_class=[], functions=[], \
     sub_class=[], initialize_elements=True):
        Entity.__init__(self, name=name, ast_node=ast_node)
        self.type_entity = EntityTypeEnum.CLASS
        self.super_class = super_class
        self.functions = functions 
        self.sub_class = sub_class
        
        if initialize_elements:
            self.initialize_elements(super_class,functions,sub_class)
    
    def get_name(self):
        if self.ast_node == {}:
            self.name 
        return self.ast_node.name
     
    #TODO(Caio) Needs tests
    def get_functions(self):
        return self.functions
    
    #TODO(Caio) ditto 23
    def get_sub_classes(self):
        return self.sub_class    
   
    #TODO(Caio) ditto 23
    def get_super_classes(self):
        return self.super_class
    
    #TODO(Caio) ditto 23
    def get_functions_str(self):
        functions_str = [e.name for e in self.functions]
        return functions_str    
    
    def set_name_to_ast_name(self):
        self.name = self.ast_node.name


    """ INITIALIZATION FUNCTIONS HERE """

         
    def initialize_elements(self,super_class,functions,sub_class):
        self.initialize_super_class()
        self.initialize_functions()
        self.initialize_sub_class()  
            
    def initialize_super_class(self):
        self.super_class = self.ast_node.bases
                          
    def initialize_sub_class(self):
        pass
        
    #TODO(Caio) Needs to create relation    
    def initialize_functions(self):
        self.functions = []
        body = self.ast_node.body
        for node in body:
            if isinstance(node, ast_enum.ast_entity_dict['function']):
                self.functions.append(node)        		
		
