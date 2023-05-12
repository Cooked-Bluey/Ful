import random
import ArtAndAssest as a
import os
import msvcrt
import time
import sys

#Level Counter
MainGameLevel = 1

#Player Class
PlayerMaxHP = 50
PlayerMaxAP = 3
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
        PlayerDmg = 10
        PlayerDmg = PlayerDmg + self.EquippedLeftArm.DMGBoost + self.EquippedRightArm.DMGBoost + self.EquippedTorso.DMGBoost + self.EquippedLeftLeg.DMGBoost + self.EquippedRightLeg.DMGBoost
        PlayerMaxAP = 3
        PlayerMaxAP = PlayerMaxAP + self.EquippedLeftArm.APBoost + self.EquippedRightArm.APBoost + self.EquippedTorso.APBoost + self.EquippedLeftLeg.APBoost + self.EquippedRightLeg.APBoost
        PlayerMaxHP = 50
        PlayerMaxHP = PlayerMaxHP + self.EquippedLeftArm.HPBoost + self.EquippedRightArm.HPBoost + self.EquippedTorso.HPBoost + self.EquippedLeftLeg.HPBoost + self.EquippedRightLeg.HPBoost
    #Player Stats Page
    def PlayerStats(self):
        global BackToInteraction
        os.system('cls')
        if InCombat == True:
            print(a.AttackMenu)
            BackToInteraction = 'a'
            self.PlayerStatsRepeats()
            print(CurrentEnemyImage)
            print(a.AttackMenu)
        elif InCombat == False:
            print(a.Menu)
            BackToInteraction = 'm'
            self.PlayerStatsRepeats()

        
    def PlayerStatsRepeats(self):
        print(f"You currently have {player.PlayerHP}HP")
        print(f"You currently have {player.PlayerAP}AP")
        print(f"You currently deal {player.PlayerDmg}Dmg")
        print(f"{str(self.EquippedLeftArm.Name)}:       {str(self.EquippedRightArm.Name)}:")
        print(f"+{int(self.EquippedLeftArm.DMGBoost)}Dmg, +{int(self.EquippedLeftArm.APBoost)}AP, +{int(self.EquippedRightArm.HPBoost)}HP.  +{int(self.EquippedRightArm.DMGBoost)}Dmg, +{int(self.EquippedRightArm.APBoost)}AP, +{int(self.EquippedRightArm.HPBoost)}HP.")
        print("")
        print(f"            {str(self.EquippedTorso.Name)}")
        print(f"            +{int(self.EquippedTorso.DMGBoost)}Dmg, +{int(self.EquippedTorso.APBoost)}AP, +{int(self.EquippedTorso.HPBoost)}HP.")
        print("")
        print(f"{str(self.EquippedLeftLeg.Name)}:       {str(self.EquippedRightLeg.Name)}:")
        print(f"+{int(self.EquippedLeftLeg.DMGBoost)}Dmg, +{int(self.EquippedLeftLeg.APBoost)}AP, +{int(self.EquippedLeftLeg.HPBoost)}HP.  +{int(self.EquippedRightLeg.DMGBoost)}Dmg, +{int(self.EquippedRightLeg.APBoost)}AP, +{int(self.EquippedRightLeg.HPBoost)}HP.")
        StatInput = '#'
        while StatInput != BackToInteraction:
            if self.Inventory == []:
                print("You haven't picked up any limbs")
            else:
                if self.PlayerAP < 0:
                    self.PlayerAP = 0

                    if self.PlayerAP > 0:
                        print("Would you like to exchange any limbs from your storage? (y/n) ")
                        StatInput = msvcrt.getch()
                        StatInput = chr(ord(StatInput))
                        if StatInput == 'y':
                            print("You hate that you need to do this.")
                            self.SwapLimbs()
                            StatInputAgain = input("Would you like to swap anything else? (y/n) ")
                            while StatInputAgain == "y":
                                self.SwapLimbs()
                                StatInputAgain = input("Would you like to swap anything else? (y/n) ")
                        elif StatInput == 'n':
                            scrollTxt("Your bag closes the limbs inside writhe in protest.")
                    else: 
                        scrollTxt("You do not have enough AP to swap out any limbs, \n")
                        scrollTxt("you would die from exhaustion \n")
                scrollTxt("Select a new menu.")
                StatInput = msvcrt.getch()
                StatInput = chr(ord(StatInput))
                os.system('cls')
            if StatInput == 'i':
                ItemInventory()
            elif StatInput == "h":
                Help()

    #Limb Swapping Function
    def SwapLimbs(self):
        for i in range(len(self.Inventory)):
            print(str(i+1) + ": " + self.Inventory[i].Name)
            print(f"{int(self.Inventory[i].DMGBoost)}DMG, {int(self.Inventory[i].HPBoost)}HP, {int(self.Inventory[i].APBoost)}AP.")
        
        LimbNumber = int(input("Swap Item Number: ")) - 1
        
        self.PlayerAP -= 1
        
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
        player.PlayerDmg = 10
        player.PlayerDmg = player.PlayerDmg + self.EquippedLeftArm.DMGBoost + self.EquippedRightArm.DMGBoost + self.EquippedTorso.DMGBoost + self.EquippedLeftLeg.DMGBoost + self.EquippedRightLeg.DMGBoost
        PlayerMaxAP = 3
        PlayerMaxAP = PlayerMaxAP + self.EquippedLeftArm.APBoost + self.EquippedRightArm.APBoost + self.EquippedTorso.APBoost + self.EquippedLeftLeg.APBoost + self.EquippedRightLeg.APBoost
        PlayerMaxHP = 50
        PlayerMaxHP = PlayerMaxHP + self.EquippedLeftArm.HPBoost + self.EquippedRightArm.HPBoost + self.EquippedTorso.HPBoost + self.EquippedLeftLeg.HPBoost + self.EquippedRightLeg.HPBoost

