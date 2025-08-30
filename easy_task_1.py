txt=input("Enter the paragraph") 

clean_txt=""                              #here we clean the text by removing punctuators.
for ct in txt.lower():
    if ct in "-_/\~’":
        clean_txt +=" "
    elif ct.isalnum() or ct.isspace():
        clean_txt += ct
    else:
        clean_txt += ""
    
t_x_t=clean_txt.split()                   #here we split the text into words.

dict1={}
for t in t_x_t:                           #here we count the frequency of words and then added to dictionary. (word as key & freq. as value)
    v1=t_x_t.count(t)
    dict1[t]=v1
    if dict1[t]==1:
        dict1.pop(t)

v2=list(dict1.values())                   #here we make a list of highest to lowest freq. having only UNIQUE values.
v2.sort(reverse=True)
lst1=list(dict.fromkeys(v2))

print("Top 3 most frequent words:")       #here we find the top 3 words occurs the most.
used = []
for freq in lst1:
    for word in dict1:
        if dict1[word] == freq:
            print(word,":",freq)
            used.append(word)
            if len(used) == 3:
                break
    if len(used) == 3:
        break
input("\nPress Enter to exit...")
