from design.entity import Entity
from util.type_entity_enum import EntityTypeEnum
from util.type_ast_entity_enum import AstEntityTypeEnum as ast_enum

class FieldNode(Entity):
	
    def __init__(self, name, ast_node, is_call=False):
        Entity.__init__(self, name=name, ast_node=ast_node)
        self.type_entity = EntityTypeEnum.FIELD
        self.is_call = is_call

    def get_name(self):
        return self.name        

    def set_name_to_ast_name(self):
        if is_call:
            self.name = self.ast_node.func.id
            
            
