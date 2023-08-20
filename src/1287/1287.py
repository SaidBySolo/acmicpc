from sys import setrecursionlimit
from typing import Literal

setrecursionlimit(10**5)

expr = input()
new_expr: str = ""

previous: Literal[
    "digit",
    "operator",
    "open_braket",
    "close_braket",
    "end",
    "",
] = ""
current: Literal[
    "digit",
    "operator",
    "open_braket",
    "close_braket",
    "end",
    "",
] = ""
expr += "e"
try:
    for w in expr:
        if w.isnumeric():
            current = "digit"
        if w in ["+", "-", "*", "/"]:
            current = "operator"
        if w == "(":
            current = "open_braket"
        if w == ")":
            current = "close_braket"
        if w == "e":
            current = "end"

        # Handle 00001
        if previous != "digit" and current == "digit":
            new_expr += "int('"

        if previous == "digit" and current != "digit":
            new_expr += "')"

        # Handle (+1)
        if previous == "open_braket" and current == "close_braket":
            raise SyntaxError

        # Handle +1
        if previous == "" and current == "operator":
            raise SyntaxError

        # handle (+1)
        if previous == "open_braket" and current == "operator":
            raise SyntaxError

        # Handle (3++3), 5**5
        if previous == "operator" and current == "operator":
            raise SyntaxError

        previous = current
        if not current == "end":
            new_expr += w

except:
    print("ROCK")
else:
    try:
        result = eval(new_expr.replace("/", "//"))
    except Exception:
        print("ROCK")
    else:
        print(result)
