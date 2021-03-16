
import re

from talon import Context, Module, actions, settings, ctrl
from  ...programming import standard_operators

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.purescript
mode: command
and code.language: purescript
"""

ctx.lists["user.code_functions"] = {
    "log": "log",
    "via non empty": "viaNonEmpty",
    "return": "return",
    "pure": "pure",
    "undefined": "undefined",
    "F map": "fmap",
    "map": "map",
    "car": "char",
    "tuple": "Tuple"
}

mod.list("haskell_classes", desc="haskell classes")
ctx.lists["user.haskell_classes"] = {
    "show":"Show",
    "equal":"Eq",
    "order":"Ord",
}

# mod.list("haskell_type_list", desc="haskell types")
ctx.lists["user.code_types"] = {
    "ref": "Ref",
    "effect": "Effect",
    "array": "Array",
    "boolean": "Boolean",
    "zipper": "Zipper",
    "either": "Either",
    "unit": "Unit",
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
    "hint map": "IntMap",
    "hint set": "IntSet",
}

# mod.list("code_operators", desc="haskell operators")
ctx.lists["user.code_extra_operators"] = {
    "bind left": "=<<",
    "bind right": ">>=",
    "map left": "<$>",
    "map right": "<#>",
    "beefy star": "<*>",
    "skip left": "<*",
    "skip right": "*>",
    "app left": "$",
    "app right": "#",
    "map end": "<>",
    "compose": "<<<",
    "apply": "$",
}

modules = {
    #       qualified, alias
    "set": ("Data.Set", "Set"),
    "map": ("Data.Map", "Map"),
    "prelude": ("Prelude", "Prelude"),
    "list": ("Data.List", "List"),
    "foldable": ("Data.Foldable", "Foldable"),
}

mod.list("haskell_module", desc="haskell modules")
ctx.lists["user.haskell_module"] = [s for (s,(q,a)) in modules.items()]

@mod.capture(rule="{self.haskell_module}")
def haskell_module(m) -> str: return modules[m.haskell_module][0]

@mod.capture(rule="{self.haskell_module}")
def haskell_module_alias(m) -> str: return modules[m.haskell_module][1]

@mod.action_class
class Actions:
    def haskell_test_action(name: str):
        """Test Action"""
        print(name)
    def haskell_import_module(name: str):
        """Import module unqualified"""
        actions.user.paste(f"import {modules[name][0]}")


@ctx.action_class("user")
class user_actions:
    def code_insert_function(text: str, selection: str):
        actions.insert(text + " ")

