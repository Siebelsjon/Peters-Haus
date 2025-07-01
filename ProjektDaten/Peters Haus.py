import pygame, time, sys, random, subprocess
from pathlib import Path
pygame.init()

icon = pygame.image.load("Texturen - 64x64\Mario.png")
screen = pygame.display.set_mode((15*64,12*64))
pygame.display.set_caption("Peters Haus")
pygame.display.set_icon(icon)
solids = []

#AUDIO


def update():
    # Häufig Wiederholte Befehlsabfolge
    pygame.display.update()
    pygame.display.flip()

class preset:
    def __init__(self,textur,solids,anom,arg):
        self.texture = textur
        self.solids = solids
        self.anomaly = anom
        self.args = arg
        
class presets:
    def __init__(self):
        self.presets = []
        
    def readPresets(self):
        counter = 0
        First = True
        datei = open('räume.txt','r') # Wichtig! räume.txt durch dateiname ersetzten
        ersteZeile =True
        anomaly = 0
        coordComp = 0
        solidsPre = []
        for zeile in datei:
            temp = len(zeile)
            anzahlPresets = temp/3
            if counter == 0:
                # Texturname
                textur = ""
                for x in range(len(zeile)-1):
                    textur = textur + zeile[x]
                
                counter = 1
            elif counter == 1:
                counter = 2
                coordComp = 0
                # Solids Koordinaten
                for char in range(temp):
                    if zeile[char] == "(" or zeile[char] == ")" or zeile[char] == ",":
                        pass
                    else:
                        if coordComp == 0:
                            currentX = zeile[char]
                            
                            coordComp = 1
                        elif coordComp == 1:
                            currentY = zeile[char]
                            
                            solidsPre.append((int(currentX),int(currentY)))
                            coordComp = 0
                
            elif counter == 2:
                if First == False:
                    anomaly = True
                elif First == True:
                    anomaly = False
                    First = False
                    
                
                
                counter = 3
                
            elif counter == 3:
                counter = 0
                args = []
                next = False
                for char in range(temp):
                    if zeile[char] == "-":
                        next = True
                    elif zeile[char] == " ":
                        next = False
                        
                    if zeile[char] != "-" and next and zeile[char] != " ":
                        args.append(str(zeile[char]))
                        
                self.presets.append(preset(textur,solidsPre,anomaly,args))
                solidsPre = []
            else:
                print("error")
                counter = 0
                
    def temp(self):
        for i in self.presets:
            print(i.solids)
            print(i.texture)

class Background:
    def __init__(self):
        self.textur = "Texturen - 64x64/textur1.png"
        self.img = pygame.image.load(self.textur)
        screen.blit(self.img,(0,0))
        
        
    def updater(self):
        screen.blit(self.img,(0,0))
        #update()
    def setIMG(self,neuText):
        self.textur = neuText
        self.img = pygame.image.load(self.textur)
        self.updater()
        
class Ereignis:
    def __init__(self):
        self.first = True
        self.current = preseter.presets[0]
        
        self.verz = Path("Texturen - 64x64/"+self.current.texture)
        #self.end = ".png"
        Background.setIMG(self.verz)
        print("Peters Haus: Wenn du eine Anomalie siehst drücke: A, wenn nicht dann: W. Du musst es fünfmal hintereinander richtig erraten um zu gewinnen, am anfang ist es immer keine Anomalie")
    def Ereignis(self,er):
        if er == "a":
            pass
        elif er == "A":
            pass
        elif er == "b":
            pass
        elif er == "B":
            pass
    def nächstEreig(self):
        rand = random.randint(0,len(preseter.presets)+4)
            
       
        if rand>len(preseter.presets)-1:
            self.current = preseter.presets[0]
        else:
            self.current = preseter.presets[rand]
        
        self.verz = Path("Texturen - 64x64/"+self.current.texture)
        Background.setIMG(self.verz)
    def sieg(self):
        print("Gut gemacht, du hast alle Anomalien erkannt")
        self.verz = Path("Texturen - 64x64/sieg.png")
        Background.setIMG(self.verz)
        


            
class Game:
    # Manager aller Klassen - startet und managed den Spielablauf
    def main(self):
        pygame.mouse.set_visible(False)
        # Start Essentieler Sachen
        #solids.append((0,0))
        #solids.append((1,0))
        cursor = True
        update()
        
        preseter.readPresets()
        Ereig = Ereignis()
        run = True
        cursor = pygame.image.load("Texturen - 64x64\peter.png")
        level = 0
        easter = None
        while run:
            #Spielablauf
            time.sleep(1/60)
            Background.updater()
            pos1=pygame.mouse.get_pos()
            #print(pos1)
            pos1X= pos1[0]
            pos1Y = pos1[1]
            if cursor:
                screen.blit(cursor,(pos1X-1000,pos1Y-1000))
            update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()
                
                # Verarbeitet Inputs der Tastatur
                
                #pos1=pygame.mouse.get_pos()
                #print(pos1)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        easter = "p"
                    elif event.key == pygame.K_i:
                        if easter == "p":
                            easter = "pi"
                    elif event.key == pygame.K_n:
                        if easter == "pi":
                            easter = "pin"
                    elif event.key == pygame.K_g:
                        if easter == "pin":
                            easter = "ping"
                    elif event.key == pygame.K_u:
                        if easter == "ping":
                            subprocess.run(["python","MiniGameMaster\\realDrachenGames2.py"])
                    elif event.key == pygame.K_a:
                        easter = None
                        if Ereig.current.anomaly == True:
                            level = level + 1
                            if level < 5:
                                print("Level ", level, "/5")
                                Ereig.nächstEreig()
                            else:
                                print("Level ", level, "/5")
                                cursor = False
                                Ereig.sieg()
                        else:
                            level = 0
                            print("Level ", level, "/5")
                            Ereig.nächstEreig()
                    elif event.key == pygame.K_w:
                        easter = None
                        if Ereig.current.anomaly == False:
                            level = level + 1
                            if level < 5:
                                print("Level ", level, "/5")
                                Ereig.nächstEreig()
                            else:
                                print("Level ", level, "/5")
                                cursor = False
                                Ereig.sieg()
                        else:
                            level = 0
                            print("Level ", level, "/5")
                            Ereig.nächstEreig()
                    else:
                        easter = None
                        
                        
preseter = presets()
Background = Background()                
main = Game()
main.main()
