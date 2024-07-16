contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}

for element in contact.keys():
    print(f'{element}: {contact[element]}')

print(contact["fullname"])
# Your code here
print(list(contact.keys())[0])


