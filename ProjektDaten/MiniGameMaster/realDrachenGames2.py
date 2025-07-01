import pygame, time, sys, random

pygame.init()
pygame.mixer.init()
solids = ()
# Fenster und so basic Pygame-Settings
icon = pygame.image.load("Texturen - 64x64/RainerWinkler.jpg")
screen = pygame.display.set_mode((10 * 64, 10 * 64))  # Fenstergröße 640x640
pygame.display.set_caption("THE REAL-ORIGINAL-TRIOLIGY OF DRACHENGAMES")  # Fenstertitel
pygame.display.set_icon(icon)  # Fenstericon

clock = pygame.time.Clock()
font = pygame.font.SysFont("Alte Schwabacher", 30)

# Soundeffekte laden
fallen_sound = pygame.mixer.Sound("Sounds/Drachenschrei.mp3")
fallen_sound.set_volume(0.5)
laufen_sound = pygame.mixer.Sound("Sounds/laufensound.mp3")
laufen_sound.set_volume(0.3)


def update():
    # Bildschirm aktualisieren (Flip + Update)
    pygame.display.update()
    pygame.display.flip()


class Eisblock:
    def __init__(self, x, y):
        # Position auf dem Raster (1-basiert)
        self.x = x + 1
        self.y = y + 1
        self.status = "normal"
        self.betretenZeit = None  # zeit wann brechen
        self.health = 15  # Leben
        self.texture_normal = pygame.image.load("Texturen - 64x64/Eisjunge1.png")
        self.texture_rissig = pygame.image.load("Texturen - 64x64/Eisjunge2.png")

    def update(self):
        # Wenn rissig dann nach 2 Sekunden Block entfernen
        if self.status == "rissig" and self.betretenZeit:
            if time.time() - self.betretenZeit > 2:
                self.status = "weg"

    def draw(self):
        # Textur je nach Status
        if self.status == "normal":
            screen.blit(self.texture_normal, (self.x * 64, self.y * 64))
        elif self.status == "rissig":
            screen.blit(self.texture_rissig, (self.x * 64, self.y * 64))


    def setStatus(self, status):
        # Status setzen und Zeit merken wenn rissig
        if status == "n":
            self.status = "normal"
        elif status == "r":
            self.status = "rissig"
            self.betretenZeit = time.time()
        elif status == "w":
            self.status = "weg"


    def setHealth(self):
        # Leben zurücksetzen
        self.health = 15


class BackgroundEngine:
    def __init__(self):
        self.eisBlöcke = []  # liste der Eisblöcke
        self.Texture = pygame.image.load("Texturen - 64x64/Eiswasser.png")  # Hintergrundbild wenn kein Eisblock mehr da

    def EngineRun(self):
        # Eisblöcke neu erstellen (8x8 Grid)
        self.eisBlöcke = []
        for y in range(8):
            row = []
            for x in range(8):
                row.append(Eisblock(x, y))
            self.eisBlöcke.append(row)

    def redraw(self):
        pygame.display.flip()
        # Hintergrund und alle Eisblöcke zeichnen
        screen.blit(self.Texture, (0, 0))
        for row in self.eisBlöcke:
            for block in row:
                block.update()
                block.draw()
        # Spieler nur zeichnen wenn sichtbar
        if Mario.visible:
            Mario.update()
        if Peter.visible:
            Peter.update()
        update()

    def checkerTobi(self):
        # Für jeden Spieler den Block unter ihm leicht brechen
        for player in [Mario, Peter]:
            pos = (int(player.PlayerPosX / 64 - 1), int(player.PlayerPosY / 64 - 1))
            block = self.eisBlöcke[pos[1]][pos[0]]
            block.health -= 1
            # Block status ändern wenn jeweils Gesundheit aufgebraucht
            if block.health <= 0:
                if block.status == "normal":
                    block.setStatus("r")
                    block.setHealth()
                elif block.status == "rissig":
                    block.setStatus("w")
                    block.setHealth()


