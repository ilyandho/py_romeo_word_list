fhand = open('romeo.txt')
word_list = []
for line in fhand:
    # Make a temporary word list by spliting lines
    temp_list = line.strip().split(' ')

    for word in temp_list:
        # Check if word is not in the word_list already
        if word not in word_list:
            word_list.append(word)

# Sort the List using sorted() instead of .sort() to retain the origin list
sorted_list = sorted(word_list)

for word in sorted_list:
    print(word)
