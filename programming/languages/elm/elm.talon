mode: user.elm
mode: command 
and code.language: elm
-
action(user.code_type_definition): "type "	
action(user.code_type_annotation): " : "
action(user.code_type_alias): "type alias "

exposing: 
    " exposing ()"
    edit.left()

# Imports
import { user.haskell_module}: user.haskell_import_module(haskell_module)
import (qualified | Q) { user.haskell_module }:
    user.haskell_import_module_qualified(haskell_module)
# Modules
module <user.haskell_module_alias>: "{haskell_module_alias}"
<user.haskell_module_alias> dot: "{haskell_module_alias}."
<user.haskell_module_alias> dot <user.camel_text>: 
    "{user.haskell_module_alias}.{camel_text}"
