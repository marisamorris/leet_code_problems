str1 = "planet"
str2 = "stardust"
str3 = "moon"


def reverse_in_place(str):
    print(str)
    # SOLUTION 1
    # new_string = str[::-1]

    # SOLUTION 2
    # convert string to list
    str_list = list(str)

    i = 0
    l = len(str_list) - 1

    while i < l:
        temp = str_list[i]

        str_list[i] = str_list[l]
        str_list[l] = temp

        i += 1
        l -= 1

    # convert reversed list back to string
    new_string = "".join(str_list)
    print(new_string)



reverse_in_place(str1)
reverse_in_place(str2)
reverse_in_place(str3)
