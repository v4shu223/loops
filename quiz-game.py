print("welcome to the quiz game")
score = 0
print("lets begin the quiz")


question = input("what is the sum of 77 and 13?")

if question == "110":
    print("correct answer")
    score += 1
else:
        print("incorrect answer")
print(f"your final score is: {score}")
