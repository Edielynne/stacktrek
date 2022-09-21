quiz = ["Where do you live?","What is my name?","Kanino ka lang?"]
answer = ["Subic","Edielynne","Oliver"]
points = 0
for i in range(len(quiz)):
    print(f"{i+1}. {quiz[i]}")
    user= input()
    if(user in answer[i]):
        points +=1
        print('correct')
    else:
        print("Wrong")

print(f"your points: {points}")
