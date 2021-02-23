from talon import Context, Module, actions, settings, ctrl

mod = Module()
ctx = Context()

mod.list("tex_simple_commands", desc="tex_simple_commands")
ctx.lists["user.tex_simple_commands"] = [ "subfile", "label", "chapter", "part", "section",  "subsubsection", "subsection", "paragraph", "subparagraph", "item"]

mod.list("tex_text_commands", desc="tex_text_commands")
ctx.lists["user.tex_text_commands"] = {"bold": "textbf", "italic": "textit", "color": "textcolor{red}"}

mod.list("tex_target", desc="tex_target")
ctx.lists["user.tex_target"] = ["text", "itemize", "tabular", "center", "minted"]

@mod.scope
def scope():
    return {
        "test": "value",
    }

mod.list("tex_snippets", desc="tex_snippets")
ctx.lists["user.tex_snippets"] = {
    "subfile":"subfile",
    "section":"sec" ,
    "paragraph":"par",
    "chapter":"cha",
    "subsection": "sub",
    "begin": "begin",
    "table": "table",
    "minted": "mint",
    "elm example": "elmexample"
}

@mod.action_class
class Actions:
    def tex_begin(name: str):
        """begin block"""
        actions.insert("begin")
        actions.key("tab")
        actions.sleep(0.1)
        actions.insert(name)
        actions.key("escape o")
    def tex_command(name: str):
        """\\something{}"""
        actions.insert(f"\\{name}{{}}")
        actions.edit.left()
