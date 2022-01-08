from math import e
import random
import sys
import time
from time import sleep
from typing import MutableMapping


global health
global mana
global weapon
global damage
global ability
global ultimate
global aDamage
eHealth = 0
aDamage = 0
ability = ""
ultimate= ""
damage = 0
health = 0
mana = 0
weapon = ""
char = ""
ryggsäck=[]
    
def start(): #backstory
    print("Du slogs mot en stor drake men började förlora..")
    sleep(1)
    print("Du försöker fly så fort som möjligt och hittar en grotta..")
    sleep(1)
    print("Du tar dig in i grottan där du är säker men kan inte ta dig ut för där vaktar draken..")
    sleep(1)
    print("vilken klass vill du välja.. Det finns 4 klasser att välja på:tank, krigare, magiker och jägare.")
    
    character=input(">")
    character=character.lower()

    if character == "tank":
        print("du har valt klassen tank.")
        char == "tank"
        sleep(1)
        statistics = """         
                  TANK
        ************************
         HP: 200
         AD: 20 
         MANA: 100
         ABILITY: AXETHROW 
         ULTIMATE: AXEFURY
        ************************          
        """
        print(statistics)
        sleep(3)
        grottöppning()
        ability = "AXETHROW"
        ultimate = "AXEFURY"
        health = 200
        mana = 100
        weapon = "Gammal rostig yxa"
        return mana, weapon, health, ability, ultimate

    if character == "krigare":
        print("du har valt klassen krigare.")
        char == "krigare"
        sleep(1)
        statistics = """         
                 KRIGARE
        ************************
         HP: 150
         AD: 35
         MANA: 100
         ABILITY: SWORDSPIN
         ULTIMATE: FATE SEALED
        ************************          
        """
        print(statistics)
        sleep(1)
        grottöppning()
        ability = "SWORDSPIN"
        ultimate = "FATE SEALED"
        health = 150
        mana = 100
        weapon = "Gammal rostig svärd"
        return mana, health, weapon, ability, ultimate

    if character == "magiker":
        print("du har valt klassen magiker.")
        char == "magiker"
        sleep(1)
        statistics = """         
                MAGIKER
        ************************
         HP: 100
         AD: 20 
         MANA: 200
         ABILITY: FIREBALL
         ULTIMATE: PRIMORDIAL BUSRT
        ************************          
        """
        print(statistics)
        sleep(1)
        grottöppning()
        ability = "FIREBALL"
        ultimate = "PRIMORDIAL BURST"
        health = 100
        mana = 200
        weapon = "Träpinne"
        return mana, health, weapon, ability, ultimate

    if character == "jägare":
        print("du har valt klassen jägare.")
        char == "jägare"
        sleep(1)
        statistics = """         
                 JÄGARE
        ************************
         HP: 100
         AD: 50
         MANA: 200
         ABILITY: QUICKSHOT
         ULTIMATE: CROSSBOW
        ************************          
        """
        print(statistics)
        sleep(1)
        grottöppning()
        ability = "QUICKSHOT"
        ultimate = "CROSSBOW"
        health = 100
        mana = 200
        weapon = "Gammal pilbåge"
    
    else:
        print("Du måste välja en utav klasserna!")



# själva starten av spelet:
def grottöppning(): 
    print("du står nu i grottöppningen, det är kvavt och du ser inte så mycket..")
    sleep(1)
    print("du går lite längre in och ser ljus, när du kollar närmare ser du 3 dörrar..")
    sleep(1)
    print("en dörr rakt framför dig, en träddörr, till vänster har ser du en gulddörr och till höger om dig har du en dörr med en dödskalle hängandes över..")
    sleep(1)
    print("du blir väldigt försiktig med tanke på att det kan bo fler monster här eller något annat mystiskt, men du behöver ta dig ut..")
    sleep(1)
    print("hur gör du? vilken dörr väljer du?")
    sleep(1)
    print("vänster höger eller rakt fram.")
    sleep(1)
    print("(För att gå vänster skriv \"gå vänster\")")
    
    förstadörr=input(">")
    förstadörr=förstadörr.lower()
    
    if förstadörr == "gå vänster":
        print("du står nu och kikar in i gulddörren, du ser ett tomt rum och en till gulddörr framför dig..")
        sleep(1)
        print("du går in och kikar in i nästa rum..")
        sleep(1)
        guldkorridor()
    
    if förstadörr == "gå höger":
        bosskoridor()

    
    if förstadörr == "gå framåt":
        lootrum()

