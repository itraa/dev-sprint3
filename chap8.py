# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Aarthi Narayan


def rotate_word(word,n):
    i = 0
    new_word = ""
    if len(word) > 0:
        while i < len(word):
            word_num=ord(word[i]) - ord('a')
            word_num = (word_num + n)  % 26 + ord('a')
#            if word_num > ord('z'):            
#                word_num = ord('a') + n                
            new_word=new_word + chr(word_num) 
            i = i + 1
        return new_word

print rotate_word('cheer',7)
print rotate_word('melon', -10)
