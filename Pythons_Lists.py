# String Exercises 1
"""
string = "I don't know"

print(string.upper())
"""

# String Exercise 2
"""
string = "sTeVe"

print(string.capitalize())
"""

# String Exercise 3
"""
string = "dave"

print(string[::-1])
"""

# String Exercise 4

user_input = input("Please type a word or phrase to be translated into Leet Speak: ")

string_2 = user_input.replace("a","4")
string_3 = string_2.replace("e", "3")
string_4 = string_3.replace("g","6")
string_5 = string_4.replace("i","1")
string_6 = string_5.replace("o","0")
string_7 = string_6.replace("s","5")
string = string_7.replace("t","7")

print(string.upper())


# Assignment 5 - Long-long vowels
#Incomplete
"""
string = "Food"
index = 0

while index <= len(string):
    if string[index] == string[index+1]:
"""

#Assignment 6 - Caesar Cipher
"""
order = "we attack at dawn destroy this message as soon as you read it"
alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher = 5
index = 0
coded_message = ""

while index < len(order):
    let = order[index]
    index = index + 1
    if let in alphabet:
        index_alphabet = alphabet.index(let)
        cipher_index = index_alphabet + cipher
        if cipher_index > len(alphabet):
            cipher_index = cipher_index - len(alphabet)
        coded_message = coded_message + alphabet[cipher_index]
    else:
        coded_message = coded_message + " "    

print(coded_message)        
"""