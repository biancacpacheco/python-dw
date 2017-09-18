from design import entity
from util.type_entity_enum import * 
from util.type_ast_entity_enum import AstEntityTypeEnum as ast_enum

class FunctionNode(entity.Entity):

    def __init__(self, name, ast_node, parameters=[], fields=[], \
     returns=[], function_calls={}):
        entity.Entity.__init__(self,name=name,ast_node=ast_node)
        self.type_entity = EntityTypeEnum.FUNCTION
        self.parameters = parameters 
        self.fields = fields
        self.returns = returns
        self.function_calls = function_calls
        
        if ast_node != {}:
            self.initialize_elements\
             (parameters,fields,returns,function_calls)


    """ ACCSSES AND CONTROL OF THE NODE ATTRIBUTES"""
    
    def get_name(self):
        if self.ast_node == {}:
            return self.name
        return self.ast_node.name 	
    
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
         caller_str = [e.func.id for e in function_calls_caller]
         callee_str = [e.func.id for e in function_calls_callee] 
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
                      

    def add_relation(self,relation):
        relation_type = relation.get_type_relation()
        value_dict = self.relations.get(relation_type)
        if value_dict is None:
            self.relations[relation_type] = [relation]
        else:
            self.relations[relation_type].append(relation)

                
    """ INITIALIZATION FUNCTIONS HERE """
    
    def initialize_elements\
     (self,parameters,fields,returns,function_calls):
         if parameters == []: 
             self.initialize_parameters()
         if fields == []:
             self.initialize_fields()
         if returns == []:
             self.initialize_returns()
         if function_calls == {}:
             self.initialize_function_calls()
    
    def initialize_parameters(self):
        self.parameters = self.ast_node.args.args
    
    def initialize_fields(self):
        self.fields = self.ast_node.body
    
    def initialize_returns(self):
        pass

    def initialize_function_calls(self):
        calls = []
        body = self.ast_node.body
        for node in body:
            if isinstance(node, ast_enum.ast_entity_dict["expr"]) and \
             isinstance(node.value, ast_enum.ast_entity_dict["call"]):
                calls.append(node.value)
        self.function_calls['caller'] = calls
        self.function_calls['callee'] = []                     
        
           
   
                         


