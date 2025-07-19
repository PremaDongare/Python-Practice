import string

filename = input("Enter file name with .txt: ")

try:
    # Open and read the file
    with open(filename, 'r') as file:
        content = file.read()

    # Count lines
    with open(filename, 'r') as file:
        lines = file.readlines()
        linecount = len(lines)

    # Clean content
    content = content.lower()
    clean_content = ""
    for char in content:
        if char not in string.punctuation:
            clean_content += char

    # Count words
    words = clean_content.split()
    count = len(words)

    # Count word frequency
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    print(f"Total lines: {linecount}")
    print(f"Total words: {count}")
    print("\nWord Frequency:")
    for word in sorted(word_freq):
        print(f"{word}: {word_freq[word]}")

except FileNotFoundError:
    print(" File not found. Please check the filename and try again.")
