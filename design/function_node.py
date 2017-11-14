from design import entity
from util.type_entity_enum import EntityTypeEnum
from util.type_relation_enum import RelationTypeEnum 
from util.type_ast_entity_enum import AstEntityTypeEnum as ast_enum
from util.type_ast_entity_enum import Print
from design.parameter_node import ParameterNode
from design.field_node import FieldNode
from design.relation.relation import Relation

class FunctionNode(entity.Entity):
    
    
    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get("__it__")
        cls.__it__ = it = object.__new__(cls)
        it.__init__(*args, **kwds)
        return it

    def __init__(self, name, ast_node, parameters=[], fields=[], \
     returns=[], function_calls={}, initialize_elements=True):
        entity.Entity.__init__(self,name=name,ast_node=ast_node)
        self.type_entity = EntityTypeEnum.FUNCTION
        self.parameters = parameters 
        self.fields = fields
        self.returns = returns
        self.function_calls = function_calls
        
        if initialize_elements:
            self.initialize_elements()


    """ ACCSSES AND CONTROL OF THE NODE ATTRIBUTES"""
    
    def get_name(self):
        if self.ast_node == {}:
            return self.name
        return self.ast_node.name 	
        
    def get_function_fields_body(self):
        return self.ast_node.body    
    
    def get_function_calls(self,just_caller=False,just_callee=False):
        calls = self.function_calls
        if just_caller and just_callee:
            just_caller,just_callee = False,False
        if just_caller:
            calls = calls['caller']
        elif just_callee:
            calls = calls['callee']
        else:
            calls = [(k, v) for k, v in calls.items()]         
        return calls     
            
    def get_relations_by_type(self, type_relation):
        return self.relations[type_relation]
 
    def get_parameters_function(self): 
        return self.parameters
   
    def get_parameters_function_str(self):
        parameters = [] 
        for e in self.get_parameters_function():
            try:
                parameters.append(e.arg)
            except:
                parameters.append(e.id)
        return parameters
    
    def get_function_calls_str\
     (self,just_caller=False,just_callee=False):
         calls_str = []
         function_calls_caller = self.get_function_calls\
          (just_caller=True,just_callee=False)
         function_calls_callee = self.get_function_calls\
          (just_caller=False,just_callee=True)
         
         caller_str = [e.name for e in function_calls_caller]
         callee_str = [e.name for e in function_calls_callee] 
         
         # If both are False or both are True
         if (not (just_caller or just_callee)) or \
           (just_caller and just_callee):
               caller = ('caller',caller_str)
               callee = ('callee',callee_str)
               calls_str = [caller,callee]
         elif just_caller:
             calls_str = caller_str
         else:
             calls_str = callee_str
         
         return calls_str  

    def set_name_to_ast_name(self):
        self.name = self.ast_node.name
         
    def add_callee(self, callee):
        if callee not in self.function_calls['callee']:
            self.function_calls['callee'].append(callee)
            relation = Relation(self, RelationTypeEnum.ISCALLED, callee)
            self.add_relation(relation)
            
    def add_relation(self,relation):
        relation_type = relation.get_type_relation()
        value_dict = self.relations.get(relation_type)
        if value_dict is None:
            self.relations[relation_type] = [relation]
        else:
            if relation not in self.relations[relation_type]:
                self.relations[relation_type].append(relation)


                
    """ INITIALIZATION FUNCTIONS HERE """
    
    def initialize_elements(self):
         self.initialize_parameters()
         self.initialize_fields()
         self.initialize_returns()
         self.initialize_function_calls()
    
    def initialize_parameters(self):
        self.parameters = self.ast_node.args.args
        relation = ""
        for parameter in self.parameters:
            parameter_entity = ParameterNode\
             ("temporary_name", ast_node=parameter)
            parameter_entity.set_name_to_ast_name()
            relation = Relation\
             (self,RelationTypeEnum.HASFIELD,parameter_entity)
            self.add_relation(relation)
    
    def initialize_fields(self):
        self.fields = self.ast_node.body
    
    def initialize_returns(self):
        pass

    def initialize_function_calls(self):
        self.function_calls = {"caller":[],"callee":[]}
        calls = []
        body = self.ast_node.body
        print_type = ast_enum.ast_entity_dict.get("print")
        for node in body:
            if isinstance\
             (node, ast_enum.ast_entity_dict["expression"]) and \
             isinstance\
             (node.value, ast_enum.ast_entity_dict["call"]):
                 calls.append(node.value)
            elif print_type is not None and isinstance\
             (node, print_type):
                print_instance = Print()
                calls.append(print_instance)
                
        caller_calls = []
        for call in calls:
            is_attribute = False
            call_name = ""
            if isinstance(call.func, ast_enum.ast_entity_dict["attribute"]):
                call_name = call.func.attr
                is_attribute = True
            else:
                call_name = call.func.id
            field = FieldNode\
             (call_name, ast_node=call, is_call=True, is_attribute=is_attribute)
            relation = Relation(self, RelationTypeEnum.CALLS, field)
            self.add_relation(relation)
            caller_calls.append(field)                     

           
        self.function_calls['caller'] = caller_calls
        self.function_calls['callee'] = []
           
                         


