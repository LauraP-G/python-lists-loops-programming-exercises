names = ['Alice', 'Bob', 'Marry', 'Joe', 'Hilary', 'Stevia', 'Dylan']

def prepender(name):
    return "My name is: " + name
    
# Your code here
introduce = list(map(prepender, names))
print(introduce)
