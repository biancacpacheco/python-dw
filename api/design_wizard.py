import ast
from util import enum

class PythonDW:
    """Python Design Wizard API"""
    
    global ONLY_ELEMENT_IN_LIST
    ONLY_ELEMENT_IN_LIST = 0
    
    def __init__(self, ast_tree=[], ast_elements_dict=None):
		self.ast_tree = []
		self.entities = []
		self.ast_elements_dict = {"class":ast.ClassDef, \
		 "function":ast.FunctionDef, \
		 "import":ast.Import }
		 
    def parse(self, file_path):
		read_file = open(file_path,'r')
		self.ast_tree = ast.parse(read_file.read())


    # Returning nodes functions 

    def get_all_elements_file(self, key='class'):
		list_elements = []
		for node in ast.walk(self.ast_tree):
			if isinstance(node, self.ast_elements_dict[key]):
				list_elements.append(node)
		return list_elements							

    def get_all_classes(self):
		return self.get_all_elements_file('class')
		
    def get_all_functions(self):
		return self.get_all_elements_file('function')

    def get_all_imports(self):
		all_imports = []
		imports = self.get_all_elements_file('import')
		for node in imports:
			for single_import in node.names:
				if single_import not in all_imports:
					all_imports.append(single_import)
		return all_imports							

    def get_functions_inside_class(self, name):
		body,functions = [],[]
		classes = self.get_all_classes()
		for node in classes:
			if node.name == name:
				body = node.body
		for node in body:
			if isinstance(node, self.ast_elements_dict['function']):
				functions.append(node.name)
		return functions		
					 
	
    def get_body_function(self, name):
		body = []
		functions = self.get_all_functions()
		for node in functions:
			if node.name == name:
				body = node.body
		return body			    


    # Returning strings functions 


    def get_all_classes_strings(self):
        classes = [e.name for e in self.get_all_classes()]
        return classes 

    def get_all_functions_strings(self):
        functions = [e.name for e in self.get_all_functions()]
        return functions
	

    def get_all_imports_strings(self):
        imports = [e.name for e in self.get_all_imports()]
        return imports


    """Relation functions related"""


    #TODO(Caio) Major feature
    def add_relation(self):
		pass			

