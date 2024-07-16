my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

def max_integer(list):
    bigger_number=list[0]
    for number in list:
        if(number > bigger_number):
            bigger_number = number

    return bigger_number


# Your code here

print(max_integer(my_list))
