import entity

class ClassNode(entity.Entity):
	
	def __init__(self, name, fields=[], functions=[], sub_class=[]):
		Entity.__init__(name)
		self.type_entity = "CLASS" #TODO(Caio) Fix this as soon as possible
		self.fields = fields
		self.functions = functions 
		self.sub_class = sub_class
			
		
