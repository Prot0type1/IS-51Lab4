"""
this program gives the end user three attempts to answer the question
what is the capital of California will be the question with the answer being Sacramento
set max_tries = 3. a loop iterate three times for each attempt,
we verify if the user input matches the answer. 
If verification is correct, print "correct!" , the loop will along with a break statement 
if the user fails to answer correctly with 3 tries, 
then print "You have used up your maximum allowed attempts.", then print "The correct answer is California"

"""

"""
main 
    question = "What is the capital of California"
    answer = "Sacramento"
    ask(question, answer)
ask 
    tries = 0
    loop three times
        increment tries 
        ask user input()
        verify if user input is equal to answer
            if so, print "Correct" then exit loop
    if not correct 
        print to the user "You have used up your maximum allowed attemptsYou have used up maximum allowed attempts
         "The correct answer is Sacramento"
main 

"""

def main():
    question = "What is the capital of California? "
    answer = "Sacramento"
    ask(question, answer)


def ask(question, answer, max_tries=3):
    tries = 0
    ans = ""
    while tries < max_tries:
        tries += 1
        ans = input(question)
        if ans == answer:
            print("Correct!")
            break
    if ans != answer:
        print("You have used up your maximum allowed attempts.")

main()