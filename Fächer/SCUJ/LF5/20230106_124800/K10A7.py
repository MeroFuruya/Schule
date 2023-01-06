# quicksort

l = list(range(10))+list(range(3))
import random
random.shuffle(l)

# l = [5, 3, 6, 2, 9, 0, 1, 4, 8, 7]

def qsort(l: list) -> list:
    def _qsort(start: int, end: int):
        pivot: int = ((end - start-1) // 2) + start  #  - 1
        print("pivot:", pivot, "; start:", start, "; end:", end)
        i = start
        while i < end:
            if i < pivot:
                # wenn man links vom pivot element ist
                if l[i] > l[pivot]:
                    print(l[i], l[pivot])
                    # und der wert größer als das pivot el ist
                    # kommt es nach rechts
                    l.insert(pivot, l.pop(i))
                    # dadurch verschiebt sich das ursprüngliche pivot element nach links
                    pivot -= 1
                    i -= 1
            else:
                # wenn man rechts vom pivot el ist
                if l[i] < l[pivot]:
                    print(l[i], l[pivot])
                    # und der wert kleiner als das pivot el ist
                    # kommt es nach links
                    l.insert(pivot, l.pop(i))
                    # dadurch verschiebt sich das pivot element nach rechts
                    pivot += 1
            i += 1
        if pivot - start > 1:
            print("first ", start, pivot, l)
            _qsort(start, pivot)
        if end - pivot > 2:
            print("second", pivot, end, l)
            _qsort(pivot, end)
    # call sort func the first time :)
    _qsort(0, len(l))
                

print(l)
qsort(l)
print(l)
    
