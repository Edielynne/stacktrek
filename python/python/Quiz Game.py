question = [ ]
answer = [""]
score = 0

for i in range (len(question)):
    print(f"Question {i+1} : {question[i]}")
    user_answer = input("Your answer: ")

    if answer [i] == user_answer:
        print ("Correct!")
        score += 1

    else:
        print("Wrong!")

print(f"Your score is: {score}")