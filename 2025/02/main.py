#!/usr/bin/env python3

import argparse


def read_input(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        input_str = f.readlines()[0].strip()
    input_list = input_str.split(",")
    return input_list


def is_invalid(id: int) -> bool:
    id = str(id)

    if len(id) % 2 != 0:
        return False

    left, right = id[: len(id) // 2], id[len(id) // 2 :]
    if left == right:
        return True

    return False


def is_invalid_2(id: int) -> bool:
    id = str(id)

    for sublen in range(1, len(id) // 2 + 1):
        if len(id) % sublen != 0:
            continue

        chunks = [id[i : i + sublen] for i in range(0, len(id), sublen)]
        if len(set(chunks)) == 1:
            return True

    return False


def part1(input: list[str]) -> int:
    invalids = []

    for idr in input:
        start, end = [int(n) for n in idr.split("-")]
        for id in range(start, end + 1):
            if is_invalid(id):
                invalids.append(id)
    return sum(invalids)


def part2(input: list[str]) -> int:
    invalids = []

    for idr in input:
        start, end = [int(n) for n in idr.split("-")]
        for id in range(start, end + 1):
            if is_invalid(id) or is_invalid_2(id):
                invalids.append(id)
    return sum(invalids)


def main(input_file, part):
    input_str = read_input(input_file)

    match part:
        case 1:
            print(part1(input_str))
        case 2:
            print(part2(input_str))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Advent of Code 2025, Day 2:
    Take input file containing raw text input, and
    print out solution to either part 1 or part 2."""
    )
    parser.add_argument("input", type=str, help="Input text file path.")
    parser.add_argument("part", type=int, help="Which part to solve, either 1 or 2.")
    args = parser.parse_args()

    if args.part > 2 or args.part < 1:
        parser.error("`part` argument must be 1 or 2.")

    main(args.input, args.part)
