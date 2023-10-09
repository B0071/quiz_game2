print("welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay. Let's go. Your current score is 0.00")
score = 0

answer = input("What is pc? ")
if answer.lower() == "pc":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is gps? ")
if answer.lower() == "gps":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is life? ")
if answer.lower() == "life":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You have answer all questions correctly! Your current score is " + str(score))