#Broader Enemy Class
InCombat = False
class Enemy():
    def __init__(self, Name, HP, AP, DMG, SpawnCount, Level = MainGameLevel):
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
    
    def EnemyCombatTurn(self):
        if player.PlayerHP < self.AP * self.DMG:
            player.PlayerHP = 0
        else:
            player.PlayerHP -= self.AP * self.DMG
            print(f"You have {player.PlayerHP}HP and the {self.Name} attacked for {self.AP * self.DMG}")
            
    def PlayerCombatTurn(self):
        ComInput = msvcrt.getch()
        ComInput = chr(ord(ComInput))
        if ComInput == "e":
            player.PlayerStats()
        elif ComInput == "i":
            ItemInventory()
        elif ComInput == "a":
            player.PlayerAP -= 1
            if self.HP < player.PlayerDmg:
                self.HP = 0
                print(f"You have killed the {self.Name}")
                return self.HP
            else:
                self.HP -= player.PlayerDmg
                print(f"{self.Name} has {self.HP}HP left and you attacked for {player.PlayerDmg} and have {player.PlayerAP}AP")
    
    def Combat(self):
        global InCombat
        InCombat = True
        while player.PlayerHP > 0 and self.HP > 0:
            if player.PlayerAP > 0:
                self.PlayerCombatTurn()
            else:
                self.EnemyCombatTurn()
                player.PlayerAP = 3
        if player.PlayerHP <= 0:
            self.InCombat = False
            DeathScreen()
        elif self.HP <= 0:
            self.InCombat = False
            CurrentDroppedLimb = self.OnDeath()
            print(str(CurrentDroppedLimb.Name))
            print("Would you like to store this limb? (y/n)")
            ComInput = msvcrt.getch()
            ComInput = chr(ord(ComInput))
            while ComInput != 'y' and ComInput != 'n':
                print("Enter a valid input")
                ComInput = msvcrt.getch()
                ComInput = chr(ord(ComInput))
            if ComInput == 'y':
                player.Inventory.append(CurrentDroppedLimb)
                scrollTxt(f"You press the mass into the bag on you back and it makes contact with the rest of the meat.")
            elif ComInput == 'n':
                scrollTxt("You have discarded the rotting tissue.")
        return self.InCombat
    
    def Debug(self):
        print("HP: " + str(self.HP) + " AP: " + str(self.AP) + " DMG: " + str(self.DMG) + " Level: " + str(self.Level))
        lmb = self.OnDeath()        
        print("Limb- HP: " + str(lmb.HPBoost) + " DMG: " + str(lmb.DMGBoost) + " AP: " + str(lmb.APBoost) + " Name: " + lmb.Name + "\n")

#Enemy Type
class Imp(Enemy):
    def __init__(self, Level):
        DMGBoost = MainGameLevel * 2 #Tweak
        RandomHPChange = random.randint(-3, 3) #Tweak
        super(Imp, self).__init__("Imp", 15 + RandomHPChange, 1, 3 + DMGBoost, 1, Level)

