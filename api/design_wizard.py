import ast
from util.type_entity_enum import EntityTypeEnum
from util.type_relation_enum import RelationTypeEnum
from util.type_ast_entity_enum import AstEntityTypeEnum
from design.relation.relation import Relation
from design.class_node import ClassNode
from design.function_node import FunctionNode 
from design.parameter_node import ParameterNode

class PythonDW:
    """Python Design Wizard API"""
    
    
    def __init__(self):
        self.ast_tree = []
        self.entities = {}
        self.ast_elements_dict = AstEntityTypeEnum.ast_entity_dict
		 
    def parse(self, file_path):
        read_file = open(file_path,'r')
        self.ast_tree = ast.parse(read_file.read())
        
    def get_entity_by_name(self,name):
        entity = self.entities.get(name)
        if entity is None:
            entity = ""
        return entity 
    
    #TODO(Caio) Needs to be tested
    def delete_entity_by_name(self, name):
        del self.entities[name]
        
    #TODO(Caio) ditto 29
    def delete_all_entities(self):
        self.entities = {}               
    


    """ Returning nodes functions """ 


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
    
    def create_class_entity(self, node):
        class_entity = ClassNode("temporary_name", ast_node=node)
        class_entity.set_name_to_ast_name()
        name = class_entity.get_name()
        self.entities[name] = class_entity
        

    #TODO(Caio) Tested but needs 'UpdateFunctionsCalls' method
    def create_function_entity(self, node):
        function_entity = FunctionNode\
         ("temporary_name", ast_node=node)
        function_entity.set_name_to_ast_name()
        name = function_entity.get_name() 
        self.entities[name] = function_entity
        calls = function_entity.get_function_calls_str(just_caller=True)
        for call in calls:
            if self.get_entity_by_name(call) != "":
                self.get_entity_by_name(call).add_callee(function_entity)

    #TODO(Caio) Code and test
    def update_function_calls(self):
        pass
   
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
    				 
    def create_function_entity_by_name(self, name):
        function_node = self.get_function_by_name(name)
        self.create_function_entity(function_node)

    def create_class_entity_by_name(self, name):
        class_node = self.get_class_by_name(name)
        self.create_class_entity(class_node)

    
    """ Returning strings functions """


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
 
