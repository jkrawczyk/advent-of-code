# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

from ...base import TextSolution, answer
import re


class Solution(TextSolution):
    _year = 2024
    _day = 3

    @answer(189600467)
    def part_1(self) -> int:
        pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
        matches = pattern.findall(self.input)
        return sum([int(a) * int(b) for a, b in matches])

    @answer(107069718)
    def part_2(self) -> int:
        input = self.input
        pattern = re.compile(r"\n")
        input = pattern.sub("", input)
        pattern = re.compile(r"don't\(\).*?do\(\)")
        input = pattern.sub("XXX", input)
        pattern = re.compile(r"don't\(\).*?$")
        input = pattern.sub("XXX", input)
        pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
        matches = pattern.findall(input)

        return sum([int(a) * int(b) for a, b in matches])


    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