#trädörren
def lootrum(): 
    print("Du går in genom den öppna trä dörren")
    sleep(1)
    print("Plötsligt stängs dörren bakom dig och du ser tre levande skeletter springa mot dig")
    sleep(1)
    print("Du måste döda dem!")
    sleep(1)
    global ability
    fight("skelett", ability)
    
#rummet innan bossrum med kartan
def bosskoridor(): 
    print("du har nu gått igenom dörren med en dödskalle över sig..")
    sleep(1)
    print("du ser massor av skelett delar överallt från döda personer..")
    sleep(1)
    print("du blir genast försiktig och kollar runt för att se om det finns någon fiende i rummet..")
    sleep(1)
    print("du ser bara massa bokhyllor med blod på från de döda och en stor port längre in i rummet..")
    sleep(1)
    print("bakom en död kropp vid en bokhylla så ser det ut att ligga en karta av något slag..")
    sleep(1)
    print("när du kollar närmare på den stora svarta porten så ser du tydliga mönster av drakar och andra monster och andra saker som du inte kan identifiera..")
    sleep(1)
    print("du misstänker att bakom den dörren finns något riktigt farligt..")
    sleep(1)
    print("vågar du gå igenom den stora porten?")

    bossdörr=input(">")
    bossdörr=bossdörr.lower()

    if bossdörr == "ja":
        bossrum()
    if bossdörr == "nej":
        print("du står kvar i korridoren, vill du inte göra något annat?")

    gåtillgrottöppning=input(">")
    gåtillgrottöppning=gåtillgrottöppning.lower()
    
    if gåtillgrottöppning == "ja":
            grottöppning()
    if gåtillgrottöppning == "nej":
        bosskoridor()

def bossrum():   #bossrummet
    target = "SKELETON KING"
    print("du har nu öppnat den stora tunga porten..")
    sleep(1)
    print("du ser dig omkring, det är en stor sal med bord och stolar lite överallt, dammigt och en stor tron längst in i rummet..")
    sleep(1)
    print("Du ser inte om någon sitter på tronen eftersom att det är så mörkt längre in. det lyser knappt där du står redan..")
    sleep(1)
    print("du ser återigen skelett delar som ligger på stolar och bord. Du märker även att inget av möblerna är trasiga..")
    sleep(1)
    print("kan det vara en magiker som gjort detta?")

def guldrum(): #själv guldrummet
    print("du är nu i guldrummet..")
    sleep(1)
    print("rummet är upplyst och du ser en guldkista mitt i rummet..")
    sleep(1)
    print("du känner dig säker när du går in..")
    sleep(1)
    print("rummet är mycket dammigt och det ser ut som om rummet har varit övergivet väldigt länge..")
    sleep(1)
    print("vill du gå fram till guldkistan?")
        
