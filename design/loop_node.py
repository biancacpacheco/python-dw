from design import entity
from util.type_entity_enum import EntityTypeEnum
from util.type_relation_enum import RelationTypeEnum 
from util.type_ast_entity_enum import AstEntityTypeEnum as ast_enum
from util.type_ast_entity_enum import Print
from design.parameter_node import ParameterNode
from design.field_node import FieldNode
from design.relation.relation import Relation
import ast
from ast import *

class LoopNode(entity.Entity):
    
    
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
