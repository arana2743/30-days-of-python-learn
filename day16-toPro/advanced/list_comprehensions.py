# list comprehensions
# powerful way to create new list based on existing list
# all done in one readable line

# example: find length of all words in string
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split(' ')
word_length = [len(word) for word in words]
print(word_length)


# another example : filter out just positive numbers
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
pos_numbers = [num for num in numbers if num > 0]
print('All positive numbers are : %s' % pos_numbers)
