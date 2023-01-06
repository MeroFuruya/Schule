
def all_combinations(n: int) -> None:
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            print(f"player {i} vs {j}")

all_combinations(3)

# one-liner (ok actually two liner *suffering noises*) for the flex hehe
def all_combinations(n: int) -> None:
    [print(f"player {i} vs {j}") for i in range(1, n+1) for j in range(i+1, n+1)]

all_combinations(3)


