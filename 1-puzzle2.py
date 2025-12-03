"""Solution: Daniel Mishan - Dec 2, 2025

What did this puzzle teach me? It taught me that simple coding is never better to mathematical analysis. I should
implement my mathematical analysis into code since the problem is solvable without machines first."""

from typing import List

def instruction(s: str) -> int:
    """This instruction takes a string s of the form (R/L)# and returns a positive/negative number based on R/L."""

    if s[0] == "L":
        return -int(s[1:])
    elif s[0] == "R":
        return int(s[1:])
    return f"Invalid instruction {s}."

def load_instructions(filename: str) -> List[int]:
    with open(filename, "r") as f:
        instructions = []
        for line in f.readlines():
            instructions.append(line.strip())

    return instructions

def convert_instructions(instructions: List[int]) -> List[int]:
    converted_instructions = []
    for i in instructions:
        converted_instructions.append(instruction(i))
    return converted_instructions

def solve(puzzle_input):
    """This function uses numerical analysis and solves for the modular eqn pos + k = 0 mod 100.

    >>> solve(["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"])
    6
    >>> solve(["R51"])
    1
    >>> solve(["R50", "R100"])
    2
    >>> solve(["R1000"])
    10
    >>> solve(["L1000"])
    10
    >>> solve(["L51"])
    1
    >>> solve(["L50", "R100"])
    2

    """
    rotations = convert_instructions(puzzle_input)
    position = 50
    count = 0

    for step in rotations:
        direction = 1 if step > 0 else -1
        for _ in range(abs(step)):
            position = (position + direction) % 100
            if position == 0:
                count += 1

    return count