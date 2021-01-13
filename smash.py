import time

from talon import Context, Module, actions, settings, ctrl
from typing import List

mod = Module()
mod.mode("dolphin", "dolphin")
ctx = Context()
# ctx.matches = r"""
# # mode: user.dolphin
# # title: /Dolphin/i
# """

smash_moves = {
    #(buttons, duration, delay after)
    "down": ("down", 1, 0),
    "up": ("up", 1, 0),
    "walk right": ("_ right", 20, 0),
    "walk left": ("_ left", 20, 0),
    "turn right": ("shift-right", 1, 5),
    "turn left": ("shift-left", 1, 5),
    "left": ("left", 5, 5),
    "lash": ("left", 15, 3),
    "right": ("right", 5, 9),
    "rash": ("right", 15, 3),
    "surf": ( "y 3 down-left-q", 1, 10),
    "wave": ( "y 3 down-right-q", 1, 10),

    "jump": ("y", 1, 4),
    "short": ("y", 1, 21),
    "leap": ("y", 4, 0),
    "skip": ("y right right right", 1, 1),
    "Walt": ("y left left left", 1, 1),

    "land": ("down z", 1, 10),

    "near": ("a", 1, 10),
    "fair": ("left-a 5 down 5 z", 1, 5),
    "bear": ("right-a 5 down 5 z", 1, 5),
    "shark": ("i 10 z", 1, 5),
    "tact": ("a", 1, 0),
    "grab": ("y z", 1, 8),
    "jab jab": ("a 3 a", 1, 30),
    "spike": ("k", 1, 0),
    "spin": ("y 5 a 20 down 5 z", 1, 1),
    "win": ("y 15 a 10 down z", 1, 22),
    # "take": ("y z", 1, 29),
    "smash": ("j", 1, 0),
    "bash": ("l", 1, 0),
    # tilt
    "slash": ("_ up up-a", 3, 32),
    "swipe": ("_ right right-a", 3, 10),
    "swot": ("_ left left-a", 3, 10),
    "poke": ("_ down down-a", 3, 20),
    # special
    "counter": ("down-b", 1, 0),
    "fall": ("down down", 1, 0),
    # defensive
    "block": ("q", 1, 10),
    "dodge": ("down-q", 1, 0),
    "roll": ("q q-left", 1, 0),
    "trip": ("q q-right", 1, 0),
    "panic": (("up-b 1 "*10)[:-1], 1, 0),

    "drop": ("down", 3, 2),
    "wave land": ("y 60 down-q", 1, 10),

}
mod.list("smash_moves", desc="smash moves")
ctx.lists["user.smash_moves"] = smash_moves.keys()

current = None
modifier = "g"

@mod.action_class
class Actions:
    def perform(moves: List[str]):
        ""
        print(moves)
        for m in moves:
            (b, duration, delay) = smash_moves[m]
            actions.user.input_string(b, duration)
            actions.user.sleep_frames(delay)

    def start_hold(input: str):
        ""
        global current
        if current:
            ctrl.key_press(current, down=False)
        ctrl.key_press(input, down=True)
        current = input

    def sleep_frames(frames: int):
        ""
        # actions.sleep(1/60*frames)
        actions.sleep(0.017*frames)

    def input_string(input: str, duration: int = 1):
        ""
        for x in input.split(" "):
            if x == "_":
                ctrl.key_press(modifier, down=True)
                continue
            try:
                actions.user.sleep_frames(int(x))
            except:
                actions.user.button(x, duration)
        ctrl.key_press(modifier, down=False)


    def input_list(input: List[str], duration: int = 1):
        ""
        for i in input:
            actions.user.input_string(i, duration)

    def button(input: str, duration: int = 1):
        "hold a button for a certain period of time"
        global current
        print(current)
        keys = input.split("-")
        for x in keys: ctrl.key_press(x, down=True)
        actions.user.sleep_frames(duration)
        for x in keys: ctrl.key_press(x, down=False)
        if current:
            ctrl.key_press(current, down=False)
            current = None


