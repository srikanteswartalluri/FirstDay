class Emp:
   def __init__(self, name, occupation, salary, department, experience, performance):
       self.name = name
       self.occupation = occupation
       self.salary = salary
       self.department = department
       self.experience = experience
       self.performance = performance


   def Canpromote(self):
       if self.experience > 3:
           print("Promote")
           return "Promote"
       else:
           print("Not yet")
           return "Not yet"


   def CP(self):
       if self.experience > 3:
           return True
       else:
           return False


   def Calculatbonus(self):
       if self.experience > 2 and self.performance > 3:  # how to perform operations?
           print("Bonus")
       else:
           print("Not yet")