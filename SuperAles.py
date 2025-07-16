#Create a superclass for types of beer called Ale 
class Ale:
    #Initialize the ale with a name and alcohol by volume 
    def __init__(self,name,abv):
        self.name=name
        self.abv=abv #Alcohol by volume
    #Calculate alcohol content by volume in ounces
    def alcohol_content(self,volume_in_oz):
        content=self.abv*volume_in_oz #Find alcohol content by multiplying the specifc alcohol by ounces
        return f"In {volume_in_oz} oz of {self.name}, there is {content} oz of alcohol"
    #Give a description of the alchols name and its alcohol by volume 
    def description(self):
        desc=f"{self.name}:{self.abv*100:.1f}%ABV"
        return desc
    
#Create a subclass for types of beer
#Each subclass provides its specifc name and ABV 
class PaleAle(Ale):
    def __init__(self):
        super().__init__("Pale Ale",0.055)
class IPA(Ale):
    def __init__(self):
        super().__init__("IPA",0.065)
class Stout(Ale):
    def __init__(self):
        super().__init__("Stout",0.07)
class Porter(Ale):
    def __init__(self):
        super().__init__("Porter",0.06)


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
#Test Code
print() #Add extra line for readability

pale=PaleAle()
ipa=IPA()
stout=Stout()
porter=Porter()

print()#extra line for readabiltiy 

print(pale.description())
print(pale.alcohol_content(20))

print() #extra line for readabiltiy 

print(ipa.description())
print(ipa.alcohol_content(8))

print() #extra line for readabiltiy 

print(stout.description())
print(stout.alcohol_content(32))

print() #extra line for readabiltiy 

print(porter.description())
print(porter.alcohol_content(12))

print() #extra line for readiablity 


