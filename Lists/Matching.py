def match(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
        
    print("Heres a list of words with the same first and last characters: \n", lst)
    return ctr

count = match(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("The number of words with the same first and last character is: ", count)