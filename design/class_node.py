import entity

class ClassNode(entity.Entity):
	
	def __init__(self, name):
		Entity.__init__(name)
		self.type_entity = "CLASS" #TODO(Caio) Fix this as soon as possible
		self.fields = []
		self.methods = []
		self.sub_class = []
			
		
