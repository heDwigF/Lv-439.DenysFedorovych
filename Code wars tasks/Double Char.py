def double_char(s):
    my_str =""
    my_list = []
    for i in s:
        i*=2
        my_list.append(i)
    my_str="".join(my_list)
    return my_str