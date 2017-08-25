import entity
from util.type_entity_enum import * 

class FunctionNode(entity.Entity):
	
	def __init__(self, name, fields=[], returns=[], function_calls=[]):
		Entity.__init__(name)
		self.type_entity = EntityTypeEnum.FUNCTION 
		self.fields = fields
		self.functions = functions 
		self.sub_class = sub_class
