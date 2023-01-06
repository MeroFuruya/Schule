
passwords = ["ababa", "baab", "sdiopc", "ajkwei", "bab"]

def prt_pw(pw_list: list):
    allowed_chars = ["ab", "ba"]
    for pw in pw_list:
        for allowed_char in allowed_chars:
            if allowed_char in pw:
                print(pw)
                break

prt_pw(passwords)


