# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Aarthi Narayan
# Exercise 9.1

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print word


# Exercise 9.2

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

count = 0
n = 0
fin = open('words.txt')
for line in fin:
    word = line.strip()
    n = n + 1
    if has_no_e(word) is True:
        print word
        count = count + 1
print "Percentage is: " + str(100 * (float(count)/float(n)))    

# Exercise 9.3

n= 0
fin = open('words.txt')
string = raw_input('Enter the string: ')

def avoids(word,string):
    for letter in word:
        if letter in string:
            return False  
    return True

for line in fin:
    word = line.strip()
    if avoids(word,string) is True:
        n = n + 1
print "Number of words without string: " + str(n)


# Exercise 9.4

def uses_only(word,string):
    for letter in word:
        if letter not in string:
            return False
    return True
