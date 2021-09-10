class guitar():
    def __init__(self,name, year = "", cost = ""):
        
        self.name = name
        self.year = year
        self.cost = cost
   
    def __str__(self):
        return '{}, ({}) : %{} added'.format(self.name, self.year,self.cost)

    def get_age(self, age):
        
