freq = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'coding' : 1}
word = input("Enter a word to find its frequnecy: ")

if word in freq:
    print("Frequency of", word, "is", freq[word])
else:
    print("This word is not in the dictionary")