def SLW(str1):
    word = ""
    all_words = []
    str1 = str1 + " "
    for i in range(0, len(str1)):
        if(str1[i] != ' '):
            word = word + str1[i]
        else:
            all_words.append(word)
            word = ""

    small = large = all_words[0]


    for k in range(0, len(all_words)):
        if(len(small)>len(all_words[k])):
            small = all_words[k]
        if(len(large)<len(all_words[k])):
            large = all_words[k]
    return small, large


str1 = "hello, my name is hunain"
print("Original Strings:\n",str1)
small,large = SLW(str1)
print("\nSmallest word: " + small)
print("Largest word: "+large)

