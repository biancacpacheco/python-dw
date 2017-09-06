from util.type_entity_enum import * 

class Entity:
    
    def __init__(self, name, ast_node):
        self.name = name
        self.ast_node = ast_node
        self.type_entity = EntityTypeEnum.DEFAULT
        self.relations = {}

    def get_name(self):
        raise NotImplementedError("Not implemented yet.")
	
    def get_ast_node(self):
        raise NotImplementedError("Not implemented yet.")
    
    def get_relations(self):
        raise NotImplementedError("Not implemented yet.")
        
    def get_relations_by_type(self, type_relation):
        raise NotImplementedError("Not implemented yet.")
    
    def set_name_to_ast_name(self):
        raise NotImplementedError("Not implemented yet.")    	
	
    def add_relation(self, relation):
        raise NotImplementedError("Not implemented yet.")
	
    def remove_relation(self, relation):
        raise NotImplementedError("Not implemented yet.")
	
    def contains_relation(self, relation):
        raise NotImplementedError("Not implemented yet.")					

