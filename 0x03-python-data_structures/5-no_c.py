#!/usr/bin/python3
def no_c(my_string):
    str3 = my_string.split(" ")
    for i in range(len(my_string)):
        for j in range(len(my_string[i])):
            if my_string[i][j] == "c" or my_string[i][j] == "C":
                continue
            new = my_string[i]
            new2 = "".join(new)
            print(new)
    # return new
    #     if str3[0] == "C" or str3[0] == "c":
    #         str3.pop(i)
    #         continue
    # return str3
