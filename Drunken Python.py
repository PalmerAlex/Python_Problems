def int_to_str(num):
    str_num = int(num)
    return str_num

def str_to_int(num):
    return str(num)

if str(4) == '4' and int('4') == 4:
    print("true")

if int_to_str(4) == '4'and str_to_int('4') == 4:
    print("TRUE")