


question = ["Who is the father of modern computer?", "Who created linux operating system?", "What is the most common programming language?", "What kind of control structure will you use to determine/validate a specific answer?", ]
answer = ["b", "a", "c", "a"]
choices = ["A. Mark zuckerberg, B. Charles babbage, C. Will smith", "A. Linus torvalds, B. Gabe newell, C. Steve jobs", "A. html/css, B. python, C. javascript", "A. if else, B. try/catch, C. while loop"]
score = 0



for i in range (len(question)):
    print(f"Question {i+1} : {question[i]}")
    print("-----------")
    print(f"Choices:" )


    c = choices[i].split(", ")
    for y in range(len(c)):
        print(c[y]+"\n")

    ans = True
    while ans == True:
        user_answer= input("Your answer: ")
        if user_answer.lower() == "a" or user_answer.lower() =="b" or user_answer.lower() =="c":
            ans = False
        else:
            print(f"{user_answer} is not in the choices")
            continue
    

    if answer [i].lower() == user_answer.lower():
        print ("Correct!")
        score += 1

    else:
        print("Wrong!")

print(f"Your score is: {score}")