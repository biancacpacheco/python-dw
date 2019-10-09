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

    def __init__(self, name, ast_node, limited_loop=True):
        entity.Entity.__init__(self,name=name,ast_node=ast_node)
        self.type_entity = EntityTypeEnum.LOOP
        self.limited_loop = limited_loop


    """ ACCSSES AND CONTROL OF THE NODE ATTRIBUTES"""
    
    def get_name(self):
        if "for" not in self.name and "while" not in self.name:
            return "for" if limited_loop else "while"
        else:
            return self.name

    def set_name(self, name):
        self.name = name

    def get_body(self):
        return self.ast_node.body
        
    def get_nested_loops(self):
        loops = []
        for e in self.get_body():
            if isinstance(e, ast_enum.ast_entity_dict['for']) or \
                isinstance(e, ast_enum.ast_entity_dict['while']):
                    loops.append(e)
        return loops
