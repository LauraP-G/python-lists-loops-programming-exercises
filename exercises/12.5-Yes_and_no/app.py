the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here

def wiki_woko(list):
    if list == 1:
        return 'wiki'
    elif list ==0:
        return 'woko'
    

list_wiki_woko = list(map(wiki_woko, the_bools))

print(list_wiki_woko)