# -------------------------------#
# ========== SETTINGS ========== #
# -------------------------------#

# Pressure levels contributed by valves when closed.
all_valves = [1, 1, 1, 1, 4, 4, 4, 4, 10, 10, 10, 10]  # default = [1, 1, 1, 1, 4, 4, 4, 4, 10, 10, 10, 10]

# Pressure levels contributed by valves which are stuck closed.
stuck_valves = [10]  # default = [10]

# Required pressure level.
target_pressure = 19  # default = 19

# -------------------------------#
# ========== INTERNAL ========== #
# -------------------------------#


def main():
    import itertools

    from collections import Counter

    def contains_all(x, y):
        return not (Counter(y) - Counter(x))

    sols = []

    for i in range(1 + len(all_valves)):
        for combo in dict.fromkeys(itertools.combinations(all_valves, i)):
            if sum(combo) == target_pressure and contains_all(combo, stuck_valves):
                sol = sorted(combo)
                diff = sorted(all_valves)
                for e in sol:
                    diff.remove(e)
                sols.append(f'Open: {diff}\nClosed: {sol}')

    print('\n\n'.join(sols))


if __name__ == '__main__':
    main()
