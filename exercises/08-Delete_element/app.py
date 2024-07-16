people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # Your code here
    #updated_people = list(people)
   
    updated_people = [name for name in people if name != person_name]
    return updated_people
    
    #for element in updated_people:
    #    if element == person_name :
    #        updated_people.remove(element)
    #return updated_people
    

   
   

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
