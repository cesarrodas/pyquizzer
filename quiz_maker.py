import os

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

quiz = input("Are we creating a new quiz? (yes/no) ")

if(quiz == "yes" or quiz == "y"):
  print("Great!")
  name = input("What is your quiz's name? ")
  folder = os.path.isdir('./quizzes')
  if(folder == False):
    os.mkdir('./quizzes')
  cls()
  print("question one")

if(quiz == "no" or quiz == "n"):
  print("goodbye.")
  exit()