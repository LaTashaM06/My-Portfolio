#LaTasha McCoy, Nov 3, 2024
#The purpose of this code is to map out a blueprint defining the class of an object and naming it's attributes and methods.

class Flower: #Flower is identified as the class.
    def __init__(self, name): #Constructor method used
        self.name = name #this is a name variable

    def grow(self): #this code is defining the method "grow" of the flower 
        print("The " +self.name + " is growing.")#telling the program to print the name of the flower and it's attribute

    def bloom(self):#this code is defining the 2nd method of the flower "bloom"
        print("The " + self.name + " is blooming.")#this is telling the program to print the name of the flower and it's 2nd attribute

def main():
    flower1 = Flower("Rose") #Rose, an attribute, has been defined in the flower class
    flower1.grow() #first method for flower 1
    flower1.bloom() #second method for flower 2
    flower2 = Flower("Daisy") #Daisy, has been defined as the 2nd attribute of the flower class
    flower2.grow() #first method for flower 2
    flower2.bloom() #second method for flower 2
    flower3 = Flower("Marigold") #Marigold is defined as 3rd attribute in flower class
    flower3.grow() #first method for flower 3
    flower3.bloom() #second method for flower 3
    

if __name__ == "__main__": #allows code to execute when file is run as script
  main()