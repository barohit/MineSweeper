from co.barohit.Square import Square
import random
from pip._vendor.progress import counter
minefield = []
counterX = 0
counterY = 0
difficultyLevelX = 0
difficultyLevelY= 0
numMines = 0
lossCondition = False
winCondition = False


answer = input("Good evening, what difficulty level would you like to play at? You can enter beginner, intermediate, or expert: ")
if (answer == "beginner"): 
    difficultyLevelX = 8
    difficultyLevelY = 8
else:
    if (answer == "intermediate"):
        difficultyLevelX = 16
        difficultyLevelY = 16
    else: 
        if (answer == "expert"): 
            difficultyLevelX = 16
            difficultyLevelY = 30
    
while (counterX < difficultyLevelX ):
    minefield.append([])
    while (counterY < difficultyLevelY): 
        minefield[counterX].append(Square(counterX, counterY))
        counterY = counterY + 1
    counterX = counterX + 1
    counterY = 0

def containerGenerator(diffLevel):
    global numMines
    if (diffLevel == "beginner"):
        while(numMines < 10): 
            xCoord = random.randint(0, difficultyLevelX - 1) #remember, range is inclusive
            yCoord = random.randint(0, difficultyLevelY - 1)
            if (minefield[xCoord][yCoord].item != "mine"):
                minefield[xCoord][yCoord].addItem("mine")
                numMines = numMines + 1
    if (diffLevel == "intermediate"):
        while(numMines < 40): 
            xCoord = random.randint(0, difficultyLevelX - 1)
            yCoord = random.randint(0, difficultyLevelY - 1)
            if (minefield[xCoord][yCoord].item != "mine"):
                minefield[xCoord][yCoord].addItem("mine")
                numMines = numMines + 1
    if (diffLevel == "expert"):
        while(numMines < 99): 
            xCoord = random.randint(0, difficultyLevelX - 1)
            yCoord = random.randint(0, difficultyLevelY - 1)
            if (minefield[xCoord][yCoord].item != "mine"):
                minefield[xCoord][yCoord].addItem("mine")
                numMines = numMines + 1
    
    
def printBoard(field):
    for e in field:
        for element in e: 
            if (element.flagStatus == "flagged"):
                print(element.flagStatus.ljust(9), end=" ")
            else:
                if (element.clickedStatus == "unclicked"):
                    print(element.clickedStatus, end=" ")
                else: 
                    if (element.item == "mine"): 
                        print(element.item.ljust(9), end=" ")
                    else:
                        if (element.item == "empty" and element.surroundingMines == 0):
                            print(element.item.ljust(9), end=" ")
                        else:
                            print("{0:9d}".format(element.surroundingMines), end=" ")
        print("")   

def play():
    xInput = int(input("Enter x-coordinate starting at 1: "))
    yInput = int(input("Enter y-coordinate starting at 1: "))
    flag = input("Would you like to click this square, flag it or unflag it? (Enter 'click', 'flag' or 'unflag')")
    try:
        if (flag == "flag"):
            if ((minefield[8 - yInput])[xInput - 1].clickedStatus == "unclicked"): #you can  only flag an unclicked square
                (minefield[8 - yInput])[xInput - 1].flagStatus = "flagged"
            else:
                print("Sorry, you cannot flag a square that has already been clicked :/")
        else:
            if (flag == "unflag"):
                (minefield[8 - yInput])[xInput - 1].flagStatus = "" #resets regardless of whether or not the square is already flagged
            else:
                if ((minefield[8 - yInput])[xInput - 1].item == "mine"):
                    global lossCondition
                    lossCondition = True
                (minefield[8 - yInput])[xInput - 1].clickedStatus = "clicked"
                (minefield[8 - yInput])[xInput - 1].flagStatus = ""
        printBoard(minefield)
        if (lossCondition == True):
            print("Sorry, you have lost :(")  
        global winCondition
        winCondition = True
        for e in minefield:
            for element in e: 
                if (element.item == "mine" and element.flagStatus == ""):
                    winCondition = False
        if (winCondition == True):
            print("Congratulations, you win! :)")
                
    except IndexError:
        print("Sorry, invalid input")
        
def initializeSurroundingMines(field):
    for e in field:
        for element in e:
            try:
                counter = 0
                if (field[element.x_coordinate + 1][element.y_coordinate].item == "mine"):
                    counter = counter + 1
                if (field[element.x_coordinate - 1][element.y_coordinate].item == "mine"):
                    counter = counter + 1
                if (field[element.x_coordinate][element.y_coordinate + 1].item == "mine"):
                    counter = counter + 1
                if (field[element.x_coordinate][element.y_coordinate - 1].item == "mine"):
                    counter = counter + 1  
                if (field[element.x_coordinate + 1][element.y_coordinate + 1].item == "mine"):
                    counter = counter + 1
                if (field[element.x_coordinate + 1][element.y_coordinate - 1].item == "mine"):
                    counter = counter + 1
                if (field[element.x_coordinate - 1][element.y_coordinate + 1].item == "mine"):
                    counter = counter + 1
                if (field[element.x_coordinate - 1][element.y_coordinate - 1].item == "mine"):
                    counter = counter + 1
                element.surroundingMines = counter
            except IndexError: #makes sure the above method code can work with border squares without having an error
                counter = counter + 0
                
                    
         
containerGenerator(answer) #creates the board
initializeSurroundingMines(minefield) #fills each square with the number of surrounding minds
printBoard(minefield) 
while (lossCondition == False and winCondition == False): 
    play()


    

    



    





