#Joseph Lee
#MCS 275 Programming Tools and File Management
#Professor Danko Adrovic
#Teaching Assistant Lakshmi Sridevi
import random
import matplotlib.pyplot as plt
class Dice(object):
        
    def getDiceNumber(self): #rolls a dice from values 1 through 6
        d = random.randint(1,6)
        return d
     

class Sierpinski(Dice):
 X =[]
 Y =[]
    
 def __init__(self, Point, rn, x, y): #Initializes the x and y coordinates of the triangle, the number of dice rolls, and the starting x, y points

        self.P1x = Point[0][0]
        self.P1y = Point[0][1]
        self.P2x = Point[1][0]
        self.P2y = Point[1][1]
        self.P3x=  Point[2][0]
        self.P3y = Point[2][1]
        self.rn = rn
        self.initial_pos_x = x
        self.initial_pos_y = y
        Dice.__init__(self)
        

 def generate_data(self): 
   
         x1 = self.initial_pos_x 
         y1 = self.initial_pos_y #Declaring the starting points to be [1,1]. This is the current position for now. 
              
         for d in range(self.rn): #rolls the dice value and the dice value will plot the point. The dice will roll 1000 times 
             d = self.getDiceNumber() 
                 
             if d == 1 or d == 2: #Selects point [0,0]. Finds the midpoint and makes it the new current position.  
               x1 = (self.P1x+x1)/2
               y1 = (self.P1y+y1)/2
               self.X.append(x1)
               self.Y.append(y1)
               self.initial_pos_x = x1
               self.initial_pos_y = y1

             elif d == 3 or d == 4: #Selects point [20,20]. Finds the midpoint and makes it the new current position
               x1 = (self.P2x+x1)/2
               y1 = (self.P2y+y1)/2
               self.X.append(x1)
               self.Y.append(y1)
               self.initial_pos_x = x1
               self.initial_pos_y = y1

             elif d == 5 or d == 6: #Selects point [40,0]. Finds the midpoint and makes it the new current position
               x1 = (self.P3x+x1)/2
               y1 = (self.P3y+y1)/2
               self.X.append(x1)
               self.Y.append(y1)
               self.initial_pos_x = x1
               self.initial_pos_y = y1
        

               
         return self.X, self.Y      
      
 def plot_data(self): #Graphs and plots the points of the Sierpinski Triangle
              
        plt.plot(self.X, self.Y,'r.')
        plt.legend(['Sierpinski Triangle'])
        plt.xlabel('X-Coordinate')
        plt.ylabel('Y-Coordinate')
        plt.grid()
        plt.show()
        

def main():
    
    # S = Sierpinski([[P1x, P1y], [P2x, P2y], [P3x, P3y]], number_of_iterations, current_pos_x, current_pos_y)
    S = Sierpinski([[0,0],[20,20],[40,0]], 1000, 1, 1)
    S.generate_data()
    S.plot_data()

main()
    






