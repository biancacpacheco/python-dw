import ast
from util import enum

class PythonDW:
    """Python Design Wizard API"""
    def __init__(self, ast_tree=[], ast_elements_dict=None):
		self.ast_tree = []
		self.ast_elements_dict = {"class":ast.ClassDef,"function":ast.FunctionDef}

    def parse(self, file_path):
		read_file = open(file_path,'r')
		self.ast_tree = ast.parse(read_file.read())

    def get_all_elements(self, key='class'):
		list_elements = []
		for node in ast.walk(self.ast_tree):
			if isinstance(node, self.ast_elements_dict[key]):
				list_elements.append(node.name)
		return list_elements							

    def get_all_classes(self):
        return self.get_all_elements('class') 

    def get_all_functions(self):
	    return self.get_all_elements('function')
	

