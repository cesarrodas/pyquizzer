import os 
from question import Question

questions = []

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
      questions.append(question)


name = input("What quiz are you taking? ")
file = os.path.exists('./quizzes/' + name + ".txt")
f = open('./quizzes/' + name + '.txt', 'r')
read_quiz(f)
f.close()
print(questions)
for x in questions:
  print(x.question)

if(file == False):
  print("This quiz does not exist.")
  print("goodbye.. ")