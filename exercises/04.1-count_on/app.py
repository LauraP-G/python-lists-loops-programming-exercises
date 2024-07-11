my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]
new_list = [];

# Your code here
for element in my_list:
    if type(element) in (dict, list):
    #if type(item) == dict or type(item) == list:
        new_list.append(element)

print(new_list)

