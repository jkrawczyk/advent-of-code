# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from ...base import StrSplitSolution, answer
from collections import Counter


class Solution(StrSplitSolution):
    _year = 2024
    _day = 4

    @answer(2644)
    def part_1(self) -> int:
        sum = 0
        for j in range(len(self.input)):
            for i in range(len(self.input[0])):
                if self.input[i][j] == "X":
                    sum += self.searchXMASes(i, j)
        return sum
    
    @answer(1952)
    def part_2(self) -> int:
        As = []
        for j in range(len(self.input)):
            for i in range(len(self.input[0])):
                if self.input[i][j] == "M":
                    As.extend(self.searchDiagonalMASes(i, j))

        counter = Counter(As)
        return sum([1 for item, count in counter.items() if count > 1])

    def searchXMASes(self, x: int, y: int) -> int:
        sum = 0
        if x >= 3 and self.input[x-1][y] == 'M' and self.input[x-2][y] == 'A' and self.input[x-3][y] == 'S':
            sum += 1
        if x < len(self.input) - 3 and self.input[x+1][y] == 'M' and self.input[x+2][y] == 'A' and self.input[x+3][y] == 'S':
            sum += 1
        if y >= 3 and self.input[x][y-1] == 'M' and self.input[x][y-2] == 'A' and self.input[x][y-3] == 'S':
            sum += 1
        if y < len(self.input[0]) - 3 and self.input[x][y+1] == 'M' and self.input[x][y+2] == 'A' and self.input[x][y+3] == 'S':
            sum += 1
        if x >= 3 and y >= 3 and self.input[x-1][y-1] == 'M' and self.input[x-2][y-2] == 'A' and self.input[x-3][y-3] == 'S':
            sum += 1
        if x >= 3 and y < len(self.input[0]) - 3 and self.input[x-1][y+1] == 'M' and self.input[x-2][y+2] == 'A' and self.input[x-3][y+3] == 'S':
            sum += 1
        if x < len(self.input) - 3 and y >= 3 and self.input[x+1][y-1] == 'M' and self.input[x+2][y-2] == 'A' and self.input[x+3][y-3] == 'S':
            sum += 1
        if x < len(self.input) - 3 and y < len(self.input[0]) - 3 and self.input[x+1][y+1] == 'M' and self.input[x+2][y+2] == 'A' and self.input[x+3][y+3] == 'S':
            sum += 1
        return sum
        
    def searchDiagonalMASes(self, x: int, y: int) -> list[tuple[int, int]]:
        As = []
        if x >= 2 and y >= 2 and self.input[x-1][y-1] == 'A' and self.input[x-2][y-2] == 'S':
            As.append((x-1, y-1))
        if x >= 2 and y < len(self.input[0]) - 2 and self.input[x-1][y+1] == 'A' and self.input[x-2][y+2] == 'S':
            As.append((x-1, y+1))
        if x < len(self.input) - 2 and y >= 2 and self.input[x+1][y-1] == 'A' and self.input[x+2][y-2] == 'S':
            As.append((x+1, y-1))
        if x < len(self.input) - 2 and y < len(self.input[0]) - 2 and self.input[x+1][y+1] == 'A' and self.input[x+2][y+2] == 'S':
            As.append((x+1, y+1))
        return As
    
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
