def intToRoman(num):
    final_roman = ""
    int_num = num
    thisdict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
        4: "IV",
        9: "IX",
        40: "XL",
        90: "XC",
        400: "CD",
        900: "CM"
    }
    x = 0
    while(int_num != 0):
        highest = 0
        for key in thisdict.keys():
            if int_num - key >= 0:
                if(key > highest):
                    highest = key

        print("higest",highest)
        int_num= int_num - highest
        final_roman += thisdict[highest]

    return final_roman

print(intToRoman(1004))


