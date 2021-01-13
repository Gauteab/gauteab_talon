mode: user.haskell
mode: command 
and code.language: haskell
-
tag(): user.code_operators
tag(): user.code_comment
tag(): user.code_generic
settings():
    user.code_private_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_protected_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_public_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_private_variable_formatter = "PRIVATE_CAMEL_CASE"
    user.code_protected_variable_formatter = "PRIVATE_CAMEL_CASE"
    user.code_public_variable_formatter = "PRIVATE_CAMEL_CASE"
action(user.code_operator_lambda): 
    "(\\)"
    edit.left()
action(user.code_operator_assignment): " = "
action(user.code_operator_addition): " + "
action(user.code_operator_subtraction): " - "
action(user.code_operator_multiplication): " * "
action(user.code_operator_division): " / "
action(user.code_operator_modulo): " % "
action(user.code_operator_equal): " == "
action(user.code_operator_not_equal): " /= "
action(user.code_operator_greater_than): " > "
action(user.code_operator_greater_than_or_equal_to): " >= "
action(user.code_operator_less_than): " < "
action(user.code_operator_less_than_or_equal_to): " <= "
action(user.code_operator_and): " && "
action(user.code_operator_or): " || "
action(user.code_null): "Nothing"
action(user.code_state_if): "if "
state then: " then "
action(user.code_state_else_if): "else if"
action(user.code_state_else): "else "
action(user.code_state_case):
	"case  of"
    edit.left()
    repeat(2)
action(user.code_type_definition): "type "	
action(user.code_import): "import "
action(user.code_comment): "-- "

# Keywords
instance: "instance "
deriving: " deriving "
deriving {user.haskell_classes}+: " deriving ({user.insert_comma_separated(haskell_classes_list)})"
class: "class "
let: "let "
add where: "where "
do block: "do\n"
comes from: " <- "

# Type Declarations
type alias: "type "
type alias <phrase>:
    "type "
    insert(user.formatted_text(phrase, "PUBLIC_CAMEL_CASE"))
    " = "
type alias <phrase> [(equals | is)] <user.haskell_type>:
    "type "
    insert(user.formatted_text(phrase, "PUBLIC_CAMEL_CASE"))
    " = "
    insert(user.haskell_type)
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

# Type Insertion
type <user.haskell_type>: "{haskell_type}"
of type: " :: "
of type <user.haskell_type>: " :: {user.haskell_type}" 
to [type] <user.haskell_type>: " -> {user.haskell_type} "
[type] <user.haskell_type> to: " {user.haskell_type} -> "
<user.haskell_type> to <user.haskell_type_>: " {haskell_type} -> {haskell_type_} "
<user.haskell_type> with <user.haskell_type_>: " ({haskell_type}, {haskell_type_}) "
list of <user.haskell_type>: " [{haskell_type}] "

# Operators
{user.haskell_operator_list}: " {haskell_operator_list} "
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

# Debug
<user.haskell_test>: "{haskell_test}"

# Miscellaneous
range from <number>: " [{number} ..] "
<user.haskell_range>: "{haskell_range}"
range <number>: 
    " [{number} ..  ] "
    edit.left()
    repeat(2)
