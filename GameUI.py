import random
import time

from GameSound import gameSound
from Weapon import weapons
from Potion import potions

GAME_NAME = "FINDING THE CROWN"
BIG_STRING_LENGTH = 100
MEDIUM_STRING_LENGTH = 50

class GameUI:

    def __init__(self):
        self.lifes = 3
        self.points = 200
        self.weapons = [random.choice(weapons)]
        self.potions = [random.choice(potions)]
        self.wonnedBattles = 0
        self.state = "menu"
        self.input = None


    def showMessage(self, message):
        print(message)
        time.sleep(len(message) * 0.07)


    def askToPlayer(self, message):
        print()
        self.input = input("> " + message + ": ")
        print()


    def showHeader(self, title, type="small"):
        if (type == "big"):
            length = BIG_STRING_LENGTH
            spaces = length - len(title)
            left = spaces // 2
            right = spaces - left

            print(f'{"-" * length}\n{" " * left}{title}{" " * right}\n{"-" * length}')
        else:
            print(title.upper())
            print("-" * len(title))

    
    def goToState(self, state):
        self.state = state
        self.input = None


    def showMenu(self):
        self.showHeader(GAME_NAME, "big")
        print("1. Jugar")
        print("2. Configuraciones")
        print("3. Reglas del juego")
        print("4. Salir")
        self.askToPlayer("¿Qué quieres hacer?")

        if (self.input == "1"): self.goToState("game")
        elif (self.input == "2"): self.goToState("settings")
        elif (self.input == "3"): self.goToState("rules")
        elif (self.input == "4"): self.goToState("exit")


    def showGame(self):
        self.goToState("history")


    def showHistory(self):
        self.showMessage("Acabas de despertar en una habitación oscura y sombría.")
        self.showMessage("No recuerdas nada, ni siquiera tu nombre.")
        self.showMessage("De repente observas una caja con una nota encima de ella.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~   No sabría cómo explicártelo, pero es necesario que en    ~")
        print("~   cuanto despiertes, tomes lo que hay en la caja y vayas   ~")
        print("~   a la montaña en el oriente donde se encuentra el         ~")
        print("~   castillo abandonado. Busca la corona de esmeraldas y     ~")
        print("~   activa su poder para que puedas volver a tu mundo.       ~")
        print("~   Espero que tengas suerte, este mundo es muy peligroso.   ~")
        print("~                                                            ~")
        print("~   Con amor, tu madre.                                      ~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(10)
        self.showMessage("Abres la caja y encuentras un arma y una pocion.")
        self.showMessage(f'El arma es: {self.weapons[0].name}')
        self.showMessage(f'La pocion es: {self.potions[0].name}')
        self.showMessage("Te pones en pie y te diriges a la puerta.")
        self.showMessage("Abres la puerta y observas un largo pasillo.")
        self.showMessage("Te percatas que no hay nadie más en esa pequeña casa.")
        self.showMessage("Sales de la casa y escuchas que hay un rio a tu derecha.")

        self.goToState("walk")

    def walk(self):
        self.showMessage("Estas caminando...")

        foundPotion = random.choice([True, False])
        if (foundPotion): self.goToState("find-potion")

        isAttacked = random.choice([True, False])
        if (isAttacked): self.goToState("battle")


    def showSettings(self):
        self.showHeader("Configuraciones", MEDIUM_STRING_LENGTH)
        print("1. Volumen de la música")
        print("2. Volumen de los efectos de sonido")
        print("3. Volver al menú")
        self.askToPlayer("¿Qué quieres hacer?")

        if (self.input == "1"): self.goToState("music-settings")
        elif (self.input == "2"): self.goToState("sound-settings")
        elif (self.input == "3"): self.goToState("menu")


    def showMusicSettings(self):
        self.showHeader("Configuraciones de la música", MEDIUM_STRING_LENGTH)
        self.askToPlayer("¿Qué volumen quieres ponerle a la música? (0 - 5)")
        gameSound.setMusicVolume(float(self.input))
        self.goToState("settings")


    def showSoundSettings(self):
        self.showHeader("Configuraciones de los efectos de sonido", MEDIUM_STRING_LENGTH)
        self.askToPlayer("¿Qué volumen quieres ponerle a los efectos de sonido? (0 - 5)")
        gameSound.setSoundVolume(float(self.input))
        self.goToState("settings")


    def showRules(self):
        self.showHeader("Reglas del juego", MEDIUM_STRING_LENGTH)
        print(f'¡Bienvenido a {GAME_NAME}!')
        print("En esta aventura deberás enfrentarte a diferentes enemigos para sobrevivir en el juego.")
        print("Tu objetivo principal es buscar la corona perdida, que se encuentra en el castillo de la montaña.") 
        print("Pero para llegar allí deberás vencer a los enemigos que se encuentran en el camino.")
        print("Cada vez que ganes una batalla podrás tomar el arma del enemigo.")
        print("Puedes guardar hasta 2 armas y 50 pociones. Cada arma tiene un daño diferente.")
        print("Comienzas el juego con 3 vidas, 200 puntos, un arma y una pocion aleatorias.")
        self.askToPlayer("Presiona ENTER para volver al menú")

        if (self.input == ""): self.goToState("menu")


    def showStats(self):

        print("❤️ ", "Vidas:", self.lifes)
        print("⭐", "Puntos:", self.points)
        print("⚔️ ", "Partidas ganadas:", self.wonnedBattles)

        print("\n🗡️  Armas", f'({len(self.weapons)}/2):')
        for i in range(len(self.weapons)):
            weapon = self.weapons[i]
            print(f' [{i + 1}] {weapon.emoji} {weapon.name} (daño: {weapon.damage})')
        
        print("\n🧪 Pociones", f'({len(self.potions)}/50):')
        for i in range(len(self.potions)):
            potion = self.potions[i]
            print(f' [{i + 1}] {potion.name}')

        self.askToPlayer("Presiona ENTER para continuar")        
        if (self.input == ""): self.goToState("walk")


    def updateLifes(self, lifes):
        if (self.lifes + lifes > 0):
            if (lifes > 0): self.showMessage("Has ganado una vida")
            else: self.showMessage("Has perdido una vida")

            self.lifes += lifes

        else:
            self.showMessage("Te has quedado sin vidas, has perdido el juego")
            self.goToState("menu")


    def updatePoints(self, points):
        if (self.points + points > 0):
            if (points > 0): self.showMessage(f'Has ganado {points} puntos')
            else: self.showMessage(f'Has perdido {points * -1} puntos')

            self.points += points

        else: self.updateLifes(-1)


    def findPotion(self):
        potion = random.choice(potions)
        self.showMessage(f'Has encontrado una pocion: {potion.name}')
        self.askToPlayer("¿Quieres guardar la pocion? (s/N)")
        savePotion = self.input

        if (savePotion == "s"): self.savePotion(potion)
    

    def savePotion(self, potion):
        if (len(self.potions) < 50):
            self.showMessage(f'Guardando la pocion {potion.name}')
            self.potions.append(potion)
        else: self.showMessage("No puedes guardar más pociones")
    

    def usePotion(self, potion):
        self.showMessage(f'Usando la pocion "{potion.name}"')

        if (potion.name == "Fenix"): self.updateLifes(potion.value)
        elif (potion.name == "Poder"): self.updatePoints(potion.value)
        elif (potion.name == "Suerte de los dioses"): self.updatePoints(potion.value)
        elif (potion.name == "Oportunidad"): self.updatePoints(potion.value)
        
        self.showMessage(potion.message)
        self.potions.remove(potion)


    def saveWeapon(self, weapon):
        if (len(self.weapons) < 2): self.weapons.append(weapon)
        else:
            self.showMessage("Tienes 2 armas, debes elegir cuál quieres reemplazar")

            for i in range(len(self.weapons)):
                weapon = self.weapons[i]
                print(f' [{i + 1}] {weapon.emoji} {weapon.name} (daño: {weapon.damage})')

            self.showMessage("¿En qué posición quieres guardar la nueva arma?")
            self.askToPlayer("Elige 1, 2 o X para cancelar")
            newPosition = self.input

            if (newPosition == 1 or newPosition == 2):
                self.showMessage(f'Has guardado el arma {weapon.name}')
                self.weapons[newPosition - 1] = weapon
        
        self.showMessage("Ahora tienes las siguientes armas:")

        for i in range(len(self.weapons)):
            weapon = self.weapons[i]
            print(f' [{i + 1}] {weapon.emoji} {weapon.name} (daño: {weapon.damage})')


    def battle(self):
        enemyWeapon = random.choice(weapons)
        self.showMessage(f'El enemigo te ha atacado con el arma {enemyWeapon.name} {enemyWeapon.emoji}')

        if (len(self.weapons) == 2):
            self.askToPlayer("¿Qué arma quieres usar?")
            weaponPosition = self.input

            if (weaponPosition == 2): myWeapon = self.weapons[1]
            else: myWeapon = self.weapons[0]
        
        else: myWeapon = self.weapons[0]

        self.showMessage(f'Usando el arma {myWeapon.name} {myWeapon.emoji}')
        self.showMessage("Atacando...")

        win = myWeapon.damage >= enemyWeapon.damage

        if (win):
            self.showMessage("¡Has ganado esta batalla!")
            self.updatePoints(myWeapon.damage)
            self.wonnedBattles += 1
            gameSound.playWin()
 
            self.askToPlayer("¿Quieres guardar la arma? (s/n)")
            saveWeapon = self.input
            if (saveWeapon == "s"): self.saveWeapon(enemyWeapon)

        else:
            self.showMessage("¡Has perdido esta batalla!")
            self.updatePoints(-enemyWeapon.damage)
            gameSound.playLose()

        if (self.wonnedBattles == 10): self.finalBattle()
        else: self.beAttacked()


    def finalBattle(self):
        self.showMessage("Por fin has llegado al castillo de la montaña")
        self.showMessage("De repente una voz detrás tuyo te sobresalta:")
        self.showMessage("")
        self.showMessage("   Te he estado esperando, estaba seguro que llegarías hasta aquí")
        self.showMessage("   Ella te dio y te dijo lo necesario para volver a tu mundo")
        self.showMessage("   Pero por supuesto, nunca te dijo quién te esperaría aquí")
        self.showMessage("   Apuesto a que ni siquiera sabes quién es ella")
        self.showMessage("   Apuesto a que ni siquiera sabes quién eres")
        self.showMessage("   Pero no te preocupes, yo te lo diré, eso no importa")
        self.showMessage("   En este mundo glorioso para mí, no voy a permitir que ganes")
        self.showMessage("")
        self.showMessage("Tu enemigo saca su mejor arma y te ataca")

        if (len(self.weapons) == 2):
            self.askToPlayer("¿Qué arma quieres usar?")
            weaponPosition = self.input

            if (weaponPosition == 2): weapon = self.weapons[1]
            else: weapon = self.weapons[0]

        else: weapon = self.weapons[0]

        self.showMessage(f'Usando el arma {weapon.name}')
        self.showMessage("Atacando...")
        win = random.choice([True, False])

        if (win):
            self.showMessage("Has ganado el juego")
            gameSound.playWin()
            self.goToState("menu")
        else:
            self.showMessage("Has perdido el juego")
            gameSound.playGameOver()
            self.goToState("menu")