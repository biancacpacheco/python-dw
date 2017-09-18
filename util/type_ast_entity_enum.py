import ast

class AstEntityTypeEnum:
    ast_entity_dict = {"class":ast.ClassDef, \
         "function":ast.FunctionDef, \
         "import":ast.Import, \
         "call":ast.Call, \
         "expr":ast.Expr } 
