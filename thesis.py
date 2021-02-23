from talon import Context, Module, actions, settings, ctrl, app
from typing import Dict

module = Module()
context = Context()

# declare all symbol lists
symbols = { k:{} for k in
    [ "function"
    , "constructor"
    , "type"
    ]
}

# module.list("function", "function")
# module.list("constructor", "constructor")
# context.lists["self.function"] = {}
# context.lists["self.constructor"] = {}

for item in symbols.keys():
    module.list(item, item)
    context.lists[f"self.{item}"] = {}

@module.action_class
class Actions:

    def clear_symbols() -> str:
        "Clears the Symbols"
        for name in dictionary.keys():
            context.lists[f"self.{name}"] = {}

    def update_symbols(dictionary: Dict[str, Dict[str,str]]) -> str:
        "Updates the Symbols"
        app.notify("!")
        for (name, v) in dictionary.items():
            print("update", name, v)
            # symbols[name].update(v)
            # context.lists[f"self.{name}"] = symbols[name]
            context.lists[f"self.{name}"] = v


# Notes:
# update context from repl
# >>> user.thesis.context.lists["self.test"]={"test":"!"}
