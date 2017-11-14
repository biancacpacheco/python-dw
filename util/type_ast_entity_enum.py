import ast

class AstEntityTypeEnum:
    
    ast_entity_dict = {"class":ast.ClassDef, \
         "function":ast.FunctionDef, \
         "import":ast.Import, \
         "call":ast.Call, \
         "expression":ast.Expr,
         "attribute": ast.Attribute,
         "name": ast.Name} 

    try:
        ast_entity_dict["print"] = ast.Print
    except:
        pass    

    
class PrintId:
    id = "print"

class Print: 
    func = PrintId()

