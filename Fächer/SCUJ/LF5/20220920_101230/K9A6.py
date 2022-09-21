def countingStars(stars: int):
    for i in range(1, stars+1):
        if i != 0:
            print('*'*i)
    for i in range(stars-1, -1, -1):
        print('*'*i)


countingStars(10)
