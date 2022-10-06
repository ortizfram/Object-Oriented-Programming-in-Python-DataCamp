"""
Inheritance and polymorphism are the core concepts of OOP that enable efficient and consistent
code reuse. Learn how to inherit from a class, customize and redefine methods, and review the 
differences between class-level data and instance-level data.

  - Inheritance: extending functionality of existing code
  - Polymorphism : creating unified interface 
  - Encapsulation:  bundiling of data and methods
  
Why use class attributes? (global constants related to class ->)
  - min / max values for attributes
  - conmmonly used values / constants : e.g. pi for a circle class 
Class methods ?
  - already shared. Same code for every instance
  - can't use instance-level data
************************************************************************************"""
# Create a Player class
class Player: 
    
    # Class Attributes 
    MAX_POSITION = 10 
    
    # constructor
    def __init__(self):
        self.position = 0
""""""
# Print Player.MAX_POSITION       
print(Player.MAX_POSITION)

# Create a player p and print its MAX_POSITITON
p = Player()
print(p.MAX_POSITION)
#------------------------------------------------------------------------#
class Player:
  # class attribute
    MAX_POSITION = 10
    
    #constructor
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move(self, steps):
        
        if(self.position + steps < Player.MAX_POSITION):
            self.position += steps
        else: 
            self.position = Player.MAX_POSITION
    

       
    # This method provides a rudimentary visualization in the console    
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()
"""
<script.py> output:
    |----------
    ----|------
    ---------|-
    ----------|
 """
#------------------------------------------------------------------------#
# Create Players p1 and p2
p1 = Player()
p2 = Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# Assign 7 to p1.MAX_SPEED
p1.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)
#------------------------------------------------------------------------#
# Create Players p1 and p2
#change class attribute Player.MAX_SPEED
p1, p2 = Player(), Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# ---MODIFY THIS LINE--- 
Player.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)
#------------------------------------------------------------------------#
class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
      # Recall that Python allows multiple variable assignments in one line
      self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return BetterDate(year, month, day)
        
bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)
