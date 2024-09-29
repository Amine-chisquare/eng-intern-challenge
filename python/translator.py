# For simplicity, we will consider each braille character to be a 6-dimensional row vector
# We start by building an English - Braille lookup table.

# We note that the letter A to J form the "base set"
table = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
}

# In the range of letters ["k", ..., "t"], the ith letter can be related to the ith letter in the range ["a", ..., "j"]:
rangeTenTwenty = [chr(i) for i in range(ord('k'), ord('t') + 1)] # the ten next letters after j (after the base set)
for letter in rangeTenTwenty:
    base_braille = list(table[chr(ord(letter) - 10)]) # get the braille rep of the corresponding letter in the base set
    base_braille[4] = 'O' # the rule relating the letters in the base set to those in rangeTenTwenty is that the '.' at index 4 is replaced by a 'O'
    table[letter] = "".join(base_braille)

# Same concept for the letters ["u", ..., "v"] 
rangeTwentyTwentyTwo = [chr(i) for i in range(ord('u'), ord('z') + 1)] # the two next letters after t 
offset = 10

for letter in rangeTwentyTwentyTwo:
    index = chr(ord(letter) - 10) 

    if chr(ord(letter) - 10) == 'w':
        table['w'] = ".OOO.O" # w is an exception to the rule we came up with
        offset = 11 # the bases of the letters after w are then offset by 1 more 
        continue

    base_braille = list(table[chr(ord(letter) - offset)]) # get the braille rep of the corresponding letter in the base set
    base_braille[5] = 'O' # '.' at index 5 is replaced by a 'O'
    table[letter] = "".join(base_braille)



# and finally ["x", "y", "z"] follow the same rule

print(table)