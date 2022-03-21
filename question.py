class Question:
  ''' A question class'''
  def __init__(self, question):
    self.question = question
    self.answer = ""
    self.choice1 = ""
    self.choice2 = ""
    self.choice3 = ""
    
  def addAnswer(self, answer):
    self.answer += answer
  
  def addChoice(self, choice):
    if (self.choice1 == ""):
      self.choice1 = choice
    elif (self.choice2 == ""):
      self.choice2 = choice
    else:
      self.choice3 = choice
    
