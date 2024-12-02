# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(1889772)
    def part_1(self) -> int:
        col1 = [int(line.split()[0]) for line in self.input]
        col2 = [int(line.split()[1]) for line in self.input]
        
        col1.sort()
        col2.sort()
        
        sum = 0
        for i in range(len(col1)):
            sum += abs(col1[i] - col2[i])
        return sum

    @answer(23228917)
    def part_2(self) -> int:
        col1 = [int(line.split()[0]) for line in self.input]
        col2 = [int(line.split()[1]) for line in self.input]

        sum = 0
        for i in range(len(col1)):
            sum += col1[i] * col2.count(col1[i])
        return sum

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
