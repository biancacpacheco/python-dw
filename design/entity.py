from util.enum import * 
class Entity:
	
	def __init__(self, name):
		self.name = name
		self.type_entity = Enum.DEFAULT
		self.relations = {}
	
	def get_name(self):
		raise NotImplementedError("Not implemented yet.")
	
	def get_relations(self):
		raise NotImplementedError
	
	def get_relations_type(self, type_relation):
		raise NotImplementedError	
	
	def add_relation(self, relation):
		raise NotImplementedError
	
	def remove_relation(self, relation):
		raise NotImplementedError
	
	def contains_relation(self, relation):
		raise NotImplementedError					

