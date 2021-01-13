mode: user.tex
mode: command 
and code.language: tex
-
tag(): user.code_comment
action(user.code_comment): "-- "

add {user.tex_simple_commands}: user.tex_command(tex_simple_commands)
begin {user.tex_target}: user.tex_begin(tex_target)
text {user.tex_text_commands}: user.tex_command(tex_text_commands)
snip {user.tex_snippets}: "{tex_snippets}\t"
comment: "% "
quoted:
    "``''"
    key(left left)
