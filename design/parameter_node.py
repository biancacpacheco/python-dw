from design import entity
from util.type_entity_enum import * 

class ParameterNode(entity.Entity):

    def __init__(self, name, ast_node):
        entity.Entity.__init__(self,name=name,ast_node=ast_node)
        self.type_entity = EntityTypeEnum.PARAMETER

    
    def get_name(self):
        if self.ast_node == {}:
            return self.name
        
        node_name = ""
        try:
            node_name = self.ast_node.arg
        except:
            node_name = self.ast_node.id
            
        return node_name	

    def set_name_to_ast_name(self):
        try:
            self.name = self.ast_node.arg
        except:
            self.name = self.ast_node.id
            
    def add_relation(self,relation):
        relation_type = relation.get_type_relation()
        value_dict = self.relations.get(relation_type)
        if value_dict is None:
            self.relations[relation_type] = [relation]
        else:
            self.relations[relation_type].append(relation)
                
