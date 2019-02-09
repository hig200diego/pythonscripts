with_vowels = "I´m Diego Freire"

show = ''.join(char for char in with_vowels if char not in "aeiou")
print(show)