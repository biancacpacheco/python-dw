from util.type_relation_enum import *

class Relation:
	
	def __init__(self, caller, type_relation, called):
		self.caller = caller
		self.type_relation = type_relation
		self.called = called
		
	def get_caller(self):
		return self.caller
	
	def get_called(self):
		return self.called
	
	def get_type_relation(self):
		return self.type_relation
		
	def get_str_relation(self):
		return self.caller + " " + self.type_relation + " " + self.called
			
				
	
		
