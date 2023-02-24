# is included

import re

def is_included(s: str) -> bool:
    return re.search(".*funktioniert.*", s) is not None

print(is_included("aaaaaafunktioniertaaaaa"))
print(is_included("aaaaaafunktionieraaaaa"))

