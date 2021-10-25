
import time

from talon import Context, Module, actions, settings, ctrl
from typing import List

mod = Module()
mod.mode("global", "global")
ctx = Context()

mod.list("global_stuff", desc="global stuff")
ctx.lists["user.global_stuff"] = {
    # "todo": "TODO",
    # "init": "init",
    # "json":"!",
    # "Jason":"!",
    # "msg":"!"
}

