
import re

from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.haskell
mode: command
and code.language: haskell
"""

ctx.lists["user.code_functions"] = {
    "print": "print",
    "return": "return",
    "pure": "pure",
    "undefined": "undefined",
    "F map": "fmap",
    "map": "map",
    "car": "char",
    "lens one": "_1",
    "lens two": "_2",
}

mod.list("haskell_type_list", desc="haskell types")
ctx.lists["user.haskell_type_list"] = {
    "boolean": "Bool",
    "either": "Either",
    "unit": "()",
    "integer": "Integer",
    "hint": "Int",
    "I O": "IO",
    "eye oh": "IO",
    "string": "String",
    "hole": "_",
    "float": "Float",
    "foldable": "Foldable",
    "vector": "Vector",
    "sequence": "Seq",
    "maybe": "Maybe",
    "map": "Map",
    "set": "Set",
    "car": "Char",
    "character": "Char",
    "parser": "Parser",
}

mod.list("haskell_operator_list", desc="haskell operators")
ctx.lists["user.haskell_operator_list"] = {
    "bind left": "=<<",
    "bind right": ">>=",
    "map left": "<$>",
    "map right": "<&>",
    "beefy star": "<*>",
    "skip left": "<*",
    "skip right": "*>",
    "app left": "$",
    "app right": "&",
    "map end": "<>",
    "compose": ".",
    "view": "^.",
    "preview": "^?",
    "preview hard": "^?!",
    "to list of": "^..",
    "lens set": ".~",
    "lens assign": ".=",
    "modify": "%~",
}

modules = {
    #       qualified, alias
    "set": ("Data.Set", "Set"),
    "prelude": ("Prelude", "Prelude"),
    "list": ("Data.List", "List"),
    "foldable": ("Data.Foldable", "Foldable"),
    "lens": ("Control.Lens", "Lens"),
    "text": ("Data.Text", "Text"),
    "map": ("Data.Map.Strict", "Map"),
}

mod.list("haskell_module_list", desc="haskell modules")
ctx.lists["user.haskell_module_list"] = [s for (s,(q,a)) in modules.items()]

@mod.capture(rule="{self.haskell_type_list}+")
def haskell_type_(m) -> str: return str(m)

@mod.capture(rule="{self.haskell_type_list}+")
def haskell_type(m) -> str: return str(m)

@mod.capture(rule="{self.haskell_module_list}")
def haskell_module(m) -> str: return modules[m.haskell_module_list][0]

@mod.capture(rule="{self.haskell_module_list}")
def haskell_module_alias(m) -> str: return modules[m.haskell_module_list][1]

@mod.capture(rule="{self.haskell_type_list}+ test {self.code_functions}")
def haskell_test(m) -> str:
    ""
    print(m)
    print(m.haskell_type_list)
    print(m.code_functions)
    return ""

@mod.action_class
class haskell_actions:
    def haskell_test_action(name: str):
        """Test Action"""
        print(name)
    def haskell_import_module_qualified(name: str):
        """Import module qualified"""
        actions.user.paste(f"import qualified {modules[name][0]} as {modules[name][1]}")
    def haskell_import_module(name: str):
        """Import module unqualified"""
        actions.user.paste(f"import {modules[name][0]}")


@ctx.action_class("user")
class user_actions:
    def code_insert_function(text: str, selection: str):
        actions.user.paste(text + " ")

