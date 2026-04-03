import random 
import hangman
word_list=['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
chosen_word=random.choice(word_list)
lives=6
display=[]
#find the length of the word and then print 
for i in range(len(chosen_word)):
    display.append('_')
print(display)
game_over=False
while not game_over:
    guessed_letter=input("guess a letter :").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1 
        if lives==0:
            game_over=True
            print("you lose")
    if '_' not in display:
        game_over=True
        print("you win")
    print(hangman.stages[6 - lives])
