"""
Author: Daniel Mishan
Date: 2025-12-05
Location: Bahia Resort San Diego, California
Update: 2025-12-13
Location: Pasadena Hotel & Pool, Los Angeles, California
"""
from pygments.lexers import j


def main():
    lines = []
    with open("day4puzzle.txt", "r") as f:
        for line in f:
            lines.append(line.strip())
    reline = lines.copy()
    newline = []
    for line in reline:
        newline.append(line.strip('\n'))

    removables = 0
    print(f"Stats: length {len(lines)}")
    # Check corners, only 4.
    for i in range(len(newline)):
        for j in range(len(newline[i])):
            if i == 0 or i == len(newline) - 1: # First or last row
                if j == 0 or j == len(newline[i]) - 1: # Corner condition
                    if lines[i][j] == "@":
                        removables += 1
                        print(f"Corner at ({i},{j}) is removable")


    # Central code is OK.
    for i in range(len(newline)):
        for j in range(len(newline[i])):
            if 0 < i < len(newline) - 1 and 0 < j < len(newline[i]) - 1:
                if lines[i][j] == "@":
                    grid_check = -1
                    for k in range(j-1, j+2):
                        if newline[i][k] == "@":
                            grid_check += 1
                        if newline[i-1][k] == "@":
                            grid_check += 1
                        if newline[i+1][k] == "@":
                            grid_check += 1

                    if grid_check <= 3:
                        print(f"Central at ({i},{j}) is removable because grid-check is {grid_check}")
                        removables += 1

    # edge lines
    for i in [0, len(newline) - 1]:
        if i == 0:
            for j in range(1, len(newline[i])):
                if lines[i][j] == "@":
                    grid_check = -1
                    for k in range(j - 1, j + 2):
                        if newline[0][k] == "@":
                            grid_check += 1
                        if newline[1][k] == "@":
                            grid_check += 1
                    if grid_check <= 3:
                        removables += 1
                        print(f"Edge at ({i},{j}) is removable because grid-check is {grid_check}")

        if i == len(newline) - 1:
            for j in range(1, len(newline[i]) - 1):
                if lines[i][j] == "@":
                    grid_check = -1
                    for k in range(j - 1, j + 2):
                        if newline[len(newline) - 1][k] == "@":
                            grid_check += 1
                        if newline[len(newline) - 2][k] == "@":
                            grid_check += 1
                    if grid_check <= 3:
                        removables += 1
                        print(f"Edge at ({i},{j}) is removable because grid-check is {grid_check}")

    # first column
    for i in range(1, len(newline) - 1):
        if lines[i][0] == "@":
            grid_check = -1
            if lines[i][0] == "@":
                grid_check += 1
            if lines[i][1] == "@":
                grid_check += 1
            if lines[i-1][0] == "@":
                grid_check += 1
            if lines[i+1][0] == "@":
                grid_check += 1
            if lines[i-1][1] == "@":
                grid_check += 1
            if lines[i+1][1] == "@":
                grid_check += 1
            if grid_check <= 3:
                removables += 1
                print(f"Edge line 0 ({i},{0}) is removable because grid-check is {grid_check}")
    # last column
    for i in range(1, len(newline) - 2):
        if newline[i][len(newline[i]) - 1] == "@":
            grid_check = -1
            if newline[i][len(newline[i]) - 1] == "@":
                grid_check += 1
            if newline[i][len(newline[i]) - 2] == "@":
                grid_check += 1
            if newline[i-1][len(newline[i]) - 1] == "@":
                grid_check += 1
            if newline[i+1][len(newline[i]) - 1] == "@":
                grid_check += 1
            if newline[i-1][len(newline[i]) - 2] == "@":
                grid_check += 1
            if newline[i+1][len(newline[i]) - 2] == "@":
                grid_check += 1
            if grid_check <= 3:
                removables += 1
                print(f"Edge line {len(newline[i]) - 1} ({i}, {len(newline[i]) - 1}) is removable because grid-check is {grid_check}")

    # Bottom row:


    return removables

if __name__ == "__main__":
    print(main())