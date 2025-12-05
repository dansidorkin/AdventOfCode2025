"""
Advent of Code 2020 - Day 2
Solution by Daniel Mishan
Date: December 3rd, 2025 - Dec 4th, 2025
Location: Bahia Resort in San Diego
"""

def janitor(filename):
    """The janitor cleans up the file content or list info and spits out a list of ranges.

    Precondition: File contains only 1 line.

    >>> janitor("./sample.txt")
    [(11, 22), (95, 115), (998, 1012)]


    """
    ranges = []
    if filename:
        with open(filename) as f:
            dirt = f.readline() # Acceptable, since only one line in the file.

    wiped = dirt.split(',') # Split by ranges (min_num - max_num)
    ranges = [tuple(int(x) for x in k.split('-')) for k in wiped] # beautiful one-liner.
    return ranges

def solve(filename):
    """This solve function takes in the puzzle input as a List[int] and returns the sum of all the invalid IDs.

    >>> solve("./sample.txt")
    [11, 22, 99, 1010]
    """

    bucket = janitor(filename)
    m = []
    for ranges in bucket:
        for k in range(ranges[0], ranges[1] + 1):
            if str(k)[len(str(k)) // 2:] == str(k)[:len(str(k)) // 2]:
                m.append(k)

    return sum(i for i in m)

def divisors(n):
    """
    >>> divisors(1)
    [1]
    >>> divisors(2)
    [1, 2]
    >>> divisors(3)
    [1, 3]
    >>> divisors(4)
    [1, 2, 4]
    >>> divisors(24)
    [1, 2, 3, 4, 6, 8, 12, 24]
    """
    divisor = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisor.append(i)
    return divisor

def splitter(n):
    """Split an integer into a list of integers. This splits by prime number factors. The groups of, say, a number with
    6 digits means I can split it into 2 groups of 3, 3 groups of 2, 6 groups of 1. The prime factors are 2,3,6. But,
    given a prime number such as 5, the only number of groups it can be split to is into groups of 1 and groups of 5.
    >>> splitter('11')
    [['1', '1'], ['11']]
    >>> splitter('222')
    [['2', '2', '2'], ['222']]
    >>> splitter('1021')
    [['1', '0', '2', '1'], ['10', '21'], ['1021']]

    """
    splitted = []
    decomposition = divisors(len(n))
    for i in decomposition:
        # Splits into equal sizes.
        subsplit = [n[x:x+i] for x in range(0,len(n),i)]
        splitted.append(subsplit)

    return splitted

def patterned(lst):
    """
    >>> patterned([10, 21])
    False
    >>> patterned(['2', '2', '2'])
    True
    >>> patterned([1])
    False
    """
    groups = len(lst)
    if len(lst) == 1:
        return False
    if all(lst[0] == lst[i] for i in range(groups)):
        return True
    return False

def combine(lst):
    return int(''.join(i for i in lst))




def solve_updated(filename):
    """This solve function takes in the puzzle input as a List[int] and returns the sum of all the invalid IDs with
    new rules.
    >>> solve_updated("./puzzle2_input.txt")
    """
    invalidID = []
    bucket = janitor(filename)
    for mops in bucket:
        for i in range(mops[0], mops[1] + 1):
            split = splitter(str(i))
            for k in split:
                if patterned(k):
                    invalidID.append(combine(k))
                    break

    return sum(id for id in invalidID)




if __name__ == '__main__':
    print(solve_updated("./puzzle2_input.txt"))