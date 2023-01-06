def get_max_length(l: list) -> int:
    max_len = 0
    for el in l:
        if len(el) > max_len:
            max_len = len(el)
    return max_len

stop = ["beenden", "stop", "ende", "e"]

d = {}

while True:
    land = input("Land: ")
    if land.lower() in stop: break
    stadt = input("Hauptstadt: ")
    if stadt.lower() in stop: break
    d[land] = stadt


laender = list(d.keys())
laender_max_len = get_max_length(laender)
staedte = list(d.values())
staedte_max_len = get_max_length(staedte)

print(f"     Land{' '*(laender_max_len-4)} | Stadt {' '*(staedte_max_len-5)}")

for i in range(len(d)):
    print(f"{i+1:3}. {laender[i] + (' '*(laender_max_len-len(laender[i])))} | {staedte[i] + (''*(staedte_max_len-len(staedte[i])))}")



