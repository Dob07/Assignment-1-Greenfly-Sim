import time
import math
import os
import numpy
from sympy import fu 

firstJuv = 0
firstAdults = 0
firstSen = 0
survivalJuv = 0
survivalAdults = 0
survivalSen = 0
birthRate = 0 
noOfGens = 0
newJuv = 0 
newAdults = 0
newSen = 0
juvenile = 0
adult = 0
senile = 0
total = 0

genArray = []
juvArray = []
adArray = []
senArray = []
totalArray = []

genJuv = "       "
juvAd = ""
adSen = ""
senTot = ""

fullArray = []

def firstGenVals():
    global firstJuv          # All of these globals are allowing the variables
    global firstAdults       # in the subprogram to change the same variables 
    global firstSen          # on the outside 
    global survivalJuv       
    global survivalAdults     
    global survivalSen       
    global birthRate         
    global noOfGens  
    global juvenile 
    global adult
    global senile        

    print("ALL THE VALUES ARE IN THOUSANDS")

    firstJuv = float(input("Starting number of juveniles?\n")) # This is setting the starting number of juveniles
    juvenile = firstJuv
    survivalJuv = float(input("Juvenile survival rate? (Between 0 and 1)\n")) # This is setting the survival rate for juveniles
    while survivalJuv < 0 or survivalJuv > 1: # This loop is making sure that the survival rate is between 0 and 1 
        print("Invalid survival rate")
        survivalJuv = float(input("Juvenile survival rate? (Between 0 and 1)\n"))

    firstAdults = float(input("Starting number of adults?\n")) # This is setting the starting number of adults
    adult = firstAdults
    survivalAdults = float(input("Adults survival rate? (Between 0 and 1)\n")) # This is setting the survival rate for adults
    while survivalAdults < 0 or survivalAdults > 1:
        print("Invalid survival rate")
        survivalAdults = float(input("Adults survival rate? (Between 0 and 1)\n"))

    firstSen = float(input("Starting number of Seniles?\n")) # This is setting the starting number of seniles
    senile = firstSen
    survivalSen = float(input("Seniles survival rate? (Between 0 and 1)\n")) # This is setting the survival rate for adults
    while survivalSen < 0 or survivalSen > 1:
        print("Invalid survival rate")
        survivalSen = float(input("Senile survival rate? (Between 0 and 1)\n"))

    birthRate = float(input("What is the birthRate?\n")) # Setting the birth rate

    noOfGens = int(input("How many generations?\n")) # Setting how many generations the simulation will run for
    while noOfGens < 5 or noOfGens > 25: # This loop is making sure the number of generations is between 5 and 25
        print("Invalid generation range")
        noOfGens = int(input("How many generations?\n"))

    menu() # return to menu

def firstGenValShow(): # This subprogram is printing all the values that were put in
    print("There are", firstJuv, "juveniles" )
    print("The juvenile Survival rate is", survivalJuv)
    print("There are", firstAdults, "adults")
    print("The adults Survival rate is", survivalAdults)
    print("There are", firstSen, "seniles")
    print("The senile Survival rate is", survivalSen)
    print("The birthRate is", birthRate)
    print("The number of generations is", noOfGens)
    time.sleep(2)
    menu()

