chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here
    list_empty=[]
    for name in list1:
        list_empty.append(name)

    for name in list2:
        list_empty.append(name)

    return list_empty

    
print(merge_list(chunk_one, chunk_two))
