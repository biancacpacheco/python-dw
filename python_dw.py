import ast

class PythonDW:
    """Python Design Wizard API"""
    def __init__(self, ast_tree=[], ast_elements_dict=None):
		self.ast_tree = []
		self.ast_elements_dict = {"class":ast.ClassDef,"function":ast.FunctionDef}

    def parse(self, file_path):
		read_file = open(file_path,'r')
		self.ast_tree = ast.parse(read_file.read())

    def get_all_elements(self, key='class'):
		for node in ast.walk(self.ast_tree):
			if isinstance(node, self.ast_elements_dict[key]):
				print node.name,					

    def get_all_classes(self):
        self.get_all_elements('class') 

    def get_all_functions(self):
		self.get_all_elements('function')
	

