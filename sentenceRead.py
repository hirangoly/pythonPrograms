import sentenceHandling as sh

# open file
print 'open file'
f = open('file2.txt')
sentence = f.read()

# print break word
print 'break word'
words = sh.break_words(sentence)
print words

# print sorted words
print 'sorted words'
print sh.sorted_words(words)

# print first word of a sentence
print 'first word of a sentence'
print sh.first_word(words)

# print last word of a sentence
print 'last word of a sentence'
print sh.last_word(words)

# print sorted sentence
print 'sorted sentence'
print sh.sorted_sentence(sentence)

# print first and last word of sentence
print 'first and last word of sentence'
print sh.first_last_word_sentence(sentence)

# print first and last word of senetence after sorting
print 'first and last word of senetence after sorting'
print sh.first_last_sorted_word_sentence(sentence)
