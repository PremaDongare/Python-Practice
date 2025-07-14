import string
sentence = input("Enter your sentence")

sentence = sentence.lower()

# remove puncuation

clean_sentence=""
for char in sentence:
    if char not in string.punctuation: # contain[, @,# etc]
        clean_sentence += char


words=clean_sentence.split()

word_count={}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print ("\nWord Frequencies:")
for word in sorted(word_count):
    print(word+":",word_count[word])