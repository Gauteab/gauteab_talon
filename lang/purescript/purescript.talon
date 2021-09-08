mode: user.purescript
mode: command 
and code.language: purescript
-
action(user.code_type_definition): "data "	
action(user.code_comment): "-- "
action(user.code_document_string): "-- | "
action(user.code_type_annotation): " :: "
action(user.code_type_alias): "type "

# Keywords
foreign import: "foreign import "
instance: "instance "
deriving: " deriving "
deriving {user.haskell_classes}+: " deriving ({user.insert_comma_separated(haskell_classes_list)})"
class: "class "
add where: "where "
do block: "do\n"
comes from: " <- "

# Type Declarations
data: "data "
data <phrase>:
    "data "
    insert(user.formatted_text(phrase, "PUBLIC_CAMEL_CASE"))
    " = "
new type: "newtype "
new type <phrase>:
    "newtype "
    insert(user.formatted_text(phrase, "PUBLIC_CAMEL_CASE"))
    " = "
    insert(user.formatted_text(phrase, "PUBLIC_CAMEL_CASE"))
    " "

# Operators
function {user.haskell_operator_list}: "({haskell_operator_list}) "
{user.haskell_operator_list} <user.code_functions>: 
    " {haskell_operator_list} "
    user.code_insert_function(code_functions, "")
<user.code_functions> {user.haskell_operator_list}: 
    user.code_insert_function(code_functions, "")
    " {haskell_operator_list} "

# Imports
import { user.haskell_module}: user.haskell_import_module(haskell_module)
import (qualified | Q) { user.haskell_module }:
    user.haskell_import_module_qualified(haskell_module)

# Modules
module <user.haskell_module_alias>: "{haskell_module_alias}"
<user.haskell_module_alias> dot: "{haskell_module_alias}."
<user.haskell_module_alias> dot <user.camel_text>: 
    "{user.haskell_module_alias}.{camel_text}"

