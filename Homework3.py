import random
import sys
animals=['kedi','köpek','kaplumbağa','tırtıl','yılan','aslan','kaplan','timsah','kuş','balık','örümcek',
         'maymun','tavşan','fare','zebra','zürafa','geyik','çekirge','ahtapot','yarasa','baykuş','kurbağa']
word=random.choice(animals) #word
print(word)
count=10
word_len=len(word)  # x
temp = list('*'*word_len)
guesses=[]   # guesses

while count > 0:
    letter=input("Enter a letter: ")  # guess
    if len(letter)>1:
        count -=1
        print("Please enter a letter")
        continue
    elif letter not in word:
        count -=1
        if count==0:
            print("Game Over...Good luck next time.")
            sys.exit()
        print(f"Wrong letter. You have {count} tries left.")
    else:
        for i in range(len(word)):
            if letter==word[i]:
                temp[i]=letter
                print(' '.join(temp), end='\n')
            else:
                guesses.append(letter)
            if '*' not in temp:
                print("Congratulations. :)")
                sys.exit()