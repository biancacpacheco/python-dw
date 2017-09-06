from design.entity import Entity
from util.type_entity_enum import * 

class ClassNode(Entity):
	
    def __init__(self, name, raw_node, fields=[], functions=[], sub_class=[]):
        Entity.__init__(name)
        self.type_entity = EntityTypeEnum.CLASS
        self.raw_node = raw_node 
        self.fields = fields
        self.functions = functions 
        self.sub_class = sub_class
    
    def get_name(self):
        return self.name		
		
