import random
import time

quiz_data = {
    "Python": {
        "Easy": [
            {"question": "What is the correct file extension for Python files?", "choices": ["A) .py", "B) pythom", "C) pyt", "D) txt"], "answer": "A"},
            {"question": "Which of the following is a valid variable name in Python?", "choices": ["A) 2nd_value", "B) second-value", "C) second_value", "D) second value"], "answer": "C"},
            {"question": "What keyword is used to define a function in Python?", "choices": ["A) func", "B) define", "C) def", "D) functions"], "answer": "C"},
            {"question": "How do you insert comments in Python?", "choices": ["A) // comment", "B) #commet", "C) /*comment*/", "D) – comment"], "answer": "B"},
            {"question": "Which function is used to read input from the user in Python?", "choices": ["A) input()", "B) scan()", "C) read()", "D) get()"], "answer": "A"},
            {"question": "What is the output of print(type(5))?", "choices": ["A) <class 'int'>", "B) <class 'float'>", "C) <class 'str'>", "D) <class 'bool'>"], "answer": "A"},
            {"question": "Which of the following is a list in Python?", "choices": ["A) (1, 2, 3)", "B) [1, 2, 3]", "C) {1, 2, 3}", "D) <1, 2, 3>"], "answer": "B"},
            {"question": "How do you create a dictionary in Python?", "choices": ["A) dict = [1, 2, 3]", "B) dict = {1, 2, 3}", "C) dict = (1: “one”, 2: “two”)", "D) dict = {1: “one”, 2: “two”}"], "answer": "D"},
            {"question": "What is the output of print(3 + 4 * 2)?", "choices": ["A) 14", "B) 11", "C) 10", "D) 7"], "answer": "B"},
            {"question": "Which operator is used for exponentiation in Python?", "choices": ["A) ^", "B) **", "C) //", "D) %"], "answer": "B"},                                  
            ],
        "Medium": [
            {"question": "What is a function in Python?", "choices": ["A) A block of code that performs a specific task and can be reused", "B)  A variable that holds multiple values in one data type", "C)  A reserved keyword in Python", "D) A built-in tool for debugging"], "answer": "A"},
            {"question": "Which of the following data types is immutable in Python?", "choices": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"], "answer": "C"},
            {"question": "What does the len() function do in Python?", "choices": ["A) Converts a string to lowercase", "B) Returns the number of elements in an object (e.g., a string, list, tuple)", "C) Appends elements to a list", "D) Sorts a list in ascending order"], "answer": "C"},
            {"question": "What is the purpose of comments in Python code?", "choices": ["A) To execute hidden code that is ignored by the interpreter", "B) To make code easier to understand for humans by providing explanations", "C) To change the behavior of Python's built-in functions", "D) To automatically optimize the code's performance"], "answer": "B"},
            {"question": "Which of the following statements about Python dictionaries is true?", "choices": ["A) Keys in a dictionary must be unique", "B) Dictionaries are ordered collections of elements", "C)  A dictionary key can be mutable", "D) Dictionaries cannot store other dictionaries"], "answer": "A"}
            
        ],
        "Hard": [
            {"question": "What happens when a function is called with more positional arguments than it is defined to accept?", "choices": ["A) The extra arguments are automatically discarded without any error", "B) The function raises a SyntaxError", "C) The function raises a TypeError", "D) The extra arguments are converted into keyword arguments"], "answer": "C"},
            {"question": "In Python, what is the main reason for using __slots__ in a class?", "choices": ["A) To provide a way to store data using dictionaries", "B) To enable faster dictionary operations", "C)  To prevent the creation of an instance dictionary, thereby saving memory", "D) To allow classes to define multiple constructors"], "answer": "C"},
            {"question": "How does Python handle variable scope in nested functions when using the global keyword?", "choices": ["A) It creates a local variable in the nested function", "B)  It makes the variable available only within the nested function", "C) It allows modification of variables defined in the global scope from within the nested function", "D) It creates a new variable in the enclosing function's scope"], "answer": "C"},
            {"question": "What is the purpose of the yield keyword in Python?", "choices": ["A) It creates a static variable in a function", "B) It is used to generate values for asynchronous code", "C) It allows a function to return multiple values and pause its state between calls", "D) It transforms a function into a decorator"], "answer": "C"},
            {"question": "Which of the following statements about metaclasses in Python is true?", "choices": ["A) Metaclasses only apply to Python built-in classes", "B) Metaclasses are used to define the behavior and structure of class instances", "C) Metaclasses are classes of classes that control the creation and behavior of classes", "D) Metaclasses cannot be inherited"], "answer": "C"}            
            
        ]
    }
        
}

def main_menu():
    print("Welcome to Quiz Whiz!")
    print("1) Start Quiz")
    print("2) Exit")
    choice = input("Choose only [1, 2]: ")
    return choice


def select_subject():
    print("Select Subject:")
    for i, subject in enumerate(quiz_data.keys(), 1):
        print(f"{i}) {subject}")
    subject_choice = input("Choose Only [1, 2]: ")
    
    subject_list = list(quiz_data.keys())
    if subject_choice.isdigit() and 1 <= int(subject_choice) <= len(subject_list):
        return subject_list[int(subject_choice) - 1]
    else:
        print("Invalid choice.")
        return None

# Function to display the difficulty selection menu
def select_difficulty():
    print("Select Difficulty Level")
    print("Each Difficulty have Points, GOOD LUCK TO YOUR QUIZ!!")
    print("1) Easy (10 Points)")
    print("2) Medium (20 Points)")
    print("3) Hard (30 Points)")
    difficulty = input("Choose only [1, 2, 3]: ")
    return {"1": "Easy", "2": "Medium", "3": "Hard"}.get(difficulty)

# Function to get questions based on subject and difficulty level
def get_questions(subject, difficulty):
    return quiz_data.get(subject, {}).get(difficulty, [])

# Function to administer the quiz
def start_quiz(questions):
    random.shuffle(questions)  # Randomize question order
    score = 0
    time_limit = 120  # 2 minutes time limit

    for question in questions:
        print("\n" + question["question"])
        for choice in question["choices"]:
            print(choice)

        start_time = time.time()
        answer = input("Enter your answer (A, B, C, D): ")
        elapsed_time = time.time() - start_time

        print(f"You took {elapsed_time:.2f} seconds to answer.")
        
        if elapsed_time > time_limit:
            print("Time's up! No points for this question.")
        elif answer.upper() == question["answer"]:
            print("Correct!")
            score += calculate_points(difficulty)
        else:
            print(f"Incorrect. The correct answer was {question['answer']}.")

    return score

# Function to calculate points based on difficulty
def calculate_points(difficulty):
    return {"Easy": 10, "Medium": 20, "Hard": 30}.get(difficulty, 0)

# Main program loop
while True:
    choice = main_menu()

    if choice == "1":
        subject = select_subject()
        if not subject:
            continue  # Retry if subject choice is invalid

        difficulty = select_difficulty()
        if not difficulty:
            print("Invalid difficulty level.")
            continue  # Retry if difficulty choice is invalid

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
