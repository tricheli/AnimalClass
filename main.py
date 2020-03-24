#Tenisce Richelieu 

#Your algorithm should go here OR you should use comments throughout

#In this class, you will create all the methods and attributes necessary to store and get
#the name, animal type, age, sound and color of the animals.

class Zoo:
    #__init___ method initializes the attributes of the instance variables
    def __init__(self):
        self.name = ''
        self.animalType = ''
        self.age = 0
        self.sound = ''
        self.color = ''
        
    def storeName(self, inName):
        self.name = inName

    def storeAnimalType(self, inAnimalType):
        self.animalType = inAnimalType

    def storeAge(self, inAge):
        self.age = inAge

    def storeSound(self, inSound):
        self.sound = inSound

    def storeColor(self, inColor):
        self.color = inColor

    def printName(self):
        print('My name is', self.name)

    def printAnimalType(self):
        print('I am a', self.animalType)
        
    def printAge(self):
        print('My age is', self.age)

    def printSound(self):
        print('My sound is', self.sound)

    def printColor(self):
        print('I am', self.color)

    
def main():
    #Create an instance of the Zoo class
    zoo_animal = Zoo()
    
    name = input('What is the name of the animal?: ')
    zoo_animal.storeName(name)
    animalType = input('What type of animal is it?: ')
    zoo_animal.storeAnimalType(animalType)
    age = int(input('How old is the animal?: '))
    zoo_animal.storeAge(age)
    sound = input('What sound does this animal make?: ')
    zoo_animal.storeSound(sound)
    color = input('What color(s) is this animal?: ')
    zoo_animal.storeColor(color)
    '''
    storeName(self, inName)
    storeAnimalType(self, inAnimalType)
    storeAge(self, inAge)
    storeSound(self, inSound)
    storeColor(self, inColor)
    '''
    zoo_animal.printName()
    zoo_animal.printAnimalType()
    zoo_animal.printAge()
    zoo_animal.printSound()
    zoo_animal.printColor()
    

