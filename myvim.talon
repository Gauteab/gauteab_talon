title: /VIM/i

-
norm: key(ctrl-c)
complete: key(ctrl-n)

delete [around] word: key(ctrl-c d a w)
delete line: key(ctrl-c d d)
change [inner] word: key(ctrl-c c i w)
change line: key(ctrl-c c c)
duplicate line: key(ctrl-c y y p)
comment line: key(ctrl-c g c c)
comment (par | paragraph): key(ctrl-c g c i p)
replace <phrase>:
    key(ctrl-c c i w)
    insert(phrase)

jump down: key(ctrl-c ctrl-d)
jump up: key(ctrl-c ctrl-u)
scroll bottom: key(ctrl-c G)
scroll top: key(ctrl-c g g)
forward: key(ctrl-c f)
backward: key(ctrl-c F)
scan <user.word>:
    key(ctrl-c /)
    insert(user.formatted_text(word, "snake"))
    key(enter)
scan: key(ctrl-c /)
scan back <user.word>:
    key(ctrl-c ?)
    insert(user.formatted_text(word, "snake"))
    key(enter)
scan back: key(ctrl-c ?)

find file: " g"
find symbol: " rg"
buffers: 
    key(ctrl-c)
    ":Buffers\n"

pain (vertical|vert): key(ctrl-c : v s enter)
pain (horizontal|whore): key(ctrl-c : s p enter)
pain right: key(ctrl-c ctrl-w l)
pain left: key(ctrl-c ctrl-w h)
pain up: key(ctrl-c ctrl-w k)
pain down: key(ctrl-c ctrl-w j)

set wrap: ":set wrap\n"
[set] no wrap: ":set nowrap\n"
no highlight: ":noh\n"

run it: key(f9)
save and quit: key(ctrl-c : w q enter)
save it: key(ctrl-c : w enter)
quit it: key(ctrl-c : q enter)
quit everything: key(ctrl-c : q a enter)
do edit: key(ctrl-c : e space)
do set: key(ctrl-c : s e t space)
do echo: key(ctrl-c : e c h o space)

next air: key(ctrl-n)
last air: key(ctrl-b)

spell on: ":set spell spelllang=en_us\n"
spell off: ":set nospell\n"
spell next: key(] s)
spell last: key([ s)
spell fix: key(z =)

mark [down] preview: ":MarkdownPreview\n"

substitute: ":s/"
substitute all: ":%s/"
