from talon import app, Module, Context, actions, ui, imgui
# from talon.voice import Capture
import re
import time
import os

mod = Module()
ctx = Context()

mod.list("bash_command", desc="")
mod.list("directory", desc="")

commands= {
    "make": ["watch\n", "clean\n", "build\n"],
    "npm": [("clean", "run clean\n"), "start\n", "install ", "version\n", ("build", "run build\n")],
    ("pure", "spago"): ["run\n", "version\n"]
}

def create_commands(dictionary):
    result = {}
    for (k, v) in dictionary.items():
        k_ = k if type(k) is str else k[0]
        k = k if type(k) is str else k[1]
        for v in v:
            if type(v) is str:
                result[f"{k_} {v}"] = f"{k} {v}"
            else:
                k2, v = v
                result[f"{k_} {k2}"] = f"{k} {v}"
    return result

ctx.lists["self.bash_command"] = create_commands(commands)
ctx.lists["self.directory"] = {
    "download": "~/Downloads"
}

