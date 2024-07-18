

# Your code above, nothing to change after this line



def lyrics_generator(list):
    result_lyrics= "";
    sum_one=0
    for element in list:
        if(element == 0):
            result_lyrics += "Boom "
        elif(element == 1):
            result_lyrics += "Drop the bass "
            sum_one += 1
            if sum_one == 3:
                result_lyrics+= "!!!Break the bass!!! "
                sum_one=0

    return result_lyrics

print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))


            
