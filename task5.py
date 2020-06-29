import random
print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
ans = random.choice(words)
n = 8
word = '-' * len(ans)
flag = False
while n != 0:  
    print(f"\n\n{word}")
    letter = input('Input a letter: > ')
    if len(letter) != 1:
        print("You should input a single letter")
        continue
    if letter.islower() == False:
        print('It is not an ASCII lowercase letter')
        continue
    

    if letter in ans and letter not in word:
        temp = ''
        for i in range(len(ans)):
            if ans[i] != letter:
                temp = temp + word[i]
            else:
                temp = temp + letter
        word = temp
    elif letter in word:
        print("You already typed this letter")
       
    else:
        print("No such letter in the word")
        n = n - 1
    
    if word == ans:
        flag = True
        break


if flag == True:
    print(f"You guessed the word {ans}!\nYou survived!")
else:
    print("You are hanged!")




