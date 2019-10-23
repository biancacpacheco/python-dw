from util.type_entity_enum import * 

class Entity(object):
    
    def __init__(self, name, ast_node):
        self.name = name
        self.ast_node = ast_node
        self.type_entity = EntityTypeEnum.DEFAULT
        self.relations = {}

    def get_name(self):
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

    def get_ast_node(self):
        return self.ast_node
    
    def add_relation(self,relation):
        relation_type = relation.get_type_relation()
        value_dict = self.relations.get(relation_type)
        if value_dict is None:
            self.relations[relation_type] = [relation]
        else:
            relations_str = [e.get_str_relation() for e in \
             self.relations[relation_type]]
            if relation.get_str_relation() not in relations_str:
                self.relations[relation_type].append(relation)
