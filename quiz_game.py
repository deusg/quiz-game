# Quiz Game

questions = ['What is the capital of Peru', 'Which is the longest river', 'Who painted the Mona Lisa?']
answers = ['Lima', 'Nile', 'Leonardo da Vinci']

score = 0
n = len(questions)

for i in range(n):
    user_answer = input(f"{questions[i]}: ")
    if user_answer.lower() == answers[i].lower():
        print("You are correct")
        score += 1
    else:
        print(f"You are incorect. The correct answer is: {answers[i]}")

print(f"Your score is: {score}")