class Strong(Enemy):
    def __init__(self, Level):
        DMGBoost = Level * 2 #Tweak
        RandomHPChange = random.randint(-3, 3) #Tweak
        super(Strong, self).__init__("Strong", 75 + RandomHPChange, 1, DMGBoost + 10, 5, Level)

class Stealth(Enemy):
    def __init__(self, Level):
        DMGBoost = Level * 2 #Tweak
        RandomHPChange = random.randint(-3, 3) #Tweak
        super(Stealth, self).__init__("Stealth", 35 + RandomHPChange, 3, DMGBoost + 5, 4, Level)

class Fast(Enemy):
    def __init__(self, Level):
        DMGBoost = Level * 2 #Tweak
        RandomHPChange = random.randint(-3, 3) #Tweak
        super(Fast, self).__init__("Fast", 25 + RandomHPChange, 5, DMGBoost + 4, 3, Level)

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

player = Player(50, 3, 10)

#Time.sleep Constant
timer = 5


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
                RowString += "██"
            elif Maze[Row][Column] == 2:
                RowString += "P " 
            elif Maze[Row][Column] == 0:
                RowString += "  "
            else: 
                RowString += str(Maze[Row][Column]) + " "
        print(RowString)
        
    print(a.Menu)
    print("Use WASD to move around the map.")

#Check if the player has reached the end of the maze
def CheckPlayerFinish(Maze):
    FinalRow = Maze[-1]
    if 2 in FinalRow:
        MainGameLevel += 1
        player.PlayerAP = PlayerMaxAP
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
        Help()
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
    global CurrentEnemyImage
    #Enemy instigators 
    #Imp
    if NextTile == 3:
        os.system('cls')
        print(a.ImpFullyBody)
        print(a.AttackMenu)
        CurrentEnemyImage = a.ImpFullyBody
        Imp(MainGameLevel).Combat()                                                        
        time.sleep(timer)

    #Fast
    elif NextTile == 4:
        os.system('cls')
        print(a.FastFullBody)
        print(a.AttackMenu)
        CurrentEnemyImage = a.FastFullBody
        Fast(MainGameLevel).Combat()
        time.sleep(timer)
    
    #Strong
    elif NextTile == 5:
        os.system('cls')
        print(a.StrongFullBody)
        print(a.AttackMenu)
        CurrentEnemyImage = a.StrongFullBody
        Strong(MainGameLevel).Combat()

        time.sleep(timer)
    
    #Stealth
    elif NextTile == 6:
        os.system('cls')
        print(a.StealthFullBody)
        print(a.AttackMenu)
        CurrentEnemyImage = a.StealthFullBody
        Stealth(MainGameLevel).Combat()
        time.sleep(timer)
    
    #Interaction instigators
    elif NextTile == 7:
        os.system('cls')
        print("""
Chest found
======================
Inside there was some:""")
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
        LoreSelect = random.randint(1, 11)
        if LoreSelect == 1:
            scrollTxt("""
The air here is so heavy, it stinks of iron and death.
i can't place my finger on it but the walls here feel like they're listening
hopefully we can find some fuel to get out of here
it feels like walking through an old grave yard.""")
        elif LoreSelect == 2:
            scrollTxt("""
A warning to any who find this
leave in any capacity that you can
this place will subject you to things worse than death
i've forgot what humanity even means cause of this place""")
        elif LoreSelect == 3:
            scrollTxt("""
I don't believe it 
this can't be real
we thought it was a person
but something was very wrong with them
there was no soul
only purpose 
who could stomach creating such an abomination""")
        elif LoreSelect == 4:
            scrollTxt("""
wyecTHEwieucbfWALLShfkbvAREiseybALIVEsrvse
sryvbTHEYsiruvbSEEysrvYOUsrv""")
        elif LoreSelect == 5:
            scrollTxt("Don't trust the overseer")
        elif LoreSelect == 6:
            scrollTxt("This isn't your skin")
        elif LoreSelect == 7:
            scrollTxt("Thief")
        elif LoreSelect == 8:
            scrollTxt("Your existence proves Nietzsche right")
        elif LoreSelect == 9:
            scrollTxt("""
Log 01 - ID Captain, Mr Xavier:
    we have reached stable orbit, solar panels are fully deployed and all glucose replicators are operational 
    they still won't tell us why we are here or what for.
    I've flown hundred of mining facilities out to their dig sites, and even more researchers to the next "universe defining outpost"
    but this feels different, the suits said it should be no different but I don't like it.
    The researchers seem closer to cult members than anything.""")
        elif LoreSelect == 10:
            scrollTxt("""
Log 37 - ID Medical Officer, Dr Martin:
    It's been a month onboard the Fulcrum and it seems that no one knows what is really happening,
    but there is a rumor that we are here on some top secret mission to help with the food shortage on titan, 
    my question is: why have us do it at such an isolated location, 
    another thing is that they keep getting me to look at tissue sample, 
    i understand that lab grown meat is a possibility but that doesn't explain the adrenal glands
    i found within the supposedly lab grown pieces.""")
        elif LoreSelect == 11:
            scrollTxt("""
Log 17 - ID Power Grid Engineer, Miss Lamarr:
    It makes 0 sense, why would we need so much power, this is a researchers facility for useless rocks,
    so why am I managing enough power to light up new california republic for a year.
    There has to be a reason, a shame that we're strictly forbids from asking about it,
    i'm starting to understand why so many had passed up on this job.""")
        time.sleep(3)