class Player:
    def __init__(self, id):
        self.visible = True
        # Verschiedene Texturen für Player
        if id == 0:
            self.Player = pygame.image.load("Texturen - 64x64/Pinguin1.png")
        elif id == 1:
            self.Player = pygame.image.load("Texturen - 64x64/Pinguin.png")
        # random Startposition
        self.PlayerPosX = random.randint(1, 8) * 64
        self.PlayerPosY = random.randint(1, 8) * 64
        self.pos = (self.PlayerPosX // 64, self.PlayerPosY // 64)
        self.last_move_time = 0  # letzter Zeitpunkt der Bewegung
        self.move_couldown = 0.2  # couldown zwischen Bewegungen damit kein dummes Gespamme

    def get_grid_pos(self):
        return (self.PlayerPosX // 64, self.PlayerPosY // 64)

    def update(self):
        if self.visible:
            screen.blit(self.Player, (self.PlayerPosX, self.PlayerPosY))

    def Bewegen(self, richtung):
        if time.time() - self.last_move_time < self.move_couldown:
            return
        self.last_move_time = time.time()
        # Bewegung in Richtung um 64 Pixel also 1 Block
        alte_pos = (self.PlayerPosX, self.PlayerPosY)
        neue_pos = alte_pos

        if richtung == "up" and self.PlayerPosY > 64:
            neue_pos = (self.PlayerPosX, self.PlayerPosY - 64)
        elif richtung == "down" and self.PlayerPosY < 8 * 64:
            neue_pos = (self.PlayerPosX, self.PlayerPosY + 64)
        elif richtung == "left" and self.PlayerPosX > 64:
            neue_pos = (self.PlayerPosX - 64, self.PlayerPosY)
        elif richtung == "right" and self.PlayerPosX < 8 * 64:
            neue_pos = (self.PlayerPosX + 64, self.PlayerPosY)
        else:
            # Wenn Bewegung über Rand, Spieler fällt ins Wasser
            if self == Peter:
                GameMaster.player_falls("Peter")
            if self == Mario:
                GameMaster.player_falls("Mario")

        ziel = (neue_pos[0] // 64, neue_pos[1] // 64)
        anderer_spieler = Mario if self == Peter else Peter
        andere_pos = anderer_spieler.get_grid_pos()

        if ziel == andere_pos:
            return  # Blockiert durch anderen Spieler

        self.PlayerPosX, self.PlayerPosY = neue_pos
        self.pos = ziel

        laufen_sound.play()

        if self.visible:
            screen.blit(self.Player, (self.PlayerPosX, self.PlayerPosY))

    def check(self):
        # Prüfen ob Spieler auf weg Block steht -> fällt ins Wasser
        self.pos = (int(self.PlayerPosX / 64 - 1), int(self.PlayerPosY / 64 - 1))
        status = Background.eisBlöcke[self.pos[1]][self.pos[0]].status

        if status == "weg":
            if self == Peter:
                GameMaster.player_falls("Peter")
            if self == Mario:
                GameMaster.player_falls("Mario")


class Schaufel(Eisblock, BackgroundEngine):
    def __init__(self):
        self.visible = False
        self.counter = 0
        self.Owner = None

        # Textur der Schaufel
        self.Schaufel = pygame.image.load("Texturen - 64x64/DevTexture.png")
        self.SchaufelPosX = random.randint(1, 8) * 64
        self.SchaufelPosY = random.randint(1, 8) * 64

    def Schaufelaktion(self):
        self.Timer()
        self.Schaufelchecker()
        if self.visible == True:
            screen.blit(self.Schaufel, (self.SchaufelPosX, self.SchaufelPosY))

    def Timer(self):
        self.counter = self.counter + 1
        if self.counter == 60:
            self.visible = True

    def Schaufelchecker(self):
        if Mario.get_grid_pos() == (self.SchaufelPosX / 64, self.SchaufelPosY / 64) and self.visible:
            self.visible = False
            self.Owner = "Mario"
        if Peter.get_grid_pos() == (self.SchaufelPosX / 64, self.SchaufelPosY / 64) and self.visible:
            self.visible = False
            self.Owner = "Peter"

    def Schaufeln(self, Auslöser):
        if self.Owner == "Mario" and Auslöser == "Mario":
            Background.eisBlöcke[3][3].setStatus("w")
            Background.eisBlöcke[4][3].setStatus("w")
            Background.eisBlöcke[3][4].setStatus("w")
            Background.eisBlöcke[4][4].setStatus("w")
            print("Wusr")
            self.counter = 0
            self.Owner = None
            #screen.blit(texture_normal , (self.x * 64, self.y * 64))
        if self.Owner == "Peter" and Auslöser == "Peter":
            Background.eisBlöcke[3][3].setStatus("w")
            Background.eisBlöcke[4][3].setStatus("w")
            Background.eisBlöcke[3][4].setStatus("w")
            Background.eisBlöcke[4][4].setStatus("w")
            print("Wutsr")
            self.counter = 0
            self.Owner = None
            #screen.blit(texture_normal, (self.x * 64, self.y * 64))
        print("Schaufel")


class Game:
    def main(self):
        GameMaster.Background = Background
        Background.EngineRun()  # Eisblöcke initialisieren
        self.score = {"Mario": 0, "Peter": 0}
        run = True
        Background.redraw()

        while run:
            Background.checkerTobi()  # Eisblöcke unter Spielern anbrechen
            Background.redraw()
            Eisen.Schaufelaktion()
            Peter.check()  # Prüfen ob Peter fällt
            Mario.check()  # Prüfen ob Mario fällt
            Peter.update()
            Mario.update()

            update()

            # Abfrage für Steuerung
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    # Bewegung Mario (Pfeiltasten)
                    if event.key == pygame.K_UP:
                        Mario.Bewegen("up")
                    elif event.key == pygame.K_DOWN:
                        Mario.Bewegen("down")
                    elif event.key == pygame.K_LEFT:
                        Mario.Bewegen("left")
                    elif event.key == pygame.K_RIGHT:
                        Mario.Bewegen("right")

                    # Bewegung Peter (WASD)
                    elif event.key == pygame.K_w:
                        Peter.Bewegen("up")
                    elif event.key == pygame.K_s:
                        Peter.Bewegen("down")
                    elif event.key == pygame.K_a:
                        Peter.Bewegen("left")
                    elif event.key == pygame.K_d:
                        Peter.Bewegen("right")

                    if event.key == pygame.K_m:
                        Eisen.Schaufeln("Mario")

                    if event.key == pygame.K_e:
                        Eisen.Schaufeln("Peter")

                    Mario.update()
                    Peter.update()

            time.sleep(1 / 30)  # Framerate ~30 FPS

    def player_falls(self, name):
        # Spieler fällt ins Wasser
        print("von Robben gefressen")
        fallen_sound.play()

        if name == "Mario":
            Mario.visible = False  # Spieler unsichtbar machen nach Tot
            self.score["Peter"] += 1  # Gegner bekommt Punkt
        elif name == "Peter":
            Peter.visible = False
            self.score["Mario"] += 1

        Background.redraw()
        self.mach_score()
        pygame.display.flip()

        print(f"Punktestand: Mario {self.score['Mario']} - Peter {self.score['Peter']}")

        self.reset_players()
        Background.EngineRun()

        # Enter um sleep couldown zu überspringen
        counter = 0

        warten = True
        while warten:
            if counter > 300:
                warten = False
            time.sleep(1 / 30)
            counter = counter + 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        warten = False

    def mach_score(self):
        # Punktestand anzeigen
        Mario_text = (f" Mario {self.score['Mario']}")
        Mario_surface = font.render(Mario_text, True, (0, 0, 125))
        Peter_text = (f" Peter {self.score['Peter']}")
        Peter_surface = font.render(Peter_text, True, (225, 0, 0))

        screen.blit(Mario_surface, (10, 10))
        screen.blit(Peter_surface, (10, 50))

    def reset_players(self):
        # Spieler nach erstem Game an zufälligen Position  setzen
        for player in [Mario, Peter]:
            player.PlayerPosX = random.randint(1, 8) * 64
            player.PlayerPosY = random.randint(1, 8) * 64
            player.visible = True
            player.pos = (player.PlayerPosX // 64, player.PlayerPosY // 64)


# Spiel starten
Background = BackgroundEngine()
Mario = Player(0)
Peter = Player(1)
Eisen = Schaufel()
GameMaster = Game()
GameMaster.main()
GameMaster.mach_score()
