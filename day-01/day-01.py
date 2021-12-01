depths = open("input.txt").read().split("\n")
depths = [int(a) for a in depths]

def part_one(depths: list) -> int:
    return num_increasing(depths)

def part_two(depths: list) -> int:
    return num_increasing([depths[x] + depths[x - 1] + depths[x - 2] for x in range(2, len(depths))])

def num_increasing(depths: list) -> int:
    return sum(depths[x] > depths[x - 1] for x in range(1, len(depths)))

print(part_one(depths))
print(part_two(depths))