regen = input("regnets?")
geld = int(input("wv geld hast du?"))
zahlen_freunde = input("zahlen deine freunde?")

answerlist = []
if regen == "n":
    answerlist.append("es regnet nicht")
if geld < 20 and zahlen_freunde == "n":
    answerlist.append("du hast kein zwanni und deine freunde zahlen nicht")
    

if len(answerlist) == 0:
    print("ab ins kino")
else: 
    print(f"zuhause, weil {' und '.join(answerlist)}")
