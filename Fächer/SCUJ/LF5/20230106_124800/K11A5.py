def foo(n: any) -> dict:
    r = {}
    if type(n) is int:
        r["vorzeichen"] = "positiv" if (n >= 0) else "negativ"
        r["parität"] = "gerade" if n % 2 == 0 else "ungerade"
    elif type(n) is float:
        r["vorzeichen"] = "positiv" if n >= 0 else "negativ"
        r["parität"] = "kein Integer"
    else:
        r["vorzeichen"] = "kein Integer"
        r["parität"] = "kein Integer"
    return r

print(foo(10))
print(foo(-11))
print(foo(0.1))
print(foo("a"))
        
