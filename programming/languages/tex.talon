mode: user.tex
mode: command 
and code.language: tex
-
tag(): user.code_comment
action(user.code_comment): "-- "

add item: "\\item "
use package: "\\usepackage{"
add {user.tex_simple_commands}: user.tex_command(tex_simple_commands)
begin {user.tex_target}: user.tex_begin(tex_target)
text {user.tex_text_commands}: user.tex_command(tex_text_commands)
snip {user.tex_snippets}: "{tex_snippets}\t"
add citation: 
    "~"
    user.tex_command("parencite")
comment: "% "
quoted:
    "``''"
    key(left left)

minted helm:
    "\\begin{{minted}}{{elm}}\n\n"
    "\\end{{minted}}\n"
    key(up up)

reference: "~\\ref{"
citation: "~\\parencite{"

code {user.code_languages}:
    "\\begin{{code}}{{{code_languages}}}{{}}{{}}\n"
    "\\end{{code}}"
