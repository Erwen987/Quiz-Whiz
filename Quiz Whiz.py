import random
import time

quiz_data = {
    "Python": {
        "Easy": [
            {"question": "What is the correct file extension for Python files?", "choices": ["A) .py", "B) pythom", "C) pyt", "D) txt"], "answer": "A"},
            {"question": "Which of the following is a valid variable name in Python?", "choices": ["A) 2nd_value", "B) second-value", "C) second_value", "D) second value"], "answer": "C"},
            {"question": "What keyword is used to define a function in Python?", "choices": ["A) func", "B) define", "C) def", "D) functions"], "answer": "C"}
        ],
        "Medium": [
            {"question": "What is the largest planet in our solar system?", "choices": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"], "answer": "C"},
            {"question": "What element does 'O' represent on the periodic table?", "choices": ["A) Oxygen", "B) Gold", "C) Iron", "D) Silver"], "answer": "A"},
        ],
        "Hard": [
            {"question": "Who wrote 'Pride and Prejudice'?", "choices": ["A) Charles Dickens", "B) Jane Austen", "C) Mark Twain", "D) Leo Tolstoy"], "answer": "B"},
            {"question": "In which year did the Titanic sink?", "choices": ["A) 1905", "B) 1912", "C) 1918", "D) 1923"], "answer": "B"},
        ]
    },
}

def main_menu():
    print("Welcome to Quiz Whiz!")
    print("1) Start Quiz")
    print("2) Exit")
    choice = input("Choose only [1, 2]: ")
    return choice

def select_subject():
    print("Select Subject:")
    for r, subject in enumerate(quiz_data.keys(), 1):
        print(f"{r}) {subject}")
    subject_choice = input("Choose Only [1, 2]: ")
    
    subject_list = list(quiz_data.keys())
    if subject_choice.isdigit() and 1 <= int(subject_choice) <= len(subject_list):
        return subject_list[int(subject_choice) - 1]
    else:
        print("Invalid choice.")
        return None

def select_difficulty():
    print("Select Difficulty Level:")
    print("1) Easy")
    print("2) Medium")
    print("3) Hard")
    difficulty = input("Choose only [1, 2, 3]: ")
    return {"1": "Easy", "2": "Medium", "3": "Hard"}.get(difficulty)

def get_questions(subject, difficulty):
    return quiz_data.get(subject, {}).get(difficulty, [])

def start_quiz(questions):
    random.shuffle(questions)
    score = 0
    time_limit = 120

    for question in questions:
        print("\n" + question["question"])
        for choice in question["choices"]:
            print(choice)

        start_time = time.time()
        print("You have 2 minutes to answer!")
        answer = input("Enter your answer (A, B, C, D) Only: ")
        elapsed_time = time.time() - start_time

        print(f"You took {elapsed_time:.2f} seconds to answer.")
        
        if elapsed_time > time_limit:
            print("Time’s up! No points for this question.")
        elif answer.upper() == question["answer"]:
            print("Correct!")
            score += calculate_points(difficulty)
        else:
            print(f"Incorrect. The correct answer was {question['answer']}.")

    return score

def calculate_points(difficulty):
    return {"Easy": 10, "Medium": 20, "Hard": 30}.get(difficulty, 0)

while True:
    choice = main_menu()

    if choice == "1":
        subject = select_subject()
        if not subject:
            continue 
             
        difficulty = select_difficulty()
        if not difficulty:
            print("Invalid difficulty level.")
            continue  
            
        questions = get_questions(subject, difficulty)

        if not questions:
            print("No questions available for this selection.")
        else:
            score = start_quiz(questions)
            print(f"\nYour final score is: {score}")

            replay = input("Do you want to play again? (yes/no): ").lower()
            if replay != "yes":
                print("Thanks for playing Quiz Whiz!")          
                break
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
