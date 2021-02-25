from talon import *
import http.client
from typing import Dict
import os
import subprocess

module = Module()
context = Context()

# declare all symbol lists
# symbols = { k:{} for k in
#     [ "function"
#     , "constructor"
#     , "type"
#     ]
# }
symbols = \
    [ "function"
    , "constructor"
    , "type"
    ]

module.list("symbol_type", "symbols of interest")
context.lists["self.symbol_type"] = symbols

@module.capture(rule="({user.function}|{user.type}|{user.constructor})")
def symbol_any(m) -> str: return m

# module.list("function", "function")
# module.list("constructor", "constructor")
# context.lists["self.function"] = {}
# context.lists["self.constructor"] = {}

for item in symbols:
    module.list(item, item)
    context.lists[f"self.{item}"] = {}

@module.action_class
class Actions:

    def print_symbols():
        "Print the symbols"
        print(context.lists)


    def navigate(target: str, type_: str):
        ""
        connection = http.client.HTTPConnection("localhost:8080")
        connection.request("GET", f"/navigate?file&target={target}&type={type_}&file={os.path.expanduser(actions.win.filename())}")
        response = connection.getresponse()
        # print(response.read().decode())
        print("Status: {} and reason: {}".format(response.status, response.reason))
        connection.close()

    def clear_symbols() -> str:
        "Clears the Symbols"
        for name in [x for x in context.lists.keys()]:
            context.lists[f"{name}"] = {}

    def update_symbols(dictionary: Dict[str, Dict[str,str]]) -> str:
        "Updates the Symbols"
        # app.notify("!")
        for (name, v) in dictionary.items():
            print("update", name, v)
            # symbols[name].update(v)
            # context.lists[f"self.{name}"] = symbols[name]
            context.lists[f"self.{name}"] = v


# Notes:
# update context from repl
# >>> user.thesis.context.lists["self.test"]={"test":"!"}
