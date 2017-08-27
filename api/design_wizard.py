import ast
from util.type_entity_enum import EntityTypeEnum
from util.type_relation_enum import RelationTypeEnum
from design.relation.relation import Relation
from design.class_node import ClassNode
from design.function_node import FunctionNode 

class PythonDW:
    """Python Design Wizard API"""
    
    
    def __init__(self, ast_tree=[], ast_elements_dict=None):
        self.ast_tree = []
        self.entities = []
        self.ast_elements_dict = {"class":ast.ClassDef, \
         "function":ast.FunctionDef, \
         "import":ast.Import }
		 
    def parse(self, file_path):
        read_file = open(file_path,'r')
        self.ast_tree = ast.parse(read_file.read())
        
    def get_entity_attr_by_name(self,name):
        entity = ""
        for element in self.entities:
            if element.get_name() == name:
                entity = element
        return entity        
                    


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
   

    def get_class_by_name(self,name):
        class_found = []
        classes = self.get_all_classes()
        for clas in classes:
            if clas.name == name:
                class_found = clas
        return class_found        
    
    def get_function_by_name(self,name):
        function_found = []
        functions = self.get_all_functions()
        for func in functions:
            if func.name == name:
                function_found = func
        return function_found 
    
    def get_import_by_name(self,name):
        import_found = []
        imports = self.get_all_imports()
        for imp in imports:
            if imp.name == name:
                import_found = imp
        return import_found        


    def get_functions_inside_class(self, name):
        body,functions = [],[]
        classes = self.get_all_classes()
        for node in classes:
            if node.name == name:
                 body = node.body
        for node in body:
            if isinstance(node, self.ast_elements_dict['function']):
                functions.append(node)
        return functions		
					 
    def get_body_function(self, name):
        body = []
        functions = self.get_all_functions()
        for node in functions:
            if node.name == name:
                body = node.body
        return body			    

    def get_fields_function(self, name):
        fields,func_node = [],[]
        functions = self.get_all_functions()
        for node in functions:
            if node.name == name:
                func_node = node.args.args
        for element in func_node:
            fields.append(element)        
        return fields        

    def create_function_entity_by_name(self, name):
        function = self.get_function_by_name(name)        
        fields = self.get_fields_function(name)
        entity = FunctionNode(name,fields=fields)
        relation = ""
        for field in fields:
            name_of_field = ""
            try:
                name_of_field = field.arg
            except:
                name_of_field = field.id    
            
            relation = Relation(function,RelationTypeEnum.HASFIELD,field,function.name,name_of_field)
            entity.relations[name_of_field] = relation
        self.entities.append(entity)
        
                        

    # Returning strings functions 


    def get_all_classes_str(self):
        classes = [e.name for e in self.get_all_classes()]
        return classes 

    def get_all_functions_str(self):
        functions = [e.name for e in self.get_all_functions()]
        return functions
	
    def get_all_imports_str(self):
        imports = [e.name for e in self.get_all_imports()]
        return imports

    def get_functions_inside_class_str(self, name):
        functions = [e.name for e in self.get_functions_inside_class(name)]
        return functions

    # Handleling here with incompatible definitions of field through python versions
    def get_fields_function_str(self,name):
        fields = [] 
        for e in self.get_fields_function(name):
            try:
                fields.append(e.arg)
            except:
                fields.append(e.id)
        return fields		


    # Relation functions related


    #TODO(Caio) Major feature
    def add_relation(self):
        pass			

