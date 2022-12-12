# Practical lesson No. 2, task No. 3.
# This program counts the number of vowels,
# consonants and other characters in user-entered English text.

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

vowels_count = 0
consonants_count = 0
other_count = 0

for l in list(input('Enter the entire text: ')):
    if l in VOWELS:
        vowels_count += 1
    elif l in CONSONANTS:
        consonants_count += 1
    else:
        other_count += 1

print(f'{consonants_count} consonants, {vowels_count} vowels, {other_count} other characters were detected in the text you entered.')

