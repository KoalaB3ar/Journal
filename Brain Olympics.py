import time #this is using the time module commands within it
import random #this is using the random module commands within it

#This is the beginning portion of the code
print("Welcome to the Brain Olympics") # this is the first message when the code is being run
time.sleep(1) #setting a timed delay before the next message
print("Are you up for the challenge?")
time.sleep(1)

#This is the second portion of the code
confirmation = "Type Y if you're ready or N if you're not ready"
print("Type Y if you're ready or N if you're not ready")
confirmation = input("Answer: ")
confirmation = str(confirmation)
yes = "Y"
no = "N" 

#This is the third portion of the code
#
#This is the countdown timer when you accept the challenge
def countdown():
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")

if confirmation == yes:
    print("Time to test your math skills")  
    countdown()
else:
    print("No worries, come back when you're ready")
    exit() #this should exit the program if there is an error

#This is the fourth portion of the code (creating math functions)
#
#This is the addition function code, we just need to do addition() to call this function
def addition():
    n1 = random.randrange(1,10)
    n2 = random.randrange(5,15)
    number1 = int(n1)
    number2 = int(n2)
    answer = int(n1 + n2)
    question = "What is {} + {}?"
    time.sleep(1)
    print(question.format(number1, number2))
    user_answer = input("Answer: ")
    user_answer = int(user_answer)
    #once the user types the answer, the program will check to see if it's correct
    if answer == user_answer: #this statement is checking if the computer's answer matches with the user
        print("That is correct!")
    else:
        print("I'm sorry that is incorrect, you have one more try")
        time.sleep(1)
        print("Here's the question again")
        question = "What is {} + {}?" #this is creating a variable "question" to hold "what is _ + _"
        time.sleep(1)
        print(question.format(number1, number2)) #recalling the variable question and using the first randomly generated number, following the second randomly generated number
        user_answer = input("Answer: ") #this is creating a variable "user_answer" to hold "Answer: "
        user_answer = int(user_answer) #this is converting the user_answer from a string to an int by re-assigning the variable
        if answer == user_answer:
            print("That is correct!")
            time.sleep(1)
        else:
            correctanswer = "I'm sorry the correct answer was: {} "
            print(correctanswer.format(answer))
            exit()

#this is the multiplication formula
def multiplication():
    m1 = random.randrange(1,10) #this will randomly pick a number between 1 to 10
    m2 = random.randrange(5,10) #this will randomly pick a number between 5 to 15
#storing the numbers generated
    mnumber1 = int(m1) #this will store the first randomly generated number
    mnumber2 = int(m2) #this will store the second randomly generated number
    manswer = int(m1 * m2) #this will store the answer, will be used to check if the user typed the correct answer
    question = "What is {} * {}?" #this is creating a variable "question" to hold "what is _ + _"
    time.sleep(1)
    print(question.format(mnumber1, mnumber2)) #recalling the variable question and using the first randomly generated number, following the second randomly generated number
    user_manswer = input("Answer: ") #this is creating a variable "user_answer" to hold "Answer: "
    user_manswer = int(user_manswer) #this is converting the user_answer from a string to an int by re-assigning the variable

    if manswer == user_manswer:
        print("That is correct!")
    else:
        print("I'm sorry that is incorrect, you have one more try")
        time.sleep(1)
        print("Here's the question again")
        question = "What is {} * {}?" #this is creating a variable "question" to hold "what is _ + _"
        time.sleep(1)
        print(question.format(mnumber1, mnumber2)) #recalling the variable question and using the first randomly generated number, following the second randomly generated number
        user_manswer = input("Answer: ") #this is creating a variable "user_answer" to hold "Answer: "
        user_manswer = int(user_manswer) #this is converting the user_answer from a string to an int by re-assigning the variable
        if manswer == user_manswer:
            print("That is correct!")
            time.sleep(1)
        else:
            correctmanswer = "I'm sorry the correct answer was: {}"
            print(correctmanswer.format(manswer))
            exit()

#this is the subtraction formula
def subtraction():
    s1 = random.randrange(20,40)
    s2 = random.randrange(1,20)
    snumber1 = int(s1)
    snumber2 = int(s2)
    sanswer = int(s1 - s2)
    question = "What is {} - {}?"
    time.sleep(1)
    print(question.format(snumber1, snumber2))
    user_sanswer = input("Answer: ")
    user_sanswer = int(user_sanswer)
    if sanswer == user_sanswer:
        print("That is correct!")
        time.sleep(1)
    else:
        print("I'm sorry that is incorrect, you have one more try")
        time.sleep(1)
        print("Here's the question again")
        question = "What is {} - {}?"
        time.sleep(1)
        print(question.format(snumber1, snumber2))
        user_sanswer = input("Answer: ")
        user_sanswer = int(user_sanswer)
        if sanswer == user_sanswer:
            print("That is correct!")
            time.sleep(1)
        else:
            correctanswer = "Im sorry the correct answer was: {}"
            print(correctanswer.format(sanswer))
            exit()

def division():
    range = (48, 30, 24, 12, 8)
    range2 = (4,2)
    d = random.choice(range) #testing to see if the random will choose one number from range and range 2
    d2 = random.choice(range2)
    danswer = int(d / d2)
    question = "What is {} / {}?"
    time.sleep(1)
    print(question.format(d, d2))
    user_danswer = input("Answer: ")
    user_danswer = int(user_danswer)
    if danswer == user_danswer:
        print("That is correct!")
        time.sleep(1)
    else:
        print("I'm sorry that is incorrect, you have one more try")
        time.sleep(1)
        print("Here's the question again")
        question = "What is {} / {}?"
        time.sleep(1)
        print(question.format(d, d2))
        user_danswer = input("Answer: ")
        user_danswer = int(user_danswer)
        if danswer == user_danswer:
            print("That is correct!")
            time.sleep(1)
        else:
            correctanswer = "Im sorry the correct answer was: {}"
            print(correctanswer.format(danswer))
            exit()



#separated by subjects for the Brain Olympics
def math():
    addition()
    time.sleep(1)
    print("Can you solve this multiplication question")
    time.sleep(1)
    multiplication()
    time.sleep(1)
    print("Can you solve this subtraction problem")
    time.sleep(1)
    subtraction()
    time.sleep(1)
    print("Can you solve this division problem")
    division()

math()

#these are codes to test to see the type of result to ensure everything is correct
#
#print(type(answer)) #this is a test to ensure the answer is storing as an integer (kept getting errors and wans't sure the solution)
#print(type(user_answer)) #this is a test to ensure the answer is storing as an integer (kept getting errors and wans't sure the solution)


