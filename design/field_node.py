from design.entity import Entity
from util.type_entity_enum import EntityTypeEnum
from util.type_ast_entity_enum import AstEntityTypeEnum as ast_enum

class FieldNode(Entity):
	
    def __init__(self, name, ast_node, is_call=False, is_attribute=False, \
     is_loop=False, is_tuple=False, is_subscript=False, is_index=False):
        Entity.__init__(self, name=name, ast_node=ast_node)
        self.type_entity = EntityTypeEnum.FIELD
        self.is_call = is_call
        self.is_attribute = is_attribute
        self.is_loop = is_loop
        self.is_tuple = is_tuple
        self.is_subscript = is_subscript
        self.is_index = is_index
        self.body = {}
        
        if is_loop:
            self.body = self.ast_node.body

    def get_name(self):
        return self.name        

    def set_name(self, name):
        self.name = name
    
    def set_name_to_ast_name(self):
        if self.is_call and not isinstance(self.ast_node.func, ast_enum.ast_entity_dict['call']) \
         and not isinstance(self.ast_node.func, ast_enum.ast_entity_dict['compare']):
            try:
                self.name = self.ast_node.func.attr
            except:
                self.name = self.ast_node.func.id
                
        elif isinstance(self.ast_node.func, ast_enum.ast_entity_dict['call']):
            try:
                self.name = self.ast_node.func.func.id
            except:
                print("FERROU MUITO")
                
        elif isinstance(self.ast_node.func, ast_enum.ast_entity_dict['compare']):
            try:
                self.name = self.ast_node.func.left.n
            except:
                try:
                    self.name = self.ast_node.func.left.s
                except:
                    try:
                        self.name = self.ast_node.func.left.func.id
                    except:
                        self.name = self.ast_node.func.left.id    
                        
       
                    
        if self.is_loop:
            try:
                self.name = str(self.ast_node.target)
            except:
                self.name = str(self.ast_node.test)
                          
            
    def get_parent_name(self):
        if self.is_call and not \
          isinstance(self.ast_node.parent, ast_enum.ast_entity_dict['module']) and \
            isinstance(self.ast_node.parent, ast_enum.ast_entity_dict['assign']):
              try:
                  return self.ast_node.parent.targets[0].id
              except:
                  return self.name  
        else:
            return self.name            
                    
    def get_nested_loops(self):
        loops = []
        if self.is_loop:
            for e in self.body:
                if isinstance(e, ast_enum.ast_entity_dict['for']) or \
                 isinstance(e, ast_enum.ast_entity_dict['while']):
                     loops.append(e)
            
        return loops
            
            
                                
