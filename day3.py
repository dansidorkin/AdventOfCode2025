"""
Advent of Code 2020 - Day 3
https://adventofcode.com/2025/day/3
Author: Daniel Mishan
Date: Dec 4th, 2025
Location: Bahia Resort San Diego, California
"""
import itertools
from day2 import combine


def optimize_bank(battery_line):
    """Get the best joltage from a bank by turning on 2 batteries. Translation: Find a pair of integers
    in a sequence of individual integers such that xy is the largest possible pair of integers.
    >>> optimize_bank("987654321111111")
    98
    >>> optimize_bank("818181911112111")
    92
    """
    joltage = 0
    for i in range(len(battery_line)):
        for j in range(i + 1, len(battery_line)):
            temp_joltage = int(battery_line[i] + battery_line[j])
            if temp_joltage > joltage:
                joltage = temp_joltage

    return joltage

def solve(filename):
    """Solve the problem of day 3 puzzle 1. Precondition: File name MUST exist."""
    total_joltage = 0
    with open(filename, "r") as file:
        for bank in file:
            total_joltage += optimize_bank(bank)

    return total_joltage

def generate_combinations(battery_line):
    """Suppose we have a battery line of length len(battery_line) and we want to turn on 12 switches. We care not for
    the numbers, so we will generate tuples here of length len(battery_line) with 1 for flipped switch and 0 otherwise.
    We will generate all such combinations."""
    return itertools.combinations(battery_line, 12)


def optimize_bank_twelve(battery_line):
    """This function works on the second part of day 3. Suppose that we have 12 switches to turn on instead of 2. Then,
    this problem translates to find the subsequence preserving order such that the number formed by the 12 digits
    is the largest. We need to find some common rules. Suggestion: randomly turn on 12, keep updating a variable.
    This will be a simulation.

    >>> optimize_bank_twelve("987654321111111")
    987654321111
    >>> optimize_bank_twelve("811111111111119")
    811111111119
    >>> optimize_bank_twelve("818181911112111")
    888911112111

    """
    joltage = 0
    for tuple in generate_combinations(battery_line):
        temporary = combine(tuple)
        print(temporary)
        if temporary > joltage:
            joltage = temporary

    print(joltage)
    return joltage

# This function would work but the O complexity is too large for an M4 Macbook with 48 unified memory...
def solve_twelve(filename):
    total_joltage = 0
    with open(filename, "r") as file:
        for bank in file:
            total_joltage += optimize_bank_twelve(bank)

    return total_joltage


def largest_k_digit_subsequence(s):
    n = len(s)
    k = 12
    to_remove = n - k  # Number of digits we must skip
    stack = []

    for digit in s:
        # While we can still remove digits AND
        # the current digit is larger than the top of stack AND
        # we have enough remaining digits to reach k
        while (to_remove > 0 and
               stack and
               stack[-1] < digit):
            stack.pop()
            to_remove -= 1

        stack.append(digit)

    # If we still need to remove digits, remove from the end
    return int(''.join(stack[:k]))


# We implement a greedy algorithm:
# Greedy didn't work from Claude.
def solve_three(filename):
    solution = 0
    with open(filename, "r") as file:
        for bank in file:
            print(largest_k_digit_subsequence(bank.strip()))
            solution += largest_k_digit_subsequence(bank.strip())

    return solution

def main():
    print(solve_three("./day3.txt"))

if __name__ == "__main__":
    main()