#Players Item Inventory
def ItemInventory():
    global InCombat
    os.system('cls')
    global BackToInteraction
    if InCombat == True:
        print(a.AttackMenu)
        BackToInteraction = 'a'
        ItemInvRepeatCode()
        os.system('cls')
        print(CurrentEnemyImage)
        print(a.AttackMenu)
    elif InCombat == False:
        print(a.Menu)
        BackToInteraction = 'm'
        ItemInvRepeatCode()
        os.system('cls')

def ItemInvRepeatCode():
    print("Health Items")
    print(f"1. You have {HPItemsList.count(1)} band aids")
    print(f"2. You have {HPItemsList.count(2)} bandages")
    print(f"3. You have {HPItemsList.count(3)} tourniquets")

    print("Action Point Items")
    print(f"4. You have {APItemList.count(1)} electrolytes.")
    print(f"5. You have {APItemList.count(2)} caffeine tablets.")
    print(f"6. You have {APItemList.count(3)} liquid amphetamines.")   
    print("What item do you want to use. ")
    InvInput = '#'
    while InvInput != BackToInteraction:
        InvInput = msvcrt.getch()
        InvInput = chr(ord(InvInput))
        if InvInput == b'\x03':
            quit()
        if InvInput == "1":
            if HPItemsList.count(1) <= 0:
                print("You don't have any of this item.")
            else:
                HPItemsList.remove(1)
                if player.PlayerHP + 3 >= PlayerMaxHP:
                    player.PlayerHP = PlayerMaxHP
                    print("Item used")
                else:
                    player.PlayerHP += 3
                    print("Item used")
                player.PlayerAP -= 1

        elif InvInput == "2":
            if HPItemsList.count(2) <= 0:
                print("You don't have any of this item.")
            else:
                HPItemsList.remove(2)
                if player.PlayerHP + 7 >= PlayerMaxHP:
                    player.PlayerHP = PlayerMaxHP
                    print("Item used")
                else:
                    player.PlayerHP += 7
                    print("Item used")
                player.PlayerAP -= 1

        elif InvInput == "3":
            if HPItemsList.count(3) <= 0:
                print("You don't have any of this item.")
            else:
                HPItemsList.remove(3)
                if player.PlayerHP + 15 >= PlayerMaxHP:
                    player.PlayerHP = PlayerMaxHP
                    print("Item used")
                else:
                    Player.PlayerHP += 15
                    print("Item used")
                player.PlayerAP -= 1
        elif InvInput == "4":
            if APItemList.count(1) <= 0:
                print("You don't have any of this item.")
            else:
                APItemList.remove(1)
                if player.PlayerAP + 1 >= PlayerMaxAP:
                    player.PlayerAP = PlayerMaxAP
                    print("Item used")
                else:
                    player.PlayerAP += 1
                    print("Item used")
                player.PlayerAP -= 1
        elif InvInput == "5":
            if APItemList.count(2) <= 0:
                print("You don't have any of this item.")
            else:
                APItemList.remove(2)
                if player.PlayerAP + 2 >= PlayerMaxAP:
                    player.PlayerAP = PlayerMaxAP
                    print("Item used")
                else:
                    player.PlayerAP += 2
                    print("Item used")
                player.PlayerAP -= 1
        elif InvInput == "6":
            if APItemList.count(3) <= 0:
                print("You don't have any of this item.")
            else:
                APItemList.remove(3)
                if player.PlayerAP + 3 >= PlayerMaxAP:
                    player.PlayerAP = PlayerMaxAP
                    print("Item used")
                else:
                    player.PlayerAP += 3
                    print("Item used")
                player.PlayerAP -= 1
        elif InvInput == "e":
            player.PlayerStats()
        elif InvInput == "h":
            Help()
    
