from importlib.resources import read_text
import re

def do_regex(input_string :str,pattern :str) -> int:

    matches = re.findall(pattern, input_string)
    return sum(int(x) * int(y) for x, y in matches)

def solve() -> tuple[int, int]:
    # Open puzzle input and strip new lines
    corrupted_memory :list = read_text("adventofcode.resources.2024", "03.txt").replace("\n","")

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    mul_total = do_regex(corrupted_memory,pattern)

    enabled_instruction_total :int = 0

    do_logic = corrupted_memory.split("do()")
    for dont_logic in do_logic:
        allowed_logic = dont_logic.split("don't()", 1)[0]

        enabled_instruction_total += do_regex(allowed_logic, pattern)

    return mul_total, enabled_instruction_total
