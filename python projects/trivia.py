## pesudo code
## 
## list of questions
## store answers (dictionary?)
## 
## randomly pick question to ask user
##
## user answers
##
## check answer
## award points
##
## display score

import random

questions = {
    "What is the instantaneous rate of change of a function called?": "derivative",
    "What value does a function approach as its input nears a point?": "limit",
    "What line touches a curve at one point and has the same slope there?": "tangent",
    "What quantity describes the steepness of a graph?": "slope",
    "What line intersects a curve at two points?": "secant",
    "What type of quotient approximates a derivative using two function values?": "difference",
    "Which rule differentiates a power of x by multiplying by its exponent?": "power",
    "Which rule is used to differentiate two functions multiplied together?": "product",
    "Which rule is used to differentiate one function divided by another?": "quotient",
    "Which rule is used to differentiate a composite function?": "chain",
    "What type of function has the same value for every input?": "constant",
    "What is the derivative of a constant function?": "zero",
    "What adjective describes a number where a derivative is zero or undefined?": "critical",
    "What is the greatest value of a function on a specified interval called?": "maximum",
    "What is the least value of a function on a specified interval called?": "minimum",
    "What is the derivative of position with respect to time called?": "velocity",
    "What is the derivative of velocity with respect to time called?": "acceleration",
    "What property describes whether a graph bends upward or downward?": "concavity",
    "What kind of point occurs where a graph changes concavity?": "inflection",
    "What type of differentiation is used when a variable is not isolated?": "implicit"
}

def calculus_trivia():
    question_list = list(questions.keys())
    total_questions = 10
    score = 0

    selected_questions = random.sample(question_list, total_questions)

    print(F"\nAll answers should be entered in lowercase\n")

    for idx, question in enumerate(selected_questions):
        print(F"{idx +1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question].strip()

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score +=1
        else:
            print(F"Wrong, The correct answer is: {correct_answer}.\n")

    print(F"Game Over! Your final score is: {score}/{total_questions}")



calculus_trivia(

)