
# 이재원 - 2023161840
import matplotlib.pyplot as plt

# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  



# Create an object RedCircle

RedCircle = Circle(0, 'red')
RedCircle.radius
RedCircle.add_radius(2)
RedCircle.radius
RedCircle.add_radius(2)
RedCircle.radius
RedCircle.add_radius(2)
# Answer = 6

RedCircle = Circle(1, 'red')
RedCircle.radius
# Answer = 1


RedCircle.radius
# Answer = 1
RedCircle.color
# Answer = 'red'


RedCircle.radius = 12
RedCircle.radius

# Call the method drawCircle
RedCircle.radius = 20
RedCircle.drawCircle()


# We can increase the radius of the circle by applying the method add_radius(). 
# Let increases the radius by 2 and then by 5: 
print('Radius of object:',RedCircle.radius)

RedCircle.add_radius(2)
RedCircle.drawCircle()
RedCircle.radius
# Answer = 22

BlueCircle = Circle(radius=100)
BlueCircle.radius
# Answer = 100
BlueCircle.color
# Answer = 'blue'

BlueCircle.drawCircle()



# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width = 2, height = 3, color ='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()



SkinnyBlueRectangle = Rectangle(2, 10, 'blue')

SkinnyBlueRectangle.height
# Answer = 10
SkinnyBlueRectangle.width
# Answer = 2
SkinnyBlueRectangle.color
# Answer = 'blue'
SkinnyBlueRectangle.drawRectangle()

# Create a new object rectangle
FatYellowRectangle = Rectangle(20, 5, 'yellow')

FatYellowRectangle.height
# Answer = 5
FatYellowRectangle.width
# Answer = 20
FatYellowRectangle.color
# Answer = 'yellow'

FatYellowRectangle.drawRectangle()
