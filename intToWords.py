def numberToWords(num):
    # up to 2 billion
    final_str = ""
    numberDict ={
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten"
    }
    num_to_str = str(num)
    x = 0
    while x < len(num_to_str):
        for key in numberDict.keys():
            if int(num_to_str[x]) in numberDict:
                final_str += numberDict[x]
        x+= 1
    print(final_str)
numberToWords(100)
