class Question:
  ''' A question class'''
  def __init__(self, question):
    self.question = question
    self.choices = []
    self.answer = ""
    
  def addAnswer(self, answer):
    self.answer += answer
  
  def addChoice(self, choice):
    self.choices.append(choice)
    
