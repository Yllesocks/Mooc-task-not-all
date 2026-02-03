text = input("Write text: ")

with open("wordlist.txt") as new_file:
	wordlist = []
	for line in new_file:
		line = line.strip()
		wordlist.append(line)

text = text.split(" ")
for word in text:
	if word.lower() in wordlist:
		print(word, end=" ")
	else:
		print(f"*{word}*", end=" ")