def guldkorridor(): #rum innan guldrumS
    print("du står nu i vad som ser ut och vara en guldig korridor..")
    sleep(1)
    print("när du ser dig omkring så ser du massa bokhyllor fullt med böcker och rummet är även dammigt..")
    sleep(1)
    print("rummet är även någorlunda upplyst..")
    sleep(1)
    print("längre in i rummet ser du en till guldig dörr..")
    sleep(1)
    print("bakom dig har du dörren du kom ifrån..")
    sleep(1)
    print("vill du gå igenom dörren framför dig?")

    gåiniguldrum=input(">")
    gåiniguldrum=gåiniguldrum.lower()

    if gåiniguldrum =="ja":
        guldrum()
    if gåiniguldrum == "nej":
        print("du står kvar i guldkorridoren, säker på att du inte vil göra något?")
        sleep(1)
        print("vill du gå tillbaka till grottöppningen?")
        gåtillgrottöppning=input(">")
        gåtillgrottöppning=gåtillgrottöppning.lower()
        if gåtillgrottöppning == "ja":
            grottöppning()
        if gåtillgrottöppning == "nej":
            print("du står nu kvar i guldkorridoren..")

    guldkista=input(">")
    guldkista=guldkista.lower()

    if guldkista == "ja":
        print("du står nu framför guldkistan.") 
        sleep(1)
        print("vill du öppna guldkistan?")
        öppnakista=input(">")
        öppnakista=öppnakista.lower()

        if guldkista == "nej":
            print("du känner att guldkistan kan vara farlig men du känner dig fortfarande säker i rummet..")

        if öppnakista == "ja":
            print("i kistan så ligger det några guldmynt och ett vapen.")
            sleep(1)
            print("vill du ta upp vapnet och guldmynten?")
            kistaitems=input(">")
            kistaitems=kistaitems.lower()
            if kistaitems == "ja":
                print("du tar upp svärdet och mynten..")
                ryggsäck.append("svärd")
                ryggsäck.append("guldmynt")
                
            if kistaitems == "nej":
                print("du låter föremålen ligga kvar.")

        if öppnakista == "nej":
            print("du känner att guldkistan k4an vara farlig men du känner dig fortfarande säker i rummet..")
    
    print("vill du gå ut ur rummet?")

    gåut=input(">")
    gåut=gåut.lower()

    if gåut == "ja":
        guldkorridor()
    if gåut == "nej":
        print("du står kvar och stirrar på en stängd guldkista..")
        sleep(1)
        print("säker på att du inte vill gå ut ur rummet?")

