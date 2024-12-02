# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    @answer(279)
    def part_1(self) -> int:
        lists = self.input
        print(lists)
        sum = 0
        for numbers in lists:
            numbers = numbers.split()
            pairs = zip(numbers, numbers[1:])
            diffs = [(int(a) - int(b)) for a, b in pairs]
            if (all(x > 0 and x < 4 for x in diffs)):
                sum += 1
            elif (all(x > -4 and x < 0 for x in diffs)):
                sum += 1
        return sum
        
    @answer(343)
    def part_2(self) -> int:
        lists = self.input
        total = 0
        for numbers in lists:
            numbers = numbers.split()
            numbers = [int(x) for x in numbers]
            total += self.check(numbers, 0)
        return total

    def check(self, numbers, depth):
        pairs = zip(numbers, numbers[1:])
        diffs = [(int(a) - int(b)) for a, b in pairs]
        if (depth == 2):
            return 0
        if (all(x > 0 and x < 4 for x in diffs)):
            return 1
        elif (all(x > -4 and x < 0 for x in diffs)):
            return 1
        else:
            for i in range(len(numbers)):
                new_numbers = numbers[:i] + numbers[i+1:]
                if self.check(new_numbers, depth + 1) == 1:
                    return 1
            return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
