def all_combinations(n: int) -> None:
    print("\n".join([f"Player {i} vs {j}" for i in range(1, n+1) for j in range(i+1, n+1)]))

all_combinations(3)

