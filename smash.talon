mode: user.dolphin
title: /Dolphin/i
-
run: user.start_hold("left")
sprint: user.start_hold("right")
shield: user.start_hold("q")
recover: user.input_string("up-b")
rec left: 
    user.start_hold("up")
    user.sleep_frames(5)
    user.start_hold("left")
    user.sleep_frames(5)
    user.input_string("b")

{user.smash_moves}: user.perform(smash_moves_list)

[press] start: user.button("s")
back: user.button("b")
go: user.input_string("right right right y 3")
no: user.input_string("left left left y 3")
ledge right:
    user.input_string("down y")
    user.input_string("right",12)
    user.input_string("down-right-q")
ledge left:
    user.input_string("down y")
    user.input_string("left",12)
    user.input_string("down-left-q")
exit menu: user.button("b", 60)
select Marth: 
    user.input_string("up", 20)
    user.input_string("right a", 33)
stop right:
    user.input_string("right", 13)
    user.input_string("left", 2)
    user.start_hold("q")
stop left:
    user.input_string("left", 13)
    user.input_string("right", 2)
    user.start_hold("q")
B left: user.input_string("left-b")
B right: user.input_string("right-b")
# dropping through platforms with aerial
