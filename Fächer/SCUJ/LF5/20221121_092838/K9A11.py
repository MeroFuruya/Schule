import random
random.seed()

rows = 6
seats = 9

loge_rows = 2
loge_seats = 9

vec_seats = []
vec_loge = []

for i in range(0, rows):
    vec_seats.append([])
    for j in range(0, seats):
        vec_seats[i].append(" ")

for i in range(0, loge_rows):
    vec_loge.append([])
    for j in range(0, loge_seats):
        vec_loge[i].append(" ")

fill_seats = random.randint(0, rows * seats)

for i in range(0, fill_seats):
    seat = random.randint(0, rows * seats)
    vec_seats[seat%rows][seat%seats] = "X"

fill_seats = random.randint(0, loge_rows * loge_seats)

for i in range(0, fill_seats):
    seat = random.randint(0, loge_rows * loge_seats)
    vec_loge[seat%loge_rows][seat%loge_seats] = "X"

print("".join(["Normale Sitze:\n[", "]\n[".join(["][".join(vec_seats[i]) for i in range(0, rows)]), "]\n\nLoge Sitze:\n[", "]\n[".join(["][".join(vec_loge[i]) for i in range(0, loge_rows)]), "]"]))


