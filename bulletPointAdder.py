#! python3
# bulletPointAdder.py - Addes Wikipedia points to the star
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.

lines = text.split('\n')

for i in range(len(lines)):		# Loop through all index in the "lines" lists
	lines[i] = '*' + lines[i] 	# add star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)