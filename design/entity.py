from util.enum import * 
class Entity:
	
	def __init__(self, name):
		self.name = name
		self.type_entity = Enum.DEFAULT
		self.relations = {}
	
	def get_name(self):
		raise NotImplementedError("Not implemented yet.")
	
	def get_relations(self):
		raise NotImplementedError("Not implemented yet.")
	
	def get_relations_type(self, type_relation):
		raise NotImplementedError("Not implemented yet.")	
	
	def add_relation(self, relation):
		raise NotImplementedError("Not implemented yet.")
	
	def remove_relation(self, relation):
		raise NotImplementedError("Not implemented yet.")
	
	def contains_relation(self, relation):
		raise NotImplementedError("Not implemented yet.")					

