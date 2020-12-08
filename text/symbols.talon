question [mark]: "?"
(downscore | underscore): "_"
double dash: "--"
triple quote: '"""'
triple tick: "'''"
(dot dot | dotdot): ".."
boom: ", "
plus: "+"
imply: "->"
arrow: "=>"
left imply: "<-"
left arrow: "<="
new line: "\\n"
carriage return: "\\r"
line feed: "\\r\\n"
args:
	insert("()")
	key(left)
inside (squares | list): 
	insert("[]") 
	key(left)
curly: 
	"{}" 
	key(left)
pointy: 
	"<>"
	key(left)
inside percent: 
	"%%" 
	key(left)
inside quotes:
	'""'
	key(left)
angle this: 
    text = edit.selected_text()
    user.paste("<{text}>")
(bracket | brace) this: 
    text = edit.selected_text()
    user.paste("{{{text}}}")
(parens | args) this: 
    text = edit.selected_text()
    user.paste("({text})")
percent this: 
    text = edit.selected_text()
    user.paste("%{text}%")
quote this:
    text = edit.selected_text()
    user.paste('"{text}"')

