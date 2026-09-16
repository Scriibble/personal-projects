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
    "What is a function?":
        "a relation where each input has exactly one output.",

    "What is the domain of a function?":
        "the set of possible input values.",

    "What is the range of a function?":
        "the set of possible output values.",

    "What is the slope formula?":
        "m = (y2 - y1) / (x2 - x1)",

    "What is the y-intercept?":
        "the point where a graph crosses the y-axis.",

    "What is the slope-intercept form of a line?":
        "y = mx + b",

    "What does m represent in y = mx + b?":
        "the slope.",

    "What does b represent in y = mx + b?":
        "the y-intercept.",

    "What is the solution to 2x + 5 = 13?":
        "x = 4",

    "What is the solution to 3x - 7 = 11?":
        "x = 6",

    "What is the distributive property?":
        "multiplying a number by every term inside parentheses.",

    "What is the zero exponent rule?":
        "any nonzero number raised to the zero power equals 1.",

    "What is a negative exponent?":
        "an exponent that represents a reciprocal.",

    "What is the product of powers rule?":
        "when multiplying the same base, add the exponents.",

    "What is the quotient of powers rule?":
        "when dividing the same base, subtract the exponents.",

    "What is a quadratic equation?":
        "an equation with a highest exponent of 2.",

    "What is the standard form of a quadratic equation?":
        "ax^2 + bx + c = 0",

    "What is the quadratic formula?":
        "x = (-b ± sqrt(b^2 - 4ac)) / 2a",

    "What is the discriminant?":
        "b^2 - 4ac",

    "What does a positive discriminant mean?":
        "the equation has two real solutions.",

    "What does a zero discriminant mean?":
        "the equation has one real solution.",

    "What does a negative discriminant mean?":
        "the equation has no real solutions.",

    "What is the solution to x^2 - 9 = 0?":
        "x = 3 or x = -3",

    "How does x^2 + 5x + 6 factor?":
        "(x + 2)(x + 3)",

    "How does x^2 - 16 factor?":
        "(x - 4)(x + 4)",

    "What is the axis of symmetry of a parabola?":
        "the vertical line that divides the parabola into two equal parts.",

    "What is the formula for the axis of symmetry?":
        "x = -b / 2a",

    "What is the vertex of y = (x - 2)^2 + 3?":
        "(2, 3)",

    "When does a parabola open upward?":
        "when the leading coefficient is positive.",

    "When does a parabola open downward?":
        "when the leading coefficient is negative.",

    "What are the zeros of a function?":
        "the x-values where the function equals zero.",

    "What is the degree of a polynomial?":
        "the highest exponent in the polynomial.",

    "What is a system of equations?":
        "two or more equations solved at the same time.",

    "What is the solution to x + y = 7 and x - y = 1?":
        "(4, 3)",

    "What is substitution?":
        "replacing one variable with an equivalent expression.",

    "What is elimination?":
        "combining equations to remove one variable.",

    "What is the square root of 49?":
        "7",

    "What is the square root of 72 in simplified form?":
        "6sqrt(2)",

    "What does x^(1/2) represent?":
        "the square root of x.",

    "What is i in complex numbers?":
        "the square root of -1.",

    "What is i^2?":
        "-1",

    "What is the square root of -25?":
        "5i",

    "What is an exponential function?":
        "a function where the variable appears in the exponent.",

    "What is the general form of an exponential function?":
        "f(x) = ab^x",

    "When does exponential growth occur?":
        "when the growth factor is greater than 1.",

    "When does exponential decay occur?":
        "when the growth factor is between 0 and 1.",

    "What is log base 10 of 100?":
        "2",

    "What is the exponential form of log base 2 of 8 = 3?":
        "2^3 = 8",

    "What is the solution to 2^x = 16?":
        "x = 4",

    "What is an arithmetic sequence?":
        "a sequence with a common difference.",

    "What is a geometric sequence?":
        "a sequence with a common ratio.",

    "What is the next number in 3, 7, 11, 15?":
        "19",

    "What is the next number in 2, 6, 18, 54?":
        "162",

    "What is the common difference in 5, 9, 13, 17?":
        "4",

    "What is the common ratio in 3, 6, 12, 24?":
        "2",

    "What is the distance formula?":
        "d = sqrt((x2 - x1)^2 + (y2 - y1)^2)",

    "What is the midpoint formula?":
        "((x1 + x2) / 2, (y1 + y2) / 2)"
}

def calculus_trivia():
    question_list = list(questions.keys())
    total_questions = 10
    score = 0

    selected_questions = random.sample(question_list, total_questions)

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