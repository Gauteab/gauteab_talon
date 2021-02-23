
import re

from talon import Context, Module, actions, settings, ctrl

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.elm
mode: command
and code.language: elm
"""

ctx.lists["user.code_functions"] = {
    "print": "print",
    "via non empty": "viaNonEmpty",
    "return": "return",
    "pure": "pure",
    "undefined": "undefined",
    "F map": "fmap",
    "map": "map",
    "car": "char",
    "lens one": "_1",
    "lens two": "_2",
}

ctx.lists["user.code_types"] = {
    "boolean": "Bool",
    "zipper": "Zipper",
    "either": "Either",
    "result": "Result",
    "unit": "()",
    "integer": "Integer",
    "hint": "Int",
    "string": "String",
    "float": "Float",
    "maybe": "Maybe",
    "dictionary": "Dict",
    "set": "Set",
    "car": "Char",
    "character": "Char",
    "parser": "Parser",
}

ctx.lists["user.code_libraries"] = { k:k for k in
    [ "List"
    , "Maybe"
    ]
}

modules = {
    #       qualified, alias
    # "set": ("Data.Set", "Set"),
    # "map": ("Data.Map", "Map"),
    # "zipper": ("Data.List.Zipper", "Zipper"),
    # "hint map": ("Data.IntMap", "IntMap"),
    # "hint set": ("Data.IntSet", "IntSet"),
    # "shell": ("Shelly", "Shelly"),
    # "prelude": ("Prelude", "Prelude"),
    # "list": ("Data.List", "List"),
    # "foldable": ("Data.Foldable", "Foldable"),
    # "lens": ("Control.Lens", "Lens"),
    # "text": ("Data.Text", "Text"),
}

mod.list("haskell_module", desc="haskell modules")
ctx.lists["user.haskell_module"] = [s for (s,(q,a)) in modules.items()]

@mod.action_class
class Actions:
    def test_action(name: str):
        """Test Action"""
        print(name)


@ctx.action_class("user")
class user_actions:
    def code_insert_function(text: str, selection: str):
        actions.insert(text + " ")

