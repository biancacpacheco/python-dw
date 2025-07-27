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

class AssignNode(entity.Entity):
        
    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get("__it__")
        cls.__it__ = it = object.__new__(cls)
        it.__init__(*args, **kwds)
        return it

    def __init__(self, name, ast_node):
        entity.Entity.__init__(self,name=name,ast_node=ast_node)
        self.type_entity = EntityTypeEnum.ASSIGN


    """ ACCESS AND CONTROL OF THE NODE ATTRIBUTES"""
    
    def get_name(self):
        return self.name

    def get_ast_node(self):
        return self.ast_node

    def set_name(self, name):
        self.name = name

    def get_body(self):
        return self.ast_node.value
        

    """ ACCESS RELATIONS """

    def get_relations(self):
        return self.relations

    def get_relations_by_type(self, type_relation):
        return self.relations.get(type_relation, [])