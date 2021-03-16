
call {user.function}: user.code_insert_function(function, "")
symbol <user.identifier>: insert(identifier)
# constructor {user.constructor}: insert(constructor)

clear symbols: user.clear_symbols()
print symbols: user.print_symbols()

go to <user.identifier>: user.symbol_navigate("{identifier}", "identifier")
go type <user.code_type>: user.symbol_navigate("{code_type}", "type")
go fun {user.function}: user.symbol_navigate("{function}", "function")
select fun {user.function}: user.symbol_select("{function}", "function")
select type <user.code_type>: user.symbol_select("{code_type}", "type")
delete type <user.code_type>: 
    user.symbol_select("{code_type}", "type")
    "d"
go imports: user.symbol_navigate("", "import")

select function: user.symbol_select_parent("value_declaration")

go to next: user.go_to_next_result("forward")
go to last: user.go_to_next_result("backward")

print cursor: user.print_cursor()

# select: user.vim_select_range(38,0,48,0)
