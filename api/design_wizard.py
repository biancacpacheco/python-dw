import ast
from util.type_relation_enum import RelationTypeEnum
from util.type_ast_entity_enum import AstEntityTypeEnum
from design.relation.relation import Relation
from design.class_node import ClassNode
from design.loop_node import LoopNode
from design.function_node import FunctionNode
from design.field_node import FieldNode


class PythonDW:
    """Python Design Wizard API"""

    # Init
    def __init__(self):
        self.ast_tree = []
        self.entities = {}
        self.ast_elements_dict = AstEntityTypeEnum.ast_entity_dict

    def parse(self, file_path):
        read_file = open(file_path, 'r')
        self.ast_tree = ast.parse(read_file.read())

        for node in ast.walk(self.ast_tree):
            for child in ast.iter_child_nodes(node):
                child.parent = node

    def parse_loop_name(self, name):
        return ''.join([i for i in name if not i.isdigit()])

    # WIP[This should iter over array while and for]
    def get_loop_entity_by_name(self, name, type_of_loop='for'):
        loops = self.entities.get(type_of_loop)
        if loops is None:
            return ''
        if type_of_loop in name:
            for e in loops:
                if e.get_name() == name:
                    return e
        return ''

    def get_entity_by_name(self, name):
        if 'for' in name and name != 'for' \
             or 'while' in name and name != 'while':
            type_of_loop = self.parse_loop_name(name)
            return self.get_loop_entity_by_name(name, type_of_loop)
        entity = self.entities.get(name)
        if entity is None:
            entity = ""
        return entity
    
    def get_entity_by_ast_node(self, target_node):
        for maybe_list in self.entities.values():
            if not isinstance(maybe_list, list):
                maybe_list = [maybe_list]
            for entity in maybe_list:
                if entity.ast_node is target_node:
                    return entity
        return None

    def get_entity_by_type(self, type_entity):
        entities_return_fields = []
        entities_return_functions = []
        entities = self.entities
        for k, v in entities.items():
            if (type(v) == type([])) and isinstance(v[0], FieldNode):
                entities_return_fields += v
            elif isinstance(v, type_entity):
                entities_return_functions.append(v)
        if type_entity == FieldNode:
            return entities_return_fields
        elif type_entity == FunctionNode:
            return entities_return_functions

    def delete_entity_by_name(self, name):
        del self.entities[name]

    def delete_all_entities(self):
        self.entities = {}

    def is_leaf_from_branch(self, branch_node, leaf):
        response = False
        while not isinstance(leaf.ast_node, self.ast_elements_dict['module']):
            if leaf.ast_node.parent != branch_node.ast_node:
                leaf.ast_node = leaf.ast_node.parent
            else:
                response = True
                break
        return response

    def check_loop_exists(self, node, type_loop):
        loops = self.entities.get(type_loop)
        if loops is None:
            return False

        for loop in loops:
            if node == loop.get_ast_node():
                return True

            
    def check_entity_exists(self, node, type_entity):
        entity_list = self.entities.get(type_entity)

        if entity_list is None:
            return False

        for e in entity_list:
            if node == e.get_ast_node():
                return True

    """ Returning nodes functions """

    def get_all_elements_file(self, key):
        list_elements = []
        if key in self.ast_elements_dict:
            for node in ast.walk(self.ast_tree):
                if isinstance(node, self.ast_elements_dict[key]):
                    list_elements.append(node)
        return list_elements

    def get_everything(self):
        list_elements = []
        for node in ast.walk(self.ast_tree):
            list_elements.append(node)
        return list_elements

    def get_all_fields_without_class_func(self):
        return self.get_all_elements_file('augassign') + \
               self.get_all_elements_file('assign') + \
               self.get_all_elements_file('call') + \
               self.get_all_elements_file('for') + \
               self.get_all_elements_file('while') + \
               self.get_all_elements_file('load') + \
               self.get_all_elements_file('store') + \
               self.get_all_elements_file('index') + \
               self.get_all_elements_file('subscript') + \
               self.get_all_elements_file('if') + \
               self.get_all_elements_file('expression') + \
               self.get_all_elements_file('print')

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

    def get_class_by_name(self, name):
        class_found = []
        classes = self.get_all_classes()
        for clas in classes:
            if clas.name == name:
                class_found = clas
        return class_found

    ##############################################################

    # Create this helpful function

    def get_node_calls_by_name(self, name):
        call_nodes = []
        fields = self.get_all_fields_without_class_func()

        for field in fields:

            if isinstance(field, self.ast_elements_dict['call']):
                call_name = self.get_name_call_node(field)
                if call_name == name:
                    call_nodes.append(field)

            elif isinstance(field, self.ast_elements_dict['print']) \
                    and name == 'print':
                call_nodes.append(field)

        return call_nodes

    def get_name_call_node(self, node):
        if isinstance(node.func, self.ast_elements_dict['attribute']):
            return node.func.attr
        else:
            return node.func.id

            # WORKING HERE TOP

    #############################################################

    # Returns node not entity
    def get_function_by_name(self, name):
        function_found = []
        functions = self.get_all_functions()
        for func in functions:
            if func.name == name:
                function_found = func
        return function_found

    def get_import_by_name(self, name):
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

    """ CREATION ENTITY FUNCTIONS """

    # TODO(Caio) Needs update
    def create_class_entity(self, node):
        class_entity = ClassNode("temporary_name", ast_node=node)
        class_entity.set_name_to_ast_name()
        name = class_entity.get_name()
        self.entities[name] = class_entity

    def create_function_entity(self, node):
        function_entity = FunctionNode("temporary_name", ast_node=node)
        function_entity.set_name_to_ast_name()
        name = function_entity.get_name()

        # Only creates if is not in entity dict
        if self.get_entity_by_name("def_" + name) == "":
            self.entities["def_" + name] = function_entity
            calls = function_entity.get_function_calls_str(just_caller=True)
            self.create_calls_entities_inside_function(calls, function_entity)

    def create_calls_entities_inside_function(self, calls, function_entity):
        for call in calls:
            call_entity = self.get_entity_by_name("def_" + call)
            if call_entity != "":
                self.__create_call_already_exists(call, call_entity,
                                                  function_entity)

            elif self.get_function_by_name(call) != []:
                self.__create_call_not_exists(call, function_entity)

            elif self.get_function_by_name(call) == []:
                call_nodes = self.get_node_calls_by_name(call)
                for node in call_nodes:
                    self.create_field_entity(node, call)

    def __create_call_already_exists(self, call,
                                     call_entity, function_entity):
        call_entity.add_callee(function_entity)
        self.get_entity_by_name("def_" + call)

        relation_calls = Relation(function_entity,
                                  RelationTypeEnum.CALLS, call_entity)
        function_entity.add_relation(relation_calls)

        relation_iscalled = Relation(call_entity,
                                     RelationTypeEnum.ISCALLED,
                                     function_entity)
        call_entity.add_relation(relation_iscalled)

    def __create_call_not_exists(self, call, function_entity):
        node_function_callee = \
            self.get_function_by_name(call)

        classe = function_entity.__class__

        function_callee = classe("temporary_name2",
                                 ast_node=node_function_callee)

        relation_calls = Relation(function_entity,
                                  RelationTypeEnum.CALLS, function_callee)

        function_entity.add_relation(relation_calls)

        relation_iscalled = Relation(function_callee,
                                     RelationTypeEnum.ISCALLED,
                                     function_entity)

        function_callee.add_relation(relation_iscalled)

        function_callee.set_name_to_ast_name()
        callee_name = function_callee.get_name()
        function_callee.add_callee(function_entity)
        self.entities["def_" + callee_name] = function_callee

    def create_field_entity(self, node, name=""):
        # parent = node.parent
        # grand_parent = {}
        field_node = {}

        # if not isinstance(parent, ast.Module):
        #     grand_parent = parent.parent

        if isinstance(node, self.ast_elements_dict['for']):
            self.create_finite_loop_entity(node)

        if isinstance(node, self.ast_elements_dict['while']):
            self.create_infinite_loop_entity(node)

        if isinstance(node, self.ast_elements_dict['if']):
            field_node = FieldNode("if", ast_node=node, is_loop=False)
            if self.entities.get("if") is None:
                field_node.set_name("if1")
                self.entities["if"] = [field_node]
            else:
                field_node.set_name('if' + str(len(self.entities["if"]) + 1))
                self.entities["if"].append(field_node)

        if isinstance(node, self.ast_elements_dict['assign']) or \
                isinstance(node, self.ast_elements_dict['augassign']):
            node = node.value

        if isinstance(node, self.ast_elements_dict['call']):

            if isinstance(node.func, self.ast_elements_dict['attribute']):
                field_node = FieldNode(node.func.attr, ast_node=node,
                                       is_call=True, is_attribute=True)
                if isinstance(node.func.value, self.ast_elements_dict['call']):
                    field_node_value = FieldNode("Temporary_name",
                                                 ast_node=node.func.value,
                                                 is_call=True,
                                                 is_attribute=False)
                    field_node_value.set_name_to_ast_name()
                    relation = Relation(field_node, RelationTypeEnum.ISCALLED,
                                        field_node_value)
                    field_node.add_relation(relation)
            else:
                field_node = FieldNode("call", ast_node=node, is_call=True,
                                       is_attribute=False)
                field_node.set_name_to_ast_name()

            if self.entities.get(field_node.get_name()) is None:
                self.entities[field_node.get_name()] = [field_node]
            else:
                self.entities[field_node.get_name()].append(field_node)
        else:
            if isinstance(node, self.ast_elements_dict['index']):
                field_node = FieldNode("index", ast_node=node, is_index=True)
            elif isinstance(node, self.ast_elements_dict['subscript']):
                field_node = FieldNode("subscript", ast_node=node,
                                       is_subscript=True)
            elif isinstance(node, self.ast_elements_dict['tuple']):
                field_node = FieldNode("tuple", ast_node=node,
                                       is_subscript=True)
            elif isinstance(node, self.ast_elements_dict['assign']) or \
                    isinstance(node, self.ast_elements_dict['call']):
                self.create_field_entity(node.value)

            if field_node != {}:
                if self.entities.get("assign_field") is None:
                    self.entities["assign_field"] = [field_node]
                else:
                    self.entities["assign_field"].append(field_node)

    def create_finite_loop_entity(self, node):
        is_loop_already_in_entities = self.check_loop_exists(node, 'for')

        if is_loop_already_in_entities:
            return
        
        loop_entity = LoopNode("for", ast_node=node, limited_loop=True)
        if self.entities.get("for") is None:
            loop_entity.set_name("for1")
            self.entities["for"] = [loop_entity]
        else:
            loop_entity.set_name('for' + str(len(self.entities["for"]) + 1))
            self.entities["for"].append(loop_entity)

    def create_infinite_loop_entity(self, node):
        is_loop_already_in_entities = self.check_loop_exists(node, 'while')

        if is_loop_already_in_entities:
            return

        loop_entity = LoopNode("while", ast_node=node, limited_loop=False)
        if self.entities.get("while") is None:
            loop_entity.set_name("while1")
            self.entities["while"] = [loop_entity]
        else:
            loop_entity.set_name('while' +
                                 str(len(self.entities["while"]) + 1))
            self.entities["while"].append(loop_entity)

    def create_body_loop(self, loop):
        for node in loop.get_body():
            if isinstance(node, self.ast_elements_dict['for']):
                self.create_finite_loop_entity(node)
                nestled_loop = self.get_entity_by_ast_node(node)
                loop_entity = self.get_entity_by_name(loop.get_name())
                relation = Relation(loop_entity, RelationTypeEnum.HASLOOP,
                                    nestled_loop)
                loop_entity.add_relation(relation)
            elif isinstance(node, self.ast_elements_dict['while']):
                self.create_infinite_loop_entity(node)
                nestled_loop = self.get_entity_by_ast_node(node)
                loop_entity = self.get_entity_by_name(loop.get_name())
                relation = Relation(loop_entity, RelationTypeEnum.HASLOOP,
                                    nestled_loop)
                loop_entity.add_relation(relation)
            elif isinstance(node, self.ast_elements_dict['if']):
                continue
            else:
                # self.create_field_entity(node) # i dont think we need this
                continue
    """ACCESSING ENTITIES FUNCTIONS"""

    def get_entities_by_type(self, key):
        if key in self.entities:
            return self.entities[key]
        else:
            return []

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
        functions = \
            [e.name for e in self.get_functions_inside_class(name)]
        return functions

    """ Major actions manipulating entities """

    def design_populate_loop_entities(self, loop_name='for'):
        loop_entities = self.entities.get(loop_name)
        if (loop_entities is None):
            return
        for loop in self.entities.get(loop_name):
            self.create_body_loop(loop)

    def design_populate_all_entities(self):
        fields = self.get_all_fields_without_class_func()
        functions = self.get_all_functions()
        for e in fields:
            self.create_field_entity(e)
        for e in functions:
            self.create_function_entity(e)
        self.design_populate_loop_entities()
        self.design_populate_loop_entities(loop_name='while')

    def design_get_relations_from_entity(self, entity_name, type_relation):
        entity = self.get_entity_by_name(entity_name)
        return entity.get_relations_by_type('HASLOOP') if entity != '' else []

    def design_get_callees_from_entity_relation(
         self, entity_name, type_relation):
        entities = self.design_get_relations_from_entity(
            entity_name, type_relation
        )
        return [e.get_callee() for e in entities] if len(entities) > 0 else []

    def design_entity_has_type_as_child(self, entity, type_to_filter):
        filtered_entities = self.entities.get(type_to_filter)
        if filtered_entities is None:
            return False
        for field in filtered_entities:
            if self.is_leaf_from_branch(entity, field):
                return True
        return False

    def design_list_entity_has_every_child_as_type(
         self, entity_list, type_to_filter):
        for entity in entity_list:
            if not \
             self.design_entity_has_type_as_child(entity, type_to_filter):
                return False
        return True

    def design_list_entity_has_some_child_as_type(
         self, entity_list, type_to_filter):
        for entity in entity_list:
            if self.design_entity_has_type_as_child(entity, type_to_filter):
                return True
        return False

    def design_get_qtd_calls_function(self, name):
        return len(self.get_node_calls_by_name(name))

    def design_get_entity(self, name):
        entity = self.get_entity_by_name(name)
        if entity == '':
            return []
        if not isinstance(entity, list):
            return [entity]
        return entity
