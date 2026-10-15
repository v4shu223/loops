print("welcome to the quiz game")
score = 0
print("lets begin the quiz")


question = input("what is the sum of 77 and 13?")

if question == "90":
    print("correct answer")
    score += 1
else:
        print("incorrect answer")
        score += 0

question = input("what is the name of the first layer of atmosphere?")

if question.lower() == "troposphere":
        print("correct answer")
        score += 1
else:
    print("incorrect answer")
    score += 0

question = input("what is the name of the second layer of atmosphere?")

if question.lower() == "stratosphere":
        print("correct answer")
        score += 1
else:
    print("incorrect answer")
    score += 0

question = input("what is the name of the third layer of atmosphere?")

if question.lower() == "mesosphere":
        print("correct answer")
        score += 1
else:
     print("incorrect answer")
     score += 0

question = input("what is the name of the fourth layer of atmosphere?")

if question.lower() == "thermosphere":
        print("correct answer")
        score += 1
else:
     print("incorrect answer")
     score += 0

question = input("what is the name of the fifth layer of atmosphere?")

if question.lower() == "exosphere":
        print("correct answer")
        score += 1
else:
     print("incorrect answer")
     score += 0


print(f"your final score is: {score}/6")

print("thank you for playing the quiz game!")

print("finnalyyyy i have completed my first quiz game in python")

