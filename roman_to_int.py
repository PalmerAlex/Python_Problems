def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    roman_string = s.upper()
    final_int = 0
    thisdict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    x = 0
    while x < len(s):
        print(thisdict[s[x]])

        if x + 1 < len(s):
            print("OK")
            pair = s[x] + s[x + 1]
            if pair in thisdict.keys():
                final_int += thisdict[pair]
                x += 1
            else:
                final_int += thisdict[s[x]]
        else:
            final_int += thisdict[s[x]]

        x += 1


    return final_int
