import os

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

def edit_quiz(file):
  done = False
  while (done == False):
    q = input("Enter a question. ")
    file.write("Q " + q)
    a = input("Enter the correct answer. ")
    file.write("A " + a)
    choice1 = input("Enter an incorrect choice. ")
    file.write("C1 " + choice1)
    choice2 = input("Enter another incorrect choice. ")
    file.write("C2 " + choice2)
    choice3 = input("Enter a third incorrect choice. ")
    file.write("C3 " + choice3)
    dun = input("Are you done? ")
    if(dun == "yes" or dun == "y"):
      print("Done!")
      print("goodbye.")
      done = True
    else:
      cls()

quiz = input("Are we creating a new quiz? (yes/no) ")

if(quiz == "yes" or quiz == "y"):
  print("Great!")
  name = input("What is your quiz's name? ")
  folder = os.path.isdir('./quizzes')
  if(folder == False):
    os.mkdir('./quizzes')
  file = os.path.exists('./quizzes/' + name + ".txt")
  if(file == True):
    print("This quiz already exists. ")
    print("goodbye.")
  else:
    print("Creating your quiz... ")
    f = open("./quizzes/" + name + ".txt", "a")
    edit_quiz(f)
    f.close()
  #cls()
  #print("question one")

if(quiz == "no" or quiz == "n"):
  add_question = input("Are we adding a question to this quiz? ")
  if(add_question == "yes" or add_question == "y"):
    quiz_name = input("What is the quizz's name? ")
    if(quiz_name[-4] != "txt"):
      quiz_name = quiz_name + ".txt"
    file = os.path.exists('./quizzes/' + quiz_name)
    if(file == True):
      f = open('./quizzes/' + quiz_name, "a")
      edit_quiz(f)
      f.close()

  if(add_question == "no" or add_question == "n"):
    print("goodbye.")
    exit()