
def reverse_text(text):
	reversed_text = ""
	character_count = len(text)
	for x in range(character_count, 0, -1):
		reversed_text += text[x - 1]
	return reversed_text

print("Reverse text here")
to_reverse = input("Enter text to reverse: ")
print(reverse_text(to_reverse))
