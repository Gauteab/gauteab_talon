
import time
from talon import Context, Module, actions, settings, ui

mod = Module()
ctx = Context()
# ctx.matches = "title: /VIM/i"

mod.list("vim_verbs", "verbs")
ctx.lists["user.vim_verbs"] = {
    "delete": "d",
    "change": "c",
    "comment": "gc",
    "upper": "gU",
    "lower": "gu",
    "lower": "gu",
    "indent": ">",
    "dedent": "<",
    "visual": "v",
}

mod.list("vim_targets", "targets")
ctx.lists["user.vim_targets"] = {
    "par": "ip",
    "string": "i\"",
    "to": "t",
    "down par": "}",
    "up par": "{",
    "back": "b",
    "back word": "b",
    "big back": "B",
    "end": "e",
    "big end": "E",
    "word": "w",
    "big word": "W",
    "back end": "ge",
    "back big end": "gE",
    "right": "l",
    "left": "h",
    "down": "j",
    "up": "k",
    "next": "n",
    "next reversed": "N",
    "previous": "N",
    "column zero": "0",
    "column": "|",
    "start of line": "^",
    "end of line": "$",
    "search under cursor": "*",
    "search under cursor reversed": "#",
    "again": ";",
    "again reversed": ",",
    "down sentence": ")",
    "sentence": ")",
    "up sentence": "(",
    "start of next section": "]]",
    "start of previous section": "[[",
    "end of next section": "][",
    "end of previous section": "[]",
    "matching": "%",
    "cursor home": "H",
    "cursor middle": "M",
    "cursor last": "L",
    "file start": "gg",
    "file top": "gg",
    "file end": "G",
    "file bottom": "G",
    "line": "line"
}

@mod.action_class
class Actions:
    def vim_set_normal_mode():
        ""
        actions.key("ctrl-c")

    def vim_normal_mode_key(k: str):
        ""
        actions.user.vim_set_normal_mode()
        actions.key(k)

    def vim_normal_mode(s: str):
        ""
        actions.user.vim_set_normal_mode()
        actions.insert(s)

    def vim_do_action(verb:str, target:str, number:int = None):
        ""
        target = target if target != "line" else verb[-1]
        cmd = f"{verb}{number if number else ''}{target}"
        actions.user.vim_normal_mode(cmd)

# @ctx.action_class("win")
# class win_actions:
#     def filename():
#         title = actions.win.title()
#         result = title.split("|")[-1]
#         return result

#     def file_ext():
#         ext = "." + actions.win.filename().split(".")[-1]
#         # print(ext)
#         return ext


@ctx.action_class("edit")
class edit_actions:
    def copy():
        actions.key("y")
