import requests
import random
import html


def fetch_question():
    url = "https://opentdb.com/api.php?amount=1&type=multiple"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    if data["response_code"] != 0 or not data["results"]:
        raise ValueError("Failed to fetch trivia question from API.")

    question_data = data["results"][0]

    question = html.unescape(question_data["question"])
    correct_answer = html.unescape(question_data["correct_answer"])
    incorrect_answers = [
        html.unescape(answer) for answer in question_data["incorrect_answers"]
    ]

    options = incorrect_answers + [correct_answer]
    random.shuffle(options)

    return question, correct_answer, options


def play_game():
    print("🎮 Trivia Quiz Game")
    print("-" * 30)

    try:
        question, correct_answer, options = fetch_question()
    except Exception as e:
        print(f"Could not load trivia question: {e}")
        return

    print(f"\nQuestion:\n{question}\n")

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_input = input("\nEnter your answer (1-4): ").strip()

    if user_input not in {"1", "2", "3", "4"}:
        print("Invalid input. Please run the game again and enter a number from 1 to 4.")
        return

    selected_option = options[int(user_input) - 1]

    print("\n--- Result ---")
    if selected_option == correct_answer:
        print("✅ Correct! You win!")
    else:
        print("❌ Wrong answer!")
        print(f"Correct answer: {correct_answer}")


if __name__ == "__main__":
    play_game()