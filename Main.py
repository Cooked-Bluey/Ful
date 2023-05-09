import random
import ArtAndAssest as a
import os
import msvcrt
import time
import sys

#Player Class


class Player:
    def __init__(self, PlayerHP, PlayerAP, PlayerDmg):
        self.PlayerHP = PlayerHP
        self.PlayerAP = PlayerAP
        self.PlayerDmg = PlayerDmg
        
        playerLimbs = AllLimbs["Player"].copy()
        self.EquippedLeftArm = playerLimbs[0]
        self.EquippedRightArm = playerLimbs[1]
        self.EquippedTorso = playerLimbs[2]
        self.EquippedLeftLeg = playerLimbs[3]
        self.EquippedRightLeg = playerLimbs[4]
        
        self.Inventory = []
    #Player Stats Page
    def PlayerStats(self):
        os.system('cls')
        print(a.Menu)
        print(self.EquippedLeftArm)
        StatInput = msvcrt.getch()
        StatInput = chr(ord(StatInput))
        if StatInput == 'i':
            ItemInventory()
        
    #Limb Swapping Function
    def SwapLimbs(self):
        for i in range(len(self.Inventory)):
            print(str(i+1) + ": " + self.Inventory[i].Name)
        
        LimbNumber = int(input("Swap Item Number: ")) - 1
        
        NewLimb = self.Inventory[LimbNumber]
        Limb = NewLimb.BodyPart
        if Limb == "LeftArm":
            self.Inventory.append(self.EquippedLeftArm)
            self.EquippedLeftArm = NewLimb
            self.Inventory.remove(self.EquippedLeftArm)
        elif Limb == "RightArm":
            self.Inventory.append(self.EquippedRightArm)
            self.EquippedRightArm = NewLimb
            self.Inventory.remove(self.EquippedRightArm)
        elif Limb == "Torso":
            self.Inventory.append(self.EquippedTorso)
            self.EquippedTorso = NewLimb
            self.Inventory.remove(self.EquippedTorso)
        elif Limb == "LeftLeg":
            self.Inventory.append(self.EquippedLeftLeg)
            self.EquippedLeftLeg = NewLimb
            self.Inventory.remove(self.EquippedLeftLeg)
        elif Limb == "RightLeg":
            self.Inventory.append(self.EquippedRightLeg)
            self.EquippedRightLeg = NewLimb
            self.Inventory.remove(self.EquippedRightLeg)

#Broader Enemy Class
class Enemy():
    def __init__(self, Name, HP, AP, DMG, SpawnCount, Level = 1):
        self.Name = Name
        self.HP = HP
        self.AP = AP
        self.DMG = DMG
        self.SpawnCount = SpawnCount
        self.Level = Level
    
    def OnDeath(self):
        DroppedLimb = AllLimbs[self.Name].copy()[random.randint(0,4)]
        DroppedLimb.EnemyChange(self.Level)
        return DroppedLimb
    
    def Debug(self):
        print("HP: " + str(self.HP) + " AP: " + str(self.AP) + " DMG: " + str(self.DMG) + " Level: " + str(self.Level))
        lmb = self.OnDeath()        
        print("Limb- HP: " + str(lmb.HPBoost) + " DMG: " + str(lmb.DMGBoost) + " AP: " + str(lmb.APBoost) + " Name: " + lmb.Name + "\n")

#Enemy Type
class Imp(Enemy):
    def __init__(self, Level):
        DMGBoost = Level * 2 #Tweak
        RandomHPChange = random.randint(-3, 3) #Tweak
        super(Imp, self).__init__("Imp", 15 + RandomHPChange, 1, 3 + DMGBoost, 1, Level)

class Strong(Enemy):
    def __init__(self, Level):
        DMGBoost = Level * 2 #Tweak
        RandomHPChange = random.randint(-3, 3) #Tweak
        super(Strong, self).__init__("Strong", 75 + RandomHPChange, 1, DMGBoost + 10, 5, Level)

class Stealth(Enemy):
    def __init__(self, Level):
        super(Stealth, self).__init__("Stealth", 35, 3, 5, 4, Level)

class Fast(Enemy):
    def __init__(self, Level):
        super(Fast, self).__init__("Fast", 25, 5, 4, 3, Level)

