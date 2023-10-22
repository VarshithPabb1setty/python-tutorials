from Question import Question

question_prompts = [
    "What is Varshith's favorite color?\n (a) Green\n (b) Blue\n (c) Red\n (d) Yellow\n\n",
    "What is Varshith's favorite sport?\n (a) Cricket\n (b) Football\n (c) Hockey\n (d) Tennis\n\n",
    "What is Varshith's favorite food?\n (a) Pizza\n (b) Burger\n (c) Dosa\n (d) Biryani\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " +str(score) + " out of " + str(len(questions)) + " questions correct.")

run_test(questions)