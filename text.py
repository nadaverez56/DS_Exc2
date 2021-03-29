def countword() -> int:
    file = open('text.txt')
    text = file.read()
    list_of_words=text.split()
    word = list_of_words[0]
    counter=0
    for i in range(1,len(list_of_words)):        
        rev=revword(list_of_words[i])
        if rev == word:
            counter+=1
    return counter+1     

def revword(word:str) -> str:
    st = ''.rstrip()
    for letter in range(0,len(word)):
        st = word[letter] + st
    return st.lower()


    