# Your code here
def matrix_builder(num_entero):
    matrix_list =[]
    for i in range(num_entero):
        row=[]
        for x in range(num_entero):
            row.append(1)
        matrix_list.append(row)

    return matrix_list


result = matrix_builder(3)

print(result)