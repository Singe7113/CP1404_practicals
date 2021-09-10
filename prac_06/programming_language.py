class ProgrammingLanguage():
    def __init__(self,name, typing = "" ,relfection = "" ,year = ""):
        
        self.name = name
        self.typing = typing
        self.relfection = relfection
        self.year = year
   
    def __str__(self):
        return '{}, {} Typing, Reflection = {}, First appeared in {}'.format(self.name,self.typing,self.relfection,self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"