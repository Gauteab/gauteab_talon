from talon import app, Module, Context, actions, ui, imgui
# from talon.voice import Capture
import re
import time
import os

mod = Module()
mod.list("bash_command", desc="")
mod.list("directory", desc="")
# @mod.capture
# def build_tool(m) -> Capture: ""
# @mod.capture
# def build_action(m) -> Capture: ""


overrides = {"pure": "spago", "repel": "repl", "helm": "elm", "in it": "init"}

local_overrides = {"cabal": {"build": "new-build",
                             "run": "new-run", "repl": "new-repl"}}

ctx = Context()

commands= {
    "make": ["watch\n", "clean\n", "build\n"]
}

def create_commands(dictionary):
    result = []
    for (k, v) in dictionary.items():
        if type(v) is str:
            result.append(f"{k} {v}")
        else:
            for v in v:
                result.append(f"{k} {v}")
    return result

ctx.lists["self.bash_command"] = create_commands(commands)
# ctx.lists["self.bash_command"] = {
#     "code down": "codedown",
#     "take": "take"
# }

# ctx.lists["self.build_tool"] = ["make",
#                                 "cabal", "stack", "pure", "cargo", "helm", "npm"]

# ctx.lists["self.tool_action"] = ["repel", "version", "start", "test", "clean", "watch",
#                                  "new", "run", "build", "install", "make", "in it"]

ctx.lists["self.directory"] = {
    "download": "~/Downloads"
}

# @ctx.capture(rule='{self.build_tool}')
# def build_tool(m): return overrides.get(m.build_tool, m.build_tool)


# @ctx.capture(rule='[test] {self.build_tool} {self.tool_action}')
# def build_action(m):
#     tool = overrides.get(m.build_tool, m.build_tool)
#     action = overrides.get(m.tool_action, m.tool_action)
#     action = local_overrides.get(tool, {}).get(action, action)
#     return f"{tool} {action} "
