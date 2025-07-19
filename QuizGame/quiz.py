import json

with open("questions.json","r")as file:
    questions = json.load(file)

score =0

for i, q in enumerate(questions):
    print(f"\nQuestion {i+1}:{q['question']}")
    for option in q["options"]:
        print(option)

    answer =input("Your ans (A/B/C/D):").strip().upper()

    if answer==q["answer"]:
        print("Correct")
        score +=1
    else:
        print(f"Wrong ans! The correct ans is {q['answer']}")
print (f"\n Quiz Completed! Your score{score} out of{len(questions)}.")
          