import time
import random
import threading

def countdown():
    global timer 
    global win 
    global wrong
    win = 0
    timer= 30
    wrong = 0
    while timer:  
        mins, secs = divmod(timer, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
       #print(timeformat, end='\r')
        time.sleep(1)
        timer -= 1
    if win == 1:
        print("Congratulations")
    elif wrong >4 :
        print("Game Over Wrong answer")
    else:
        print("Time out!")
    
word = ["Hello","Word","Yes", "No"]
used = []
start = ""


#random picking of array 
rand = random.randint(0,len(word)-1) 
guess = word[rand].lower() #word

#declare stating blanks
for i in range(len(guess)):
    start += "_"

#Start the game 
game = True
count_thread = threading.Thread(target = countdown) 
while game == True:
    play = input("Start? (Y/N) ") 
    if(play.lower() == "y" ):
        count_thread.start()
        game = False

    elif(play.lower()== "n"):
        print("Bye")
        game = False
        exit()
    else:
        print("Press Y to Continue || Press N to Close")



guess_array = [*guess] #[y,e,s]
blank = [*start] #[y,-,-] y__
print(f"{len(guess)} Letter Word")
print(start)
 
while timer > 0 :
    unlockedletter = "".join(blank) # yes || guess = yes

    if(wrong >4):
        timer=1
        count_thread.join()
        break
    
    if(unlockedletter == guess ): 
        timer = 1
        win = 1
        count_thread.join()
        break
    
    
    print(f"Wrong: {wrong}")
    user_answer = input("Your Guess: \n").lower()

    if(user_answer.lower() in used):
      print(f"{user_answer} is already given") 
      continue
     

    if(user_answer in guess_array):
        used.append(user_answer)
        for i in range(len(guess)):
            if guess_array[i].lower() == user_answer:
                 del(blank[i])
               
                 blank.insert(i, guess_array[i])         
        print("".join(blank))

    else:
        wrong+=1

    used.append(user_answer)






       
        




        





