import time
class guitar():
    def __init__(self,name, year = "", cost = ""):
        self.name = name
        self.year = year
        self.cost = cost
   
    def __str__(self):
        return '{}, ({}) : ${} added.'.format(self.name,self.year,self.cost)
    
    def __repr__(self):
        return str(self)

    def get_age(self):
        return (2020 - self.year)