def DeathScreen():
    scrollTxt("""You have perished aboard the happy meat farms genetic research facility.
Associated cleaning cost will be deducted from your families compensation.
We hope you enjoyed your stay.""")
    quit()
    
def Help():
    os.system('cls')
    scrollTxt("This is the help/tutorial page where different aspects of the game you are playing can be learnt about. \nYou can exit this menu at any point by pressing 'm' and can return to this page at any time. \nSo what would you like to know? \n")
    print("========================================")
    print("1. The maze, its features and functions.")
    time.sleep(0.05)
    print("2. The inventory and how to use it.")
    time.sleep(0.05)
    print("3. The status page what it tells you and how it's used.")
    print("Where you you like to go?")
    TutorialSection = msvcrt.getch()
    TutorialSection = chr(ord(TutorialSection))
    while TutorialSection != 'm':
        TutorialSection = msvcrt.getch()
        TutorialSection = chr(ord(TutorialSection))
        
        if TutorialSection == '1':
            os.system('cls')
            scrollTxt("""The Maze.\n
The maze is the main page of the game where progression is made and interactions are instigated. \n
As a result it can be confusing as there are many numbers on the screen that may not make sense. \n
To combat this here is a key for each item that will be found in the maze.\n""")
            print("""
- Player = P
- Imp = 3
- Fast = 4
- Strong = 5
- Stealth = 6
- Chest = 7
- Lore = 8
- Exit = 9""")
            print("Return to help menu? (y/n)")
            TutorialSection = msvcrt.getch()
            TutorialSection = chr(ord(TutorialSection))
            if TutorialSection == "y":
                Help()
            
            
        elif TutorialSection == '2':
            scrollTxt("""The Inventory is where all the items you have collected from chest will be stored. \n
These items are either HP (health point) or AP (action point) related items that have a one off use of rasing your current HP/AP \n
Items are used by inputting the corresponding number and the game should tell you if the item has been used.\n""")
            
            print("Return to help menu? (y/n)")
            TutorialSection = msvcrt.getch()
            TutorialSection = chr(ord(TutorialSection))
            if TutorialSection == "y":
                Help()
                
                
        elif TutorialSection == '3':
            scrollTxt("""The status page has 2 primary uses \n
The first is that it tells you your current HP, AP adn Dmg \n
The second use is that it is the place where limbs are swapped out, it being the the way of increasing power within the game. \n""")
            
            print("Return to help menu? (y/n)")
            TutorialSection = msvcrt.getch()
            TutorialSection = chr(ord(TutorialSection))
            if TutorialSection == "y":
                Help()



def EndOfGame():
    scrollTxt("""You arrive at the bridge, the very top of the ship. \n
You look out onto the deck of your metal casket, \n
You attempt to open the main computer but the system is broken. \n
All that is displayed is the date, December 27th, \n
4001. \n
You are stuck, not knowing what to believe, then the failing computer shuts off. \n
Your reflection stairs at you, \n
You are a monster of this ship now too. \n
We hope you enjoy your Stay.
""")
    quit()
def Intro():
    os.system('cls')
    scrollTxt("For the best experience play with the terminal fully open and zoomed in so you can read the text clearly")
    time.sleep(1)
    os.system('cls')
    scrollTxt("You wake up into a haze, air heavy and putrid. \nDecay seemingly the only constant about the room you wake up in all you know is that it is December 27th, year 3156 and that you need to survive. \nBut what ever is echoing those screams along the failing hull of the ship isn't going to make it easy.\n")
    time.sleep(0.05)
    print(a.title)
    scrollTxt("============================================ Happy Meat Farm's 13th Genetic Marvel ============================================")
    time.sleep(3)
if MainGameLevel == 20:
    EndOfGame()

if __name__ == "__main__":    
    #Enemy Dictionary   
    EnemyDict = {
        "Imp": Imp(2),
        "Strong": Strong(2),
        "Fast": Fast(2),
        "Stealth":Stealth(2)
    }
    
    Intro()
    while True:
        Mz = GenerateMaze(15)
        SpawnEnemies(Mz, EnemyDict)
        PrintMaze(Mz)
        print(MainGameLevel)
        while CheckPlayerFinish(Mz) == False:
            PrintMaze(Mz)    
            Interaction(ChangePlayerPosition(Mz))