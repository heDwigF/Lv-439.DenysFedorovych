class Figure:
    def __init__(self,color,no_of_sides):
        self.color = 'white'
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def get_side_and_color(self):
        self.color = input('Enter a color of figure ')
        self.sides = [float(input("Enter side ")) for i in range(self.n)]


    def info(self):
        return self.color,self.sides
class Rectangle(Figure):
    def __init__(self):
        Figure.__init__(self,'white',2)   

  