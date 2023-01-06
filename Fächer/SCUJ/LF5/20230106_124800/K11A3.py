def supersearch(d: dict, value: any) -> bool:
    return value in list(d.values())

d = {"a": 1}

print(supersearch(d, 1))
print(supersearch(d, 2))

