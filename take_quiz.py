import os 
from question import Question

questions = []

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

def read_quiz(file):
  question = False
  for line in file:
    if line.startswith("Q"):
      question = Question(line[2:])
    elif line.startswith("A"):
      question.addAnswer(line[2:])
    elif line.startswith("C1") or line.startswith("C2"):
      question.addChoice(line[3:])
    elif line.startswith("C3"):
      question.addChoice(line[3:])
      question.randomize()
      questions.append(question)


name = input("What quiz are you taking? ")
file = os.path.exists('./quizzes/' + name + ".txt")
f = open('./quizzes/' + name + '.txt', 'r')
read_quiz(f)
f.close()
cls()
right = 0
total = len(questions)
for quest in questions:
  print(quest.question)
  letters = ("A. ", "B. ", "C. ", "D. ")
  choice = { "a": quest.order[0], "b": quest.order[1], "c": quest.order[2], "d": quest.order[3]}
  pick = {0: quest.answer, 1: quest.choice1, 2: quest.choice2, 3: quest.choice3 }
  for index, item in enumerate(quest.order):
    if(item == 0):
      print(letters[index] + quest.answer)
    else:
      choo = "choice" + str(item)
      print(letters[index] + getattr(quest, choo))
  answer = input("Enter the correct letter. ")
  chosen = pick[choice[answer.strip().lower()]]
  print(chosen)
  if(quest.answer == chosen):
    right += 1
  input("next")
  cls()
print("You got " + str(right) + " questions right out of " + str(total)) 
print("Your score is " + str(right/total * 100))
      

if(file == False):
  print("This quiz does not exist.")
  print("goodbye.. ")