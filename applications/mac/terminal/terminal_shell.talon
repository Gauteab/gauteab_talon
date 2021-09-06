app: apple_terminal
app: iTerm2
not title: /VIM/
-
tag(): user.file_manager
tag(): user.git
tag(): terminal

# Actions
action(user.file_manager_open_parent): "cd ..\n"
action(app.tab_open): key(cmd-t)
action(app.tab_close): key(cmd-w)
action(app.tab_next): key(ctrl-tab)
action(app.tab_previous): key(ctrl-shift-tab)
action(app.window_open): key(cmd-n)
action(edit.page_down): key(command-pagedown)
action(edit.page_up): key(command-pageup)

# Commands
copy mode: key(cmd-shift-c)
remove: "rm "
move: "mv "
make dirk: "mkdir "
extract: "extract "
pan doc: "pandoc "
carol: "curl "
resume: "fg\n"
rerun: key(up enter)
rerun 2: key(up up enter)
cd: "cd "
cd up: "cd ..\n"
(cd|go) <user.directory>: "cd {directory}\n"
B root: "br\n"
brew install: "brew install "
edit: "vi "
editor: "vi\n"
edit file:
  insert("vi")
  key(enter space g)
list files: "l\n"
find file: key(ctrl-g)
find (his | history): key(ctrl-r)

talon log: "talon-log\n"
talon install: "talon-pip install "
talon repel: "talon-repl\n"

run Haskell: "runHaskell "
Haskell repel: "ghci\n"
Haskell demon: "ghcid -r -W "
ghc up: "ghcup"
ghc up set: "ghcup set"

helm live: "elm-live src/"
helm live main: "elm-live src/Main.elm\n"
java C:"javac "
java run:"java "

dash <user.letters>: " -{letters} "
dash dash <user.word>: " --{word}"
do {user.bash_command}: "{bash_command} "

(directory | dirt) {user.directory}: "{directory}"

# pure install: "spago install "
# pure run: "spago run "
# pure build: "spago build "
# pure bundle: "spago bundle-app --main Main --to "

{user.bash_command}: "{bash_command}"
move {user.directory}:
    "mv "
    insert(directory)