def runSim(): # This runs the simulation 
    global firstJuv          # Declare variables
    global survivalJuv       
    global survivalAdults     
    global survivalSen       
    global birthRate         
    global noOfGens
    global newJuv
    global newAdults
    global newSen
    global juvenile 
    global adult
    global senile
    global total
    global genArray
    global juvArray 
    global adArray 
    global senArray 
    global totalArray 
    global genJuv 
    global juvAd 
    global adSen 
    global senTot
    global fullArray

    noOfGens = noOfGens + 1
    gencheck = 0
    total = juvenile + adult + senile

    for i in range(noOfGens): # This will run for the amount of generations that there are
        genArray.append(gencheck) # These append the values from 
        juvArray.append(juvenile) # each generation into its own
        adArray.append(adult)     # array depending on its type
        senArray.append(senile)
        totalArray.append(total)
        tArr = [gencheck, juvenile, adult, senile, total] # This is an array for the file save
        fullArray.append(tArr) # This sends the tArr to the main array for the file save

        newJuv = adult * birthRate # This works out the new juveniles
        newJuv = round(newJuv, 2) # This rounds it to 2 dp.

        newAdults = juvenile * survivalJuv # This works out the new adults
        newAdults = round(newAdults, 2) 

        newSen = (senile * survivalSen) + (adult * survivalAdults) # This works out the new seniles
        newSen = round(newSen, 2)

        total = newJuv + newAdults + newSen # This works out the total
        total = round(total, 2)

        juvenile = newJuv # These set the new values as the old value and allow it to repeat
        adult = newAdults
        senile = newSen
        
        gencheck = gencheck + 1

    print("GENERATION   JUVENILES   ADULTS   SENILES   TOTAL") # This is the top of the table
    for i in range(noOfGens):
        genJuv = "        "
        juvAd = ""
        adSen = ""
        senTot = ""
        gStr = str(genArray[i])
        jStr = str(juvArray[i])
        aStr = str(adArray[i])
        sStr = str(senArray[i])
        if len(gStr) > 1:        #This is making sure the generation is in line with the top
            genJuv = "       "    

        a = len(jStr)            #This is making sure the juveniles is in line with the top
        while a != 10:
            juvAd = juvAd + " "
            a = a + 1

        a = len(aStr)            #This is making sure the adults is in line with the top
        while a != 7:
            adSen = adSen + " "
            a = a + 1

        a = len(sStr)            #This is making sure the senile is in line with the top
        while a != 8:
            senTot = senTot + " " 
            a = a + 1

        print("  ", genArray[i], genJuv, juvArray[i], juvAd, adArray[i], adSen, senArray[i], senTot, totalArray[i]) # This repeatedly prints to give the look of a table
        
    print(" ") 
    menu() # Takes back to menu


def export(): # The export to file function
    global fullArray
    global noOfGens
    ord = fullArray 

    exportedFile = input("What is the name of the file? ") # Asks for the name of the file
    if os.path.exists(exportedFile): # If the files name already exists then
        print("This file already exists")
        overrideQ = input("Do you want to override it? ") # Asks if they want to override the pre-existing file
        while overrideQ.lower() == "no" or overrideQ.lower() == "n": # If they dont
            exportedFile = input("What is the name of the new file? ") # Name the new file
            f = open(exportedFile, "w")
            f.write("GENERATION   JUVENILES   ADULTS   SENILES   TOTAL")
            f.write("\n")
            for i in range(noOfGens): # Goes down the array 1 by 1 and makes it look like a table
                f.write(str(ord[i]))
                f.write("\n") 
            f.close()
            break
        if overrideQ.lower() == "yes" or overrideQ.lower() == "y": # If they want to override the pre-existing file then the exact same happens except naming the new file
            f=open(exportedFile,"w")               
            f.write("GENERATION   JUVENILES   ADULTS   SENILES   TOTAL")
            f.write("\n")
            for i in range(noOfGens):
                f.write(str(ord[i]))
                f.write("\n")
            f.close()
    else: # If the file is a new name then run as normal
        f=open(exportedFile,"w")               
        f.write("GENERATION   JUVENILES   ADULTS   SENILES   TOTAL")
        f.write("\n")
        for i in range(noOfGens):
            f.write(str(ord[i]))
            f.write("\n")
        f.close()
    menu()
            


    
def menu(): # This subprogram is the menu where the program starts and returns to after a subprogram is done
    print("Greenfly Population\n")                          # These prints are showing the options that can be done
    print("1: Set the values for the first generation")
    print("2: Show the values for the first generation")
    print("3: Run the simulation")
    print("4: Save results")
    print("5: Quit")
    choiceSelect = int(input("\nPlease select the option 1, 2, 3, 4 or 5: ")) # Asking the user to input an option

    if choiceSelect != 1:                   # All of these if statements are checking that
        if choiceSelect != 2:               # they have picked a value that is valid
                if choiceSelect != 3:
                    if choiceSelect != 4:
                        if choiceSelect != 5:
                            choiceSelect = int(input("\nPlease select the option 1, 2, 3, 4 or 5: ")) # If it isnt valid it asks the user again

    if choiceSelect == 1:
        firstGenVals() # This accesses the subprogram to change the values that will be used in the simuulation
    elif choiceSelect == 2:
        firstGenValShow() # this will print a table with the values for gen 0
    elif choiceSelect == 3:
        runSim() # this will run the simulation
    elif choiceSelect == 4:
        export() # this will save the results of the simulation into a txt file
    elif choiceSelect == 5:
        exit() # this quits the program

menu()
