from talon import *
import http.client
from typing import Dict
import os
import subprocess
import json

module = Module()
context = Context()

# declare all symbol lists
# symbols = { k:{} for k in
#     [ "function"
#     , "constructor"
#     , "type"
#     ]
# # }
# symbols = \
#     [ "function"
#     , "constructor"
#     , "type"
#     ]

# module.list("symbol_type", "symbols of interest")
# context.lists["self.symbol_type"] = symbols

# @module.capture(rule=f'({("|".join( f"{{user.{s}}}" for s in symbols ))})')
# def identifier(m) -> str: return m

# module.list("function", "function")
# module.list("constructor", "constructor")
# context.lists["self.function"] = {}
# context.lists["self.constructor"] = {}

# for item in symbols:
#     module.list(item, item)
#     context.lists[f"self.{item}"] = {}

BASE_URL = "localhost:8080"

def request_GET(url: str):
    connection = http.client.HTTPConnection(BASE_URL)
    connection.request("GET", url)
    response = connection.getresponse()
    print("Status: {} and reason: {}".format(response.status, response.reason))
    result = json.loads(response.read()) if response.status == 200 else None
    print(result)
    connection.close()
    return result

def document_query(file: str, target: str, type_: str):
    line, column = actions.user.editor_get_cursor_position()
    return request_GET(f"/document-query?file&target={target}&type={type_}&file={os.path.expanduser(actions.win.filename())}&line={line}&column={column}")

def next_result(direction):
    return request_GET(f"/cycle-result?direction={direction}")

def navigate_to_node_start(node):
    actions.user.editor_go_to_position(node["startPosition"]["row"]+1, node["startPosition"]["column"])

@module.action_class
class editor_actions:

    def editor_get_cursor_position() -> int:
        "get the position of the cursor. e.g: (12, 13)"

    def editor_get_file_path() -> str:
        "get the full file path for the file being currently edited"
        # return os.path.expanduser(actions.win.filename())

    def editor_go_to_position(row: int, column: int):
        "navigate to the given position in the editor"

    def editor_select_range(line1: int, column1: int, line2: int, column2: int):
        "marks the given range in the editor"

@module.action_class
class Actions:
    def symbol_select_parent(target: str):
        ""
        line, column = actions.user.editor_get_cursor_position()
        file = actions.user.editor_get_file_path()
        node = request_GET(f"/select-parent?target={target}&file={file}&line={line}&column={column}")
        navigate_to_node_start(node)
    def print_cursor():
        ""
        cursor = actions.user.editor_get_cursor_position()
        print(cursor)
    def print_symbols():
        "Print the symbols"
        print(context.lists)

    def go_to_next_result(direction: str = "forward"):
        ""
        node = next_result(direction)
        navigate_to_node_start(node)

    def symbol_select(target: str, type_: str):
        ""
        file = actions.user.editor_get_file_path()
        node = document_query(file, target, type_)
        start = node["startPosition"]
        end = node["endPosition"]
        actions.user.editor_select_range(start["row"]+1, start["column"], end["row"]+1, end["column"])

    def symbol_navigate(target: str, type_: str):
        ""
        file = actions.user.editor_get_file_path()
        node = document_query(file, target, type_)
        navigate_to_node_start(node)

    def clear_symbols():
        "Clears the Symbols"
        print("clearing symbols")
        context.lists = {}

    def update_symbols(dictionary: Dict[str, Dict[str,str]]) -> str:
        "Updates the Symbols"
        print(dictionary.keys())
        for (name, v) in dictionary.items():
            print("update", name, v)
            module.list(name, name)
            context.lists[f"self.{name}"] = v

        @module.capture(rule=f'({("|".join( f"{{user.{s}}}" for s in dictionary.keys() ))})')
        def identifier(m) -> str: return m

# Notes:
# update context from repl
# >>> user.thesis.context.lists["self.test"]={"test":"!"}
# get index (offset by 1): :echo wordcount().cursor_chars 
