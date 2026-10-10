from itertools import chain, combinations

s = {1, 2, 3}

power_set = list(
    chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
)

print("Power Set:")
for x in power_set:
    print(set(x))