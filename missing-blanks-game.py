# IPND Stage 2 Final Project v5

difficulty = ["easy", "medium", "hard"]

easy_text = """___1___ is a high-level, structured, open-___2___ programming language that can be used for a wide variety of ___3___ tasks. 
Python was created by Guido Van Rossum in the early 1990s, its following has grown steadily and interest is increased markedly in the last 
few years or so. It is named after ___4___ Python's Flying Circus comedy program."""
easy_answers = ["Python", "source", "programming", "Monty"]
easy_blanks = ["___1___", "___2___", "___3___", "___4___"]

medium_text = """___1___ is a high-level, structured, open-___2___ programming language that can be used for a wide variety of ___3___ tasks. 
Python was created by Guido Van Rossum in the early 1990s, its following has grown steadily and interest is increased markedly in the last 
few years or so. It is named after ___4___ Python's Flying Circus comedy program. Python is used extensively for ___5___ administration 
(many vital components of Linux Distributions are written in it), also its a great language to ___6___ programming to novices. NASA has 
used Python for its software systems and has adopted it as the standard ___7___ language for its Integrated Planning System. Python is 
also extensively used by Google to implement many components of its web crawler and ___8___ engine & Yahoo! for managing its 
discussion groups."""
medium_answers  = ["Python", "source", "programming", "Monty", "system", "teach", "scripting", "search"]
medium_blanks = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___", "___7___", "___8___"]

hard_text = """___1___ is a high-level, structured, open-___2___ programming language that can be used for a wide variety of ___3___ tasks. 
Python was created by Guido Van Rossum in the early 1990s, its following has grown steadily and interest is increased markedly in the last 
few years or so. It is named after ___4___ Python's Flying Circus comedy program. Python is used extensively for ___5___ administration 
(many vital components of Linux Distributions are written in it), also its a great language to ___6___ programming to novices. NASA has 
used Python for its software systems and has adopted it as the standard ___7___ language for its Integrated Planning System. Python is 
also extensively used by Google to implement many components of its web crawler and ___8___ engine & Yahoo! for managing its 
discussion groups. Python within itself is an interpreted programming ___9___ that is automatically compiled into ___10___ before 
execution. It is also a dynamically typed language that includes (but does not require one to use) ___11___ oriented features and 
constructs. The most unusual aspect of Python is that whitespace is significant; instead of block delimiters (braces in the C family 
of languages), ___12___ is used to indicate where blocks begin and end."""
hard_answers  = ["Python", "source", "programming", "Monty", "system", "teach", "scripting", "search", "language", "bytecode", "object", "indentation"]
hard_blanks = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___", "___7___", "___8___", "___9___", "___10___", "___11___", "___12___"]

# Text source: https://en.wikibooks.org/wiki/Python_Programming/Overview

# asks the user to select a level
def select_level():
	"""
	ask the user to select a level, if they mistype prompts again
	"""
	user_level = raw_input("Welcome to my Guess the Missing Word game. You have 5 attempts at each missing word. Please select a level: easy medium or hard (case sensitive): ")
	while user_level not in difficulty:
		user_level = raw_input("Try again. Please select a level: easy medium or hard (case sensitive): ")
	return user_level

# gets the quiz based on the level chosen by the user
def get_quiz(select_level):
	if select_level == "easy":
		return easy_text
	if select_level == "medium":
		return medium_text
	if select_level == "hard":
		return hard_text

# gets the answers to the quiz & the blanks to be replaced in the quiz text, based on the level chosen by the user
def get_answers(select_level):
	if select_level == "easy":
		return easy_answers, easy_blanks
	if select_level == "medium":
		return medium_answers, medium_blanks
	if select_level == "hard":
		return hard_answers, hard_blanks

# counts the number of elements in the answer list for the level chosen by the user
def number_of_answers(select_level):
	if select_level == "easy":
		return len(easy_answers)
	if select_level == "medium":
		return len(medium_answers)
	if select_level == "hard":
		return len(hard_answers)

# runs the quiz of asking for a guess and returning a response if correct or incorrect 
def play_quiz():
	"""
	asks the user to guess the missing word, 
	if correct, returns the updated quiz text,
	if incorrect, deducts one from guesses_left and they can guess again
	"""
	level = select_level()
	solution_text = get_quiz(level)
	print solution_text
	missing_word_count = number_of_answers(level)
	quiz_answers, blank_words = get_answers(level) 
	guesses_left = 5
	index = 0
	while index < missing_word_count:
		user_guess = raw_input("\nWhat is the answer to " + blank_words[index] + "?""\n")   
		if user_guess == quiz_answers[index]:
			solution_text = solution_text.replace(blank_words[index], quiz_answers[index])
			index += 1
			guesses_left = 5
			print "That is the correct answer!"
			print solution_text
		else:
			guesses_left -=1
			if guesses_left == 0:
				print "Game over!"
				return
			else:
				print "Incorrect answer, you have " + str(guesses_left) + " guesses left."
	print "Congratulations, you win!"
	return

# executes the quiz 
play_quiz()


# research note - string and integer concatenation info here http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python
