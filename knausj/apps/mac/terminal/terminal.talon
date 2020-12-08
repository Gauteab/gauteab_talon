app: apple_terminal
app: iTerm2
-
tag(): user.tabs
tag(): user.splits

# Windowing
action(user.split_window_left): key(cmd-alt-left)
action(user.split_window_right): key(cmd-alt-right)
action(user.split_window_down): key(cmd-alt-down)
action(user.split_window_up): key(cmd-alt-up)
action(user.split_window_horizontally): key(cmd-shift-d)
action(user.split_window_vertically): key(cmd-d)

abort: key(ctrl-c)
suspend: key(ctrl-z)
