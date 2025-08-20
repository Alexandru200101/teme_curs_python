class Circle:
    def __init__(self,radius):
        self.radius=radius
    def arie(self):
        return 3.14*self.radius**2
    def circumferinta(self):
        return 2*3.14*self.radius

if __name__=="__main__":
    circle1=Circle(3)
    print(circle1.arie())
    print(circle1.circumferinta())
        
