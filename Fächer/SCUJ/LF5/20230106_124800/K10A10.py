# print every number from 0 to n in 0.1 steps
def ptr_to_n(n: float):
    for i in range(0, int(n)):
        for j in range(10):
            print(f"{i}.{j}")
    for i in range(int(n*10)-(int(n)*10)+1):
        print(f"{int(n)}.{i}")
ptr_to_n(10.1)



