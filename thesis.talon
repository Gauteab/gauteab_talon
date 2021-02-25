
call {user.function}: user.code_insert_function(function, "")
symbol <user.symbol_any>: insert(symbol_any)
# constructor {user.constructor}: insert(constructor)

clear symbols: user.clear_symbols()
print symbols: user.print_symbols()

go type <user.code_type>: user.navigate("{code_type}", "type")
go fun {user.function}: user.navigate("{function}", "function")
go imports: user.navigate("", "import")