#Limb class
class Limb():
    def __init__(self, Set, BodyPart, HPBoost, APBoost, DMGBoost):
        self.BodyPart = BodyPart
        self.SetID = Set
        self.BodyPart = BodyPart
        self.Name = BodyPart + Set
        self.DMGBoost = DMGBoost
        self.HPBoost = HPBoost
        self.APBoost = APBoost
        
    def EnemyChange(self, Level): #Tweak
        self.DMGBoost += Level-1
        self.DMGBoost += random.randint(0, 1)
        
        self.HPBoost += Level-1
        self.HPBoost += random.randint(-1, 3)

        self.APBoost += random.randint(0, 1)

#Level Counter
MainGameLevel = 1

#The Possible interactions
Interactables = ["Imp", "Fast", "Strong", "Stealth", "Chest", "Lore"]


#Scrolling text function
def scrollTxt(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

#Creates the Limb sets for fully equip sets
def GenerateSet(SetName, limbHP, limbAP, limbDMG):
    UpperLimbTypes = ["LeftArm", "RightArm", "Torso"]
    LowerLimbTypes = ["LeftLeg", "RightLeg"]
    
    UpperLimbHP = limbHP*MainGameLevel
    UpperLimbDMG = limbDMG*MainGameLevel
    
    SetLimbs = []
    #TWEAK
    for limb in UpperLimbTypes:
        SetLimbs.append(Limb(SetName, limb, UpperLimbHP, limbAP, UpperLimbDMG))
        
    for limb in LowerLimbTypes:
        SetLimbs.append(Limb(SetName, limb, limbHP, limbAP, limbDMG))
    
    return SetLimbs
AllLimbs = {
    "Imp":GenerateSet("Imp", 3, 1, 2),
    "Strong":GenerateSet("Strong", 18, 1, 4),
    "Stealth":GenerateSet("Stealth", 10, 2, 3),
    "Fast":GenerateSet("Fast", 7, 3, 2),
    "Player":GenerateSet("Player", 1, 1, 1)
}

#Players Item Inventories
HPItemsList = []
APItemList = []

player = Player(100, 50, 10)

#Time.sleep Constant
timer = 2


def CheckAround(Map):
    # initialize list 
    ZeroIndexes = []
    
    # iterate over each element in the Map
    for i in range(len(Map)):
        for j in range(len(Map[0])):
            if Map[i][j] == 0:
                # check if every direction has a 1
                HasOneAbove = i > 0 and Map[i-1][j] == 1
                HasOneBelow = i < len(Map)-1 and Map[i+1][j] == 1
                HasOneLeft = j > 0 and Map[i][j-1] == 1
                HasOneRight = j < len(Map[0])-1 and Map[i][j+1] == 1
                
                if HasOneAbove and HasOneBelow and HasOneLeft and HasOneRight:
                    # append the index of the zero to the list
                    ZeroIndexes.append((i,j))
    
    return ZeroIndexes

def GenerateMaze(Size = 15, EntranceCol = random.randrange(1, 15 - 1)):
    # Initialize the Maze with walls
    Size = Size - 2

    Maze = [[1] * Size for _ in range(Size)]

    # Set the entrance and exit
    #EntranceCol = random.randrange(1, Size - 1)
    Maze[0][EntranceCol] = 0
    ExitCol = random.randrange(1, Size - 1)
    while ExitCol == EntranceCol:
        ExitCol = random.randrange(1, Size - 1)
    Maze[Size - 1][ExitCol] = 0

    '''# Ensure that first and last elements of each Row are 1s
    for Row in Maze:
        Row[0] = 1
        Row[-1] = 1
    
    # Ensure only one 0 in the first and last Rows
    Maze[0][ExitCol] = 1
    Maze[Size - 1][EntranceCol] = 1'''
    
    # Recursive Backtrack algorithm
    PastCoordinates = [(random.randrange(1, Size - 1), random.randrange(1, Size - 1))]
    while PastCoordinates:
        Row, Col = PastCoordinates[-1]
        Maze[Row][Col] = 0
        Neighbours = []
        if Row > 1 and Maze[Row - 2][Col] == 1:
            Neighbours.append((Row - 2, Col))
        if Col > 1 and Maze[Row][Col - 2] == 1:
            Neighbours.append((Row, Col - 2))
        if Row < Size - 2 and Maze[Row + 2][Col] == 1:
            Neighbours.append((Row + 2, Col))
        if Col < Size - 2 and Maze[Row][Col + 2] == 1:
            Neighbours.append((Row, Col + 2))
        if Neighbours:
            chosen = random.choice(Neighbours)
            chosen_Row, chosen_Col = chosen
            WallRow, WallCol = (Row + chosen_Row) // 2, (Col + chosen_Col) // 2
            Maze[WallRow][WallCol] = 0
            PastCoordinates.append(chosen)
        else:
            PastCoordinates.pop()

    for Row in Maze:
        Row.insert(0, 1)
        Row.append(1)

    TopRowZeroes = []
    BottomRowZeroes = []

    for i in range(Size+2):
        if Maze[0][i] == 0:
            TopRowZeroes.append(i)

        if Maze[Size-1][i] == 0:
            BottomRowZeroes.append(i)


    TopRow = []
    for i in range(Size+2): 
        TopRow.append(1)
    TopRowStartingPosition = TopRowZeroes[random.randint(0, len(TopRowZeroes)-1)]
    TopRow[TopRowStartingPosition] = 2
    Maze[1][TopRowStartingPosition] = 0


    BottomRow = []
    for i in range(Size+2): 
        BottomRow.append(1)
    BottomRowStartingPosition = BottomRowZeroes[random.randint(0, len(BottomRowZeroes)-1)]
    BottomRow[BottomRowStartingPosition] = 9
    Maze[Size-2][BottomRowStartingPosition] = 0

    Maze.append(BottomRow)
    Maze.insert(0, TopRow)

    for coords in CheckAround(Maze):
        Maze[coords[0]][coords[1]] = 1

    return Maze

#Converting Int to Char/Sym
def PrintMaze(Maze):
    os.system('cls')
    for Row in range(len(Maze)):
        RowString = ""
        for Column in range (len(Maze)):
            if Maze[Row][Column] == 1:
                RowString += "# "
            elif Maze[Row][Column] == 2:
                RowString += "P " 
            elif Maze[Row][Column] == 0:
                RowString += "  "
            else: 
                RowString += str(Maze[Row][Column]) + " "
        print(RowString)
        
    print(a.Menu)

#Check if the player has reached the end of the maze
def CheckPlayerFinish(Maze):
    FinalRow = Maze[-1]
    if 2 in FinalRow:
        MainGameLevel += 1
        return True
    else:
        return False

#Player Movement and other interaction commands
def ChangePlayerPosition(Maze):
    Direction = msvcrt.getch()
    if Direction == b'\x03':
        quit()
    else:
        Direction = chr(ord(Direction))

    for Row in range(len(Maze)):
        for Column in range (len(Maze)):
            if Maze[Row][Column] == 2:
                PlayerIndex = (Row, Column)
                        
    #player movement
    if Direction == "w":
        if PlayerIndex[0] - 1 >= 0:
            if Maze[PlayerIndex[0] - 1][PlayerIndex[1]] != 1:
                NextTile = Maze[PlayerIndex[0] - 1][PlayerIndex[1]]
                Maze[PlayerIndex[0] - 1][PlayerIndex[1]] = 2 
                Maze[PlayerIndex[0]][PlayerIndex[1]] = 0
                return NextTile
    elif Direction == "s":
        if PlayerIndex[0] + 1 <= len(Maze)-1:
            if Maze[PlayerIndex[0] + 1][PlayerIndex[1]] != 1:
                NextTile = Maze[PlayerIndex[0] + 1][PlayerIndex[1]]
                Maze[PlayerIndex[0] + 1][PlayerIndex[1]] = 2 
                Maze[PlayerIndex[0]][PlayerIndex[1]] = 0
                return NextTile
    elif Direction == "a":
        if PlayerIndex[1] - 1 >= 0:
            if Maze[PlayerIndex[0]][PlayerIndex[1] - 1] != 1:
                NextTile = Maze[PlayerIndex[0]][PlayerIndex[1] - 1]
                Maze[PlayerIndex[0]][PlayerIndex[1] - 1] = 2 
                Maze[PlayerIndex[0]][PlayerIndex[1]] = 0
                return NextTile
    elif Direction == "d":
        if PlayerIndex[1] + 1 <= len(Maze)-1:
            if Maze[PlayerIndex[0]][PlayerIndex[1] + 1] != 1:
                NextTile = Maze[PlayerIndex[0]][PlayerIndex[1]+1]
                Maze[PlayerIndex[0]][PlayerIndex[1]+1] = 2
                Maze[PlayerIndex[0]][PlayerIndex[1]] = 0
                return NextTile
    elif Direction == "i":
        ItemInventory()
    
    elif Direction == "e":
        player.PlayerStats()

    elif Direction == "h":
        print("Working on it")

#Total Number of 0's in the array
def GetFreeSpace(Maze):
    FreeSpaces = 0
    for Row in range(len(Maze)):
        for Column in range (len(Maze)):
            if Maze[Row][Column] == 0:
                FreeSpaces += 1
    return FreeSpaces

#Enemy Spawns Based on the conditions of the maze
def SpawnEnemies(Maze, EnemyDict):
    Chest = True
    Lore = True
    FreeSpaces = GetFreeSpace(Maze)
    while FreeSpaces > 0:
        for Row in range(len(Maze)-2):
            CurrentRow = Row + 1
            for Column in range (len(Maze)):
                if Maze[CurrentRow][Column] == 0 and random.randint(0, 3) == 0:
                    if Lore == True and Chest == True:
                        Index = random.randint(0, len(Interactables)-1)
                    elif Lore == False and Chest == False:
                        Index = random.randint(0, len(Interactables)-3)
                    elif Lore == False:
                        Index = random.randint(0, len(Interactables)-2)
                    elif Chest == False:
                        Index = random.randint(0, len(Interactables)-1)
                        while Index == len(Interactables)-3:
                            Index = random.randint(0, len(Interactables)-1)
                    Interactable = Interactables[Index]
                    Maze[CurrentRow][Column] = Index + 3
                    if Index == len(Interactables)-1:
                        FreeSpaces -= 1
                        Lore = False
                    elif Index == len(Interactables)-2:
                        FreeSpaces -= 1
                        Chest = False
                    else:
                        FreeSpaces -= EnemyDict[Interactable].SpawnCount

#The interactions based on the number interacted with on the screen
def Interaction(NextTile):
    #Enemy instigators 
    if NextTile == 3:
        os.system('cls')
        print("""
    Imp
                """)
        print(a.ImpFullyBody)
        
        time.sleep(timer)
    elif NextTile == 4:
        os.system('cls')
        print("""
Fast
            """)
        print(a.FastFullBody)
        time.sleep(timer)
    elif NextTile == 5:
        os.system('cls')
        print("""
Strong
            """)
        print(a.StrongFullBody)
        time.sleep(timer)
    elif NextTile == 6:
        os.system('cls')
        print("""
Stealth
            """)
        print(a.StealthFullBody)
        time.sleep(timer)
    #Interaction instigators
    elif NextTile == 7:
        os.system('cls')
        print("""
Chest found""")
        APorHP = random.randint(0,1)
        if APorHP == 0:
            HPItem = random.randint(1, 6)
            if HPItem == 1 or HPItem == 2 or HPItem == 3:
                HPItemsList.append(1)
                print("band aid")
            elif HPItem == 4 or HPItem == 5:
                HPItemsList.append(2)
                print("bandage")
            elif HPItem == 6:
                HPItemsList.append(3)
                print("tourniquet")
        elif APorHP == 1:
            APItem = random.randint(1, 6)
            if APItem == 1 or APItem == 2 or APItem == 3:
                print("electrolytes")
                APItemList.append(1)
            elif APItem == 4 or APItem == 5:
                print("caffeine tablets")
                APItemList.append(2)
            elif APItem == 6:
                print("liquid amphetamines")
                APItemList.append(3)
                
        time.sleep(timer)
    elif NextTile == 8:
        os.system('cls')
        LourSelect = random.randint(1, 11)
        if LourSelect == 1:
            scrollTxt("""
The air here is so heavy, it stinks of iron and death.
i can't place my finger on it but the walls here feel like they're listening
hopefully we can find some fuel to get out of here
it feels like walking through an old grave yard.""")
        elif LourSelect == 2:
            scrollTxt("""
A warning to any who find this
leave in any capacity that you can
this place will subject you to things worse than death
i've forgot what humanity even means cause of this place""")
        elif LourSelect == 3:
            scrollTxt("""
I don't believe it 
this can't be real
we thought it was a person
but something was very wrong with them
there was no soul
only purpose 
who could stomach creating such an abomination""")
        elif LourSelect == 4:
            scrollTxt("""
wyecTHEwieucbfWALLShfkbvAREiseybALIVEsrvse
sryvbTHEYsiruvbSEEysrvYOUsrv""")
        elif LourSelect == 5:
            scrollTxt("Don't trust the overseer")
        elif LourSelect == 6:
            scrollTxt("This isn't your skin")
        elif LourSelect == 7:
            scrollTxt("Thief")
        elif LourSelect == 8:
            scrollTxt("Your existence proves Nietzsche right")
        elif LourSelect == 9:
            scrollTxt("""
Log 01 - ID Captain, Mr Xavier:
    we have reached stable orbit, solar panels are fully deployed and all glucose replicators are operational 
    they still won't tell us why we are here or what for.
    I've flown hundred of mining facilities out to their dig sites, and even more researchers to the next "universe defining outpost"
    but this feels different, the suits said it should be no different but I don't like it.
    The researchers seem closer to cult members than anything.""")
        elif LourSelect == 10:
            scrollTxt("""
Log 37 - ID Medical Officer, Dr Martin:
    It's been a month onboard the Fulcrum and it seems that no one knows what is really happening,
    but there is a rumor that we are here on some top secret mission to help with the food shortage on titan, 
    my question is: why have us do it at such an isolated location, 
    another thing is that they keep getting me to look at tissue sample, 
    i understand that lab grown meat is a possibility but that doesn't explain the adrenal glands
    i found within the supposedly lab grown pieces.""")
        elif LourSelect == 11:
            scrollTxt("""
Log 17 - ID Power Grid Engineer, Miss Lamarr:
    It makes 0 sense, why would we need so much power, this is a researchers facility for useless rocks,
    so why am I managing enough power to light up new california republic for a year.
    There has to be a reason, a shame that we're strictly forbids from asking about it,
    i'm starting to understand why so many had passed up on this job.""")
        time.sleep(3)

#Players Item Inventory
def ItemInventory():
    os.system('cls')
    PlayerMaxHP = 50
    PlayerMaxAP = 3
    print(a.Menu)
    print("Health Items")
    print(f"1. You have {HPItemsList.count(1)} band aids")
    print(f"2. You have {HPItemsList.count(2)} bandages")
    print(f"3. You have {HPItemsList.count(3)} tourniquets")

    print("Action Point Items")
    print(f"4. You have {APItemList.count(1)} electrolytes.")
    print(f"5. You have {APItemList.count(2)} caffeine tablets.")
    print(f"6. You have {APItemList.count(3)} liquid amphetamines.")   
    print("What item do you want to use. ")
    InvInput = msvcrt.getch()
    InvInput = chr(ord(InvInput))
    if InvInput == "1":
        if HPItemsList.count(1) <= 0:
            print("You don't have any of this item.")
        else:
            HPItemsList.remove(1)
            if Player.PlayerHP + 3 >= PlayerMaxHP:
                Player.PlayerHP = PlayerMaxHP
                print("Item used")
            else:
                Player.PlayerHP += 3
                print("Item used")

    elif InvInput == "2":
        if HPItemsList.count(2) <= 0:
            print("You don't have any of this item.")
        else:
            HPItemsList.remove(2)
            if Player.PlayerHP + 7 >= PlayerMaxHP:
                Player.PlayerHP = PlayerMaxHP
                print("Item used")
            else:
                Player.PlayerHP += 7
                print("Item used")
    elif InvInput == "3":
        if HPItemsList.count(3) <= 0:
            print("You don't have any of this item.")
        else:
            HPItemsList.remove(3)
            if Player.PlayerHP + 15 >= PlayerMaxHP:
                Player.PlayerHP = PlayerMaxHP
                print("Item used")
            else:
                Player.PlayerHP += 15
                print("Item used")
            
    elif InvInput == "4":
        if APItemList.count(1) <= 0:
            print("You don't have any of this item.")
        else:
            APItemList.remove(1)
            if Player.PlayerAP + 1 >= PlayerMaxAP:
                Player.PlayerAP = PlayerMaxAP
                print("Item used")
            else:
                Player.PlayerAP += 1
                print("Item used")
                
    elif InvInput == "5":
        if APItemList.count(2) <= 0:
            print("You don't have any of this item.")
        else:
            APItemList.remove(2)
            if Player.PlayerAP + 2 >= PlayerMaxAP:
                Player.PlayerAP = PlayerMaxAP
                print("Item used")
            else:
                Player.PlayerAP += 2
                print("Item used")
            
    elif InvInput == "6":
        if APItemList.count(3) <= 0:
            print("You don't have any of this item.")
        else:
            APItemList.remove(3)
            if Player.PlayerAP + 3 >= PlayerMaxAP:
                Player.PlayerAP = PlayerMaxAP
                print("Item used")
            else:
                Player.PlayerAP += 3
                print("Item used")
    elif InvInput == "e":
        player.PlayerStats()
    InvInput = msvcrt.getch()
    while chr(ord(InvInput)) != "m":
        os.system('cls')
        if InvInput == b'\x03':
            quit()
        else:
            InvInput = chr(ord(InvInput))
            print(a.Menu)
            print("Health Items")
            print(f"1. You have {HPItemsList.count(1)} band aids")
            print(f"2. You have {HPItemsList.count(2)} bandages")
            print(f"3. You have {HPItemsList.count(3)} tourniquets")
            
            print("Action Point Items")
            print(f"4. You have {APItemList.count(1)} electrolytes.")
            print(f"5. You have {APItemList.count(2)} caffeine tablets.")
            print(f"6. You have {APItemList.count(3)} liquid amphetamines.")   

            print("What item do you want to use. ")
            if InvInput == "1":
                if HPItemsList.count(1) <= 0:
                    print("You don't have any of this item.")
                else:
                    HPItemsList.remove(1)
                    if Player.PlayerHP + 3 >= PlayerMaxHP:
                        Player.PlayerHP = PlayerMaxHP
                        print("Item used")
                    else:
                        Player.PlayerHP += 3
                        print("Item used")
            elif InvInput == "2":
                if HPItemsList.count(2) <= 0:
                    print("You don't have any of this item.")
                else:
                    HPItemsList.remove(2)
                    if Player.PlayerHP + 7 >= PlayerMaxHP:
                        Player.PlayerHP = PlayerMaxHP
                        print("Item used")
                    else:
                        Player.PlayerHP += 7
                        print("Item used")
            elif InvInput == "3":
                if HPItemsList.count(3) <= 0:
                    print("You don't have any of this item.")
                else:
                    HPItemsList.remove(3)
                    if Player.PlayerHP + 15 >= PlayerMaxHP:
                        Player.PlayerHP = PlayerMaxHP
                        print("Item used")
                    else:
                        Player.PlayerHP += 15
                        print("Item used")
                    
            elif InvInput == "4":
                if APItemList.count(1) <= 0:
                    print("You don't have any of this item.")
                else:
                    APItemList.remove(1)
                    if Player.PlayerAP + 1 >= PlayerMaxAP:
                        Player.PlayerAP = PlayerMaxAP
                        print("Item used")
                    else:
                        Player.PlayerAP += 1
                        print("Item used")
            elif InvInput == "5":
                if APItemList.count(2) <= 0:
                    print("You don't have any of this item.")
                else:
                    APItemList.remove(2)
                    if Player.PlayerAP + 2 >= PlayerMaxAP:
                        Player.PlayerAP = PlayerMaxAP
                        print("Item used")
                    else:
                        Player.PlayerAP += 2
                        print("Item used")
            elif InvInput == "6":
                if APItemList.count(3) <= 0:
                    print("You don't have any of this item.")
                else:
                    APItemList.remove(3)
                    if Player.PlayerAP + 3 >= PlayerMaxAP:
                        Player.PlayerAP = PlayerMaxAP
                        print("Item used")
                    else:
                        Player.PlayerAP += 3
                        print("Item used")
            elif InvInput == "e":
                player.PlayerStats()
                
            InvInput = msvcrt.getch()


#def Help():
    
if __name__ == "__main__":    
    #Enemy Dictionary   
    EnemyDict = {
        "Imp": Imp(MainGameLevel),
        "Strong": Strong(MainGameLevel),
        "Fast": Fast(MainGameLevel),
        "Stealth":Stealth(MainGameLevel)
    }
    
    while True:
        Mz = GenerateMaze(15)
        SpawnEnemies(Mz, EnemyDict)
        PrintMaze(Mz)
        print(MainGameLevel)
        while CheckPlayerFinish(Mz) == False:
            PrintMaze(Mz)    
            Interaction(ChangePlayerPosition(Mz))