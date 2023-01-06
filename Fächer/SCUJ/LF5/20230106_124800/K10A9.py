# schlechter name but i do what i am told
def blablub(lis: list, obj: object) -> list:
    if obj not in lis:
        lis.append(obj)
    return obj

l = []

class test_obj:
    pass

print(l)
blablub(l, test_obj)
print(l)

