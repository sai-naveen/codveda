file = open("sample.txt", "r")

text = file.read()
words = text.split()
count = len(words)

print("Total words:", count)

file.close()
