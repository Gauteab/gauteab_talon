# ML-family of programming languages 
# (Meta-Language, not Machine Learning)
# code.language: elm
code.language: haskell
code.language: purescript
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

action(user.code_comment): "-- "
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
action(user.code_state_case):
	"case  of"
    edit.left()
    repeat(2)
action(user.code_state_if): "if "
action(user.code_state_else_if): " else if "
action(user.code_state_else): "else "
action(user.code_import): "import "

# Keywords
[state] let: "let "
[state] in: " in "
state type: " type "
state as: " as "
state then: " then "

# Type Insertion
of type: user.code_type_annotation()
of type <user.code_type>: 
    user.code_type_annotation()
    "{code_type}" 
to [type] <user.code_type>: " -> {code_type} "
[type] <user.code_type> to: " {code_type} -> "

# Type Declarations
type alias: user.code_type_alias()
type alias <user.text>:
    user.code_type_alias()
    insert(user.formatted_text(text, "PUBLIC_CAMEL_CASE"))
    " = "
type alias <user.text> (equals | is) <user.code_type>:
    user.code_type_alias()
    insert(user.formatted_text(text, "PUBLIC_CAMEL_CASE"))
    " = "
    insert(code_type)

