def no_dups(s):
    words = s.split()
    wordset = []
    for word in words:
        if word not in wordset:
            wordset.append(word)
    return ' '.join(wordset)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))