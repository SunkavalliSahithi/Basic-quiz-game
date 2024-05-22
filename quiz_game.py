# quiz_game.py

# Quiz data: list of dictionaries
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. J.K. Rowling", "C. Mark Twain", "D. Ernest Hemingway"],
        "answer": "A"
    }
]

def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Your answer (A, B, C, or D): ").upper()
    while user_answer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please choose A, B, C, or D.")
        user_answer = input("Your answer (A, B, C, or D): ").upper()
    return user_answer
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer was {correct_answer}.")
        return False
def quiz():
    score = 0
    for question in quiz_questions:
        user_answer = ask_question(question)
        if check_answer(user_answer, question["answer"]):
            score += 1
        print()  # Blank line for spacing
    print(f"Your final score is: {score}/{len(quiz_questions)}")

# Run the quiz
if __name__ == "__main__":
    quiz()
