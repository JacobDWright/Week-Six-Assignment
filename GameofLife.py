#Jacob Wright
#Intro to Computer Science
#Week 6 assignment
#Collaborated with Daniel McMurry, Marissa Gross, Evan Sauers

#Populate defines what is in the world
def populate(world,h,w):
  dummy = 0

#Display shows the population in the world
def display(world,h,w):
  dummy2 = 2

#Generation updates the population and returns the next generation.
def generation(world,h,w):
  dummy3 = 3

#Main puts all of the functions together
def main():
  import random
  height = 22
  width = 80
  world = []
  x = input("Enter q to quit")
  while x != "q":
  
  
    populate(world,height,width)
  
    display(world,height,width)
  
    generation(world,height,width)
  
  
main()  