def fight(enemy, ability):

    def tutorial():
        print("""
                                                *****Fight tutorial*****
        
                                Kom ihåg att använda dina abilities under spelets gång!

            För att använda de behöver du kontrollera din mana, du kan göra det genom att skriva mana i terminalen

             Fienden kommer alltid att attackera efter dig, alltså är det möjligt att gå ut ur fighten utan skada

                  Du måste även kontrollera ditt hp, det kommer att skrivas ut efter varje fiendes attack 

             Du kan inte använda några föremål under fightens gång, alltså kan du inte använda exempelvis livselixir 

             Du måste tänka strategiskt, dina abilities är värdefulla och väldigt dyra, du måste tänka efter dina steg

                    Du kan använda dina abilities genom att under fightensgång skriva a och ultimate gennom u
             """)
        
    
    def enemies(enemy):
        if enemy == "skelett":
            global eHealth
            ehealth = 200
            enemy = True
            if eHealth <= 0:
                enemy == False
            return ehealth, enemy
            
    
    def eAttack(enemy, health):
        if enemy == "skelett":
            enemytxt = random.choice(["Skeletten drar upp sitt svärd!", "Den skrattar i ditt ansikte!", "Skeletten attackerar lågt!"])
            print(enemytxt)
            health = health - (random.randint(1,4)) 
            return health   # mozna zmienic na return health - random.randint(1,4)
    
    def attPower(weapon, ability, ultimate, damage, aDamage):
        if weapon == "Gammal rostig yxa":
            damage = random.randint(20,30)
        elif weapon == "Gammal rostig svärd":
            damage = random.randint(35,50)
        elif weapon =="Träpinne":
            damage = random.randint(20,40)
        elif weapon == "Gammal pilbåge":
            damage = random.randint(40,50)
        elif ability == "AXETHROW":
            aDamage = 50
        elif ultimate == "AXEFURY":
            aDamage = 100
        elif ability == "SWORDSPIN":
            aDamage = 80
        elif ultimate == "FATE SEALED":
            aDamage = 150
        elif ability == "FIREBALL":
            aDamage = 70
        elif ultimate == "PRIMORDIAL BURST":
            aDamage = 1000
        elif ability == "QUICKSHOT":
            aDamage = 60
        elif ultimate == "CROSSBOW":
            aDamage = 80

        return damage, aDamage

    def attack(enemy, health, eHealth):
        attPower(weapon)
        eHealth -= damage
        print("Du attackerade skeletten med din autoattack \n \n den har {}hp kvar".format(eHealth))
        if eHealth > 0:
            if enemy == "skelett":
                eAttTxt = random.choice(["Dess ben delar flyger omkring i rummet!", "Skeletten skriker vilt!", "Skeletten kunde inte försvara sig!"])
                print(eAttTxt)
        return eHealth        
    
    def abilities(ability, ultimate, health, eHealth):
        def axeThrow(eHealth):
            attPower(ability)
            eHealth -= aDamage
            print("Du kastar din yxa på fienden, han har {}hp kvar!".format(eHealth))
            return eHealth
        def axeFury(eHealth):
            attPower(ultimate)
            eHealth -= aDamage
            print("Du använder din speciella attack AXEFURY \n \n fienden har {}hp kvar!".format(eHealth))
            return eHealth
        def swordSpin(eHealth):
            attPower(ability)
            eHealth -= aDamage
            print("Du snurrar runt med din svärd i handen \n \n fienden har {}hp kvar!".format(eHealth))
            return eHealth
        def fateSealed(eHealth):
            attPower(ultimate)
            eHealth -= aDamage
            print("Du skär genom fienden med ditt svärd \n \n han har {}hp kvar!".format(eHealth))
            return eHealth
        def fireBall(eHealth):
            attPower(ability)
            eHealth -= aDamage
            print("Du kastar en eldkula på fienden! \n \n han har {}hp kvar!".format(eHealth))
            return eHealth
        def primordialBurst(eHealth):
            attPower(ultimate)
            eHealth -= aDamage
            print("Du kastar en svarthål på fienden \n \n han har dött!")
            return eHealth
        def quickShot(eHealth):
            attPower(ability)
            eHealth -= aDamage
            print("Du skjuter tre pilar riktigt fort! \n \n din fiende har {}hp kvar!".format(eHealth))
            return eHealth
        def crossBow(eHealth):
            attPower(ultimate)
            eHealth -= aDamage
            print("Du tar fram din armborst och skjuter nu mycket kraftigare och fortare! \n \n din fiende har {}hp kvar!".format(eHealth))
            return eHealth

    def maxhealth(health):
        if health > 20:
            health = 20
            return health 
    def maxmana(mana):
        if mana > 200:
            mana = 200
            return mana
    def backpack(health, mana):
        def bröd():
            print("Bröd ger dig 20hp")
            health + 20
        def livelixir():
            print("Livselixir ger dig 100 hp")
            health + 100
        def manaelixir():
            print("Manaelixir ger dig 100 mana")
            mana + 100

    def fightskelett(enemy, ability, ultimate, mana):
        action = str(input("Du står framför skeletten, vad vill du göra?"))
        if action == "attack":
            if ability == "AXETHROW":
                attack("skelett", 200, eHealth)
            elif ability == "SWORDSPIN":
                attack("skelett", 150, eHealth)
            elif ability == "FIREBALL":
                attack("skelett", 100, eHealth)
            elif ability == "QUICKSHOT":
                attack("skelett", 100, eHealth)
        elif action == "a":
            if mana >= 50:
                attPower(ability)
        elif action == "u":
            if mana >= 100:
                attPower(ultimate)
        while enemy == True:
            print(action)
        if enemy == False:
            print("Du har dödat skeletten!")
            pass

    tutorial()
    enemies("skelett")
    print("Du måste döda skeletten för att ta dig ur rummet!")
    if ability == "AXETHROW":
        fightskelett("skelett", "AXETHROW", "AXEFURT", 100)
    elif ability == "SWORDSPIN":
        fightskelett("skelett", "SWORDSPIN", "FATE SEALED", 100)
    elif ability == "FIREBALL":
        fightskelett("skelett", "FIREBALL", "PRIMORDIAL BURST", 200)
    elif ability == "QUICKSHOT":
        fightskelett("skelett", "QUICKSHOT", "CROSSBOW", 200)

start() 
