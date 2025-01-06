t: dict[str, int] = {
    "!" : 33,
    '"' : 34,
    "#" : 35,
    "$" : 36,
    "%" : 37,
    "&" : 38,
    "'" : 39,
    "(" : 40,
    ")" : 41,
    "*" : 42,
    "+" : 43,
    "," : 44,
    "-" : 45,
    "." : 46,
    "/" : 47,
    "0" : 48,
    "1" : 49,
    "2" : 50,
    "3" : 51,
    "4" : 52,
    "5" : 53,
    "6" : 54,
    "7" : 55,
    "8" : 56,
    "9" : 57,
    ":" : 58,
    ";" : 59,
    "<" : 60,
    "=" : 61,
    ">" : 62,
    "?" : 63,
    "@" : 64,
    "A" : 65,
    "a" : 65,
    "B" : 66,
    "b" : 66,
    "C" : 67,
    "c" : 67,
    "D" : 68,
    "d" : 68,
    "E" : 69,
    "e" : 69,
    "F" : 70,
    "f" : 70,
    "G" : 71,
    "g" : 71,
    "H" : 72,
    "h" : 72,
    "I" : 73,
    "i" : 73,
    "J" : 74,
    "j" : 74,
    "K" : 75,
    "k" : 75,
    "L" : 76,
    "l" : 76,
    "M" : 77,
    "m" : 77,
    "N" : 78,
    "n" : 78,
    "O" : 79,
    "o" : 79,
    "P" : 80,
    "p" : 80,
    "Q" : 81,
    "q" : 81,
    "R" : 82,
    "r" : 82,
    "S" : 83,
    "s" : 83,
    "T" : 84,
    "t" : 84,
    "U" : 85,
    "u" : 85,
    "V" : 86,
    "v" : 86,
    "W" : 87,
    "w" : 87,
    "X" : 88,
    "x" : 88,
    "Y" : 89,
    "y" : 89,
    "Z" : 90,
    "z" : 90,
    "[" : 91,
    "]" : 93,
    "^" : 94,
    "_" : 95,
}
base: int = 113
modulo: int = 4294967296

def multmod(a: int) -> int:
    r: int = (a * base) % modulo
    r = round(r)
    return r

def powermod(k: int) -> int:
    r: int = 1
    if k == 0:
        return r
    for _ in range(k):
        r = multmod(r)
    return r

def hashgen(s: str) -> str:
    val: int = 0
    k: int = 0
    l: int = len(s)
    while k < l:
        val = val + (t[s[-k-1]] * powermod(k))
        k = k + 1
    val = val % modulo
    val = round(val)
    val = str(val)
    for _ in range(10 - len(val)):
        val = "0" + val
    return val

'''
def test():
    print(hashgen("BLUEPRINT_3134") == "1245775007")
    print(hashgen("UI_TT_DM_GE_WIRBELWIND_NAME") == "1374287734")
    print(hashgen("UI_TT_DM_GE_WIRBELWIND_PROPERTIES_1") == "0002633250")
    print(hashgen("UI_TT_DM_GE_WIRBELWIND_MOD_3A") == "0069236184")
'''