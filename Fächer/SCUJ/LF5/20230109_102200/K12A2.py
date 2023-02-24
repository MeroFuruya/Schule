# nur ungerade

def nur_ungerade(l: list[int]) -> list[int]:
    return [i for i in l if i % 2 == 1]

print(nur_ungerade(list(range(10))))

