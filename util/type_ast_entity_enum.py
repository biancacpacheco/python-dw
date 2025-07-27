import ast

class AstEntityTypeEnum:
    
    ast_entity_dict = {"class":ast.ClassDef, \
         "function": ast.FunctionDef, \
         "import": ast.Import, \
         "call": ast.Call, \
         "expression": ast.Expr, \
         "attribute": ast.Attribute, \
         "name": ast.Name, \
         "load": ast.Load, \
         "store": ast.Store, \
         "assign": ast.Assign, \
         "augassign": ast.AugAssign, \
         "module" : ast.Module, \
         "for" : ast.For, \
         "while" : ast.While, \
         "store" : ast.Store, \
         "subscript" : ast.Subscript, \
         "index" : ast.Index, \
         "tuple" : ast.Tuple, \
         "if" : ast.If, \
         "compare": ast.Compare, \
         "list": ast.List, \
         "set": ast.Set, \
         "dict": ast.Dict, \
         "constant": ast.Constant, \
         "binop": ast.BinOp, \
         "subscript": ast.Subscript 
         } 

    try:
        ast_entity_dict["print"] = ast.Print
    except:
        pass    

    
class PrintId:
    id = "print"

class Print: 
    func = PrintId()

