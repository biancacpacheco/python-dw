from design import entity
from util.type_entity_enum import * 

class FunctionNode(entity.Entity):

    def __init__(self, name, fields=[], returns=[], function_calls=[]):
        entity.Entity.__init__(self,name=name)
        self.type_entity = EntityTypeEnum.FUNCTION 
        self.fields = fields
        self.returns = returns
        self.function_calls = function_calls
    
    def get_name(self):
        return self.name	
