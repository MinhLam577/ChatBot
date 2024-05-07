import json
from difflib import get_close_matches
import random
import os

json_data_path = "data/json/question_data.json"
def load_json_file(file: str) -> dict:
    with open(file, 'r', encoding="utf-8") as f:
        return json.load(f)
    
def save_json_file(file: str, data: dict) -> None:
    with open(file, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
def convert_json_string_to_python_string(json_string: str) -> str:
    return json_string.replace('"""', '') if json_string.startswith('"""') else json_string

def find_best_match(user_question: str, question: list[str]) -> str | None:
    #Convert all strings to lower case
    user_question = user_question.lower()
    question = [q.lower() for q in question]
    matches = get_close_matches(user_question, question, n=1, cutoff=0.7)
    return matches[0] if matches else None

def get_answer_for_question(user_question: str, questions: dict) -> str | None:
    user_question = user_question.lower()
    for q in questions["questions"]:
        q["question"] = q["question"].lower()
        if q["question"] == user_question:
            # Check if the answer is a list
            if isinstance(q["answer"], list):
                # If it is, find the best match within the list
                return convert_json_string_to_python_string(random.choice(q["answer"]))
            else:
                # If it's not a list, return the answer as is
                return convert_json_string_to_python_string(q["answer"])

def chatbot(file: str) -> None:
    questions_data = load_json_file(file)
    while True:
        user_question = input('You: ')
        if user_question == 'exit':
            break
        best_match: str | None = find_best_match(user_question, [question['question'] for question in questions_data['questions']])
        if best_match:
            answer: str = get_answer_for_question(best_match, questions_data)
            print(f'Chatbot: {answer}')
        else:
            print(f"Bot: I don't have the answer. Please teach me.")
            new_answer = input('Type new answer or skip to skip the question or exit to stop: ')
            if new_answer.lower().strip() == "skip":
                continue
            if new_answer.lower().strip() == "exit":
                break
            save_character = input(f"Bạn có muốn lưu câu trả lời là {new_answer} cho câu hỏi {user_question} không (y/n): ")
            if save_character.lower() == "y":
                questions_data["questions"].append({"question": user_question, "answer": new_answer})
                save_json_file(file, questions_data)
        c = input("Do you want to clear the terminal (y/n): ")
        if c.lower() == "y":
            os.system('cls' if os.name == 'nt' else 'clear')
chatbot(json_data_path)