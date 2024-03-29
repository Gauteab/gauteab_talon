import sys

from typing import Set

from talon import Context, Module, actions, app

# My experience:
#   fine - conflicts with find
#   jury  - suddenly always matching with three or tree
#   pit  - conflicts with page
#   yank - conflicts with vim command
default_alphabet = "air brat cap dark each far guest harp ink Jack Kate look made near out pit quench red sir trap urge verb who plex yank said".split(" ")
letters_string = "abcdefghijklmnopqrstuvwxyz"

default_digits = "zero one two three four five six seven eight nine".split(" ")
numbers = [str(i) for i in range(10)]
default_f_digits = (
    "one two three four five six seven eight nine ten eleven twelve".split(" ")
)

mod = Module()
mod.list("letter", desc="The spoken phonetic alphabet")
mod.list("symbol_key", desc="All symbols from the keyboard")
mod.list("arrow_key", desc="All arrow keys")
mod.list("number_key", desc="All number keys")
mod.list("modifier_key", desc="All modifier keys")
mod.list("function_key", desc="All function keys")
mod.list("special_key", desc="All special keys")
mod.list("punctuation", desc="words for inserting punctuation into text")


@mod.capture(rule="{self.modifier_key}+")
def modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(m.modifier_key_list)


@mod.capture(rule="{self.arrow_key}")
def arrow_key(m) -> str:
    "One directional arrow key"
    return m.arrow_key


@mod.capture(rule="<self.arrow_key>+")
def arrow_keys(m) -> str:
    "One or more arrow keys separated by a space"
    return str(m)


@mod.capture(rule="{self.number_key}")
def number_key(m) -> str:
    "One number key"
    return m.number_key


@mod.capture(rule="{self.letter}")
def letter(m) -> str:
    "One letter key"
    return m.letter


@mod.capture(rule="{self.letter}")
def upper_letter(m) -> str:
    "Return one upper case"
    return m.letter.upper()


@mod.capture(rule="{self.letters}")
def letters(m) -> str:
    "Multiple letter keys"
    return m.letters


@mod.capture(rule="{self.special_key}")
def special_key(m) -> str:
    "One special key"
    return m.special_key


@mod.capture(rule="{self.symbol_key}")
def symbol_key(m) -> str:
    "One symbol key"
    return m.symbol_key


@mod.capture(rule="{self.function_key}")
def function_key(m) -> str:
    "One function key"
    return m.function_key


@mod.capture(
    rule="( <self.letter> | <self.number_key> | <self.symbol_key> "
    "| <self.arrow_key> | <self.function_key> | <self.special_key> )"
)
def unmodified_key(m) -> str:
    "A single key with no modifiers"
    return str(m)


@mod.capture(rule="{self.modifier_key}* <self.unmodified_key>")
def key(m) -> str:
    "A single key with optional modifiers"
    try:
        mods = m.modifier_key_list
    except AttributeError:
        mods = []
    return "-".join(mods + [m.unmodified_key])


@mod.capture(rule="<self.key>+")
def keys(m) -> str:
    "A sequence of one or more keys with optional modifiers"
    return " ".join(m.key_list)


@mod.capture(rule="{self.letter}+")
def letters(m) -> str:
    "Multiple letter keys"
    return "".join(m.letter_list)


ctx = Context()
ctx.lists["self.modifier_key"] = {
    # If you find 'alt' is often misrecognized, try using 'alter'.
    "alt": "alt",  #'alter': 'alt',
    "command": "cmd",
    "control": "ctrl",  #'troll':   'ctrl',
    "option": "alt",
    "shift": "shift",  #'sky':     'shift',
    "super": "super",
}
alphabet = dict(zip(default_alphabet, letters_string))
ctx.lists["self.letter"] = alphabet

# `punctuation_words` is for words you want available BOTH in dictation and as
# key names in command mode. `symbol_key_words` is for key names that should be
# available in command mode, but NOT during dictation.
punctuation_words = {
    # TODO: I'm not sure why we need these, I think it has something to do with
    # Dragon. Possibly it has been fixed by later improvements to talon? -rntz
    "`": "`",
    ",": ",",  # <== these things
    "back tick": "`",
    "comma": ",",
    "period": ".",
    "semicolon": ";",
    "colon": ":",
    "forward slash": "/",
    "question mark": "?",
    "exclamation mark": "!",
    "exclamation point": "!",
    "dollar sign": "$",
    "asterisk": "*",
    "hash sign": "#",
    "number sign": "#",
    "percent sign": "%",
    "at sign": "@",
    "and sign": "&",
    "ampersand": "&",
}
symbol_key_words = {
    "grave": "`",
    "comma": ",",
    "dot": ".",
    "point": ".",
    "space": " ",
    "void": " ",
    "semi": ";",
    "tick": "'",
    "lock": "[",
    "square": "[",
    "rock": "]",
    "slash": "/",
    "bish": "\\",
    "minus": "-",
    "dash": "-",
    "equals": "=",
    "plus": "+",
    "question": "?",
    "tilde": "~",
    "bang": "!",
    "dollar": "$",
    "score": "_",
    "colon": ":",
    "coal": ":",
    "lub": "(",
    "paren": "(",
    "rub": ")",
    "lace": "{",
    "race": "}",
    "angle": "<",
    "langle": "<",
    "rangle": ">",
    "star": "*",
    "hash": "#",
    "percent": "%",
    "cent": "%",
    "caret": "^",
    "at sign": "@",
    "swirl": "@",
    "amper": "&",
    "pipe": "|",
    "quote": '"',
}

# make punctuation words also included in {user.symbol_keys}
symbol_key_words.update(punctuation_words)
ctx.lists["self.punctuation"] = punctuation_words
ctx.lists["self.symbol_key"] = symbol_key_words
ctx.lists["self.number_key"] = dict(zip(default_digits, numbers))
ctx.lists["self.arrow_key"] = {
    "down": "down",
    "left": "left",
    "right": "right",
    "up": "up",
}


simple_keys = [
    # "end",
    # "enter",
    "escape",
    # "home",
    # "insert",
    "pagedown",
    "pageup",
    "space",
    "tab",
]

alternate_keys = {
    "backspace": "backspace",
    "forward delete": "delete",
    "junk": "backspace",
    "nuke": "delete",
}
# mac apparently doesn't have the menu key.
if app.platform in ("windows", "linux"):
    alternate_keys["menu key"] = "menu"

keys = {k: k for k in simple_keys}
keys.update(alternate_keys)
ctx.lists["self.special_key"] = keys
ctx.lists["self.function_key"] = {
    f"F {default_f_digits[i]}": f"f{i + 1}" for i in range(12)
}


@mod.action_class
class Actions:
    def get_alphabet() -> dict:
        """Provides the alphabet dictionary"""
        return alphabet
