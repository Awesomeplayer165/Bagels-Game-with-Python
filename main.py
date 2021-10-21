# main.py

secretNumber = "345"

numberOfGuesses = 0

while numberOfGuesses != 10:
	userInput = input("Enter a 3 digit number: ")
	if len(userInput) != 3: print("Enter a 3 digit number and try again"); continue

	for index, char in enumerate(userInput):
		if char in secretNumber and secretNumber[index] == char:
			print("Fermi")
		elif char in secretNumber and secretNumber[index] != char:
			print("Pico")
		else:
			print("Bagels")

	if secretNumber == userInput: print("You got it!"); exit()

	numberOfGuesses += 1

print("Out of guesses")