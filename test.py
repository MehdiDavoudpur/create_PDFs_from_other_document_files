text = "This is an example string for splitting."
split_words = 3
words = text.split(" ")
pattern = r'\b\w+\b'
line_text = ""
for i in range(0, len(words), split_words):
    splited_words = words[i:i + split_words]
    for word in splited_words:
        line_text = line_text + word + ' '
    print(line_text)
    line_text = ""
