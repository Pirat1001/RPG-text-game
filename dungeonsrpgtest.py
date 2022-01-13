from math import e
import random
import sys
import time
from time import sleep
from typing import MutableMapping


enemy = ""
aDamage = 0
uDamage = 0
health = 0
mana = 0
damage = 0
char = ""
ryggsäck=[]
    
def start(): #backstory
    global health
    global aDamage
    global uDamage
    global mana
    global damage
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
         WEAPON: GAMMAL ROSTIG YXA
        ************************          
        """
        print(statistics)
        sleep(2)
        aDamage = 50
        uDamage = 100
        health = 200
        mana = 100
        damageC = 20
        damage == damage + damageC
        return mana, health, aDamage, damage, uDamage

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
         WEAPON: GAMMAL ROSTIG SVÄRD
        ************************          
        """
        print(statistics)
        sleep(2)
        aDamage = 50
        uDamage = 100
        health = 150
        mana = 100
        damageC = 40
        damage = damage + damageC
        return mana, health, damage, aDamage, uDamage

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
         WEAPON: TRÄPINNE
        ************************          
        """
        print(statistics)
        sleep(2)
        aDamage = 80
        uDamage = 1000
        health = 100
        mana = 200
        damageC = 30
        damage = damage + damageC
        return mana, health, damage, aDamage, uDamage

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
         WEAPON: GAMMAL PILBÅGE
        ************************          
        """
        print(statistics)
        sleep(2)
        aDamage = 60
        uDamage = 120
        health = 100
        mana = 200
        damageC = 45
        damage = damage + damageC
        return mana, health, damage, aDamage, uDamage
    
    else:
        print("Du måste välja en utav klasserna!")

def guldrum(): #själva guldrummet
    print("du är nu i guldrummet..")
    sleep(1)
    print("rummet är upplyst och du ser en guldkista mitt i rummet..")
    sleep(1)
    print("du känner dig säker när du går in..")
    sleep(1)
    print("rummet är mycket dammigt och det ser ut som om rummet har varit övergivet väldigt länge..")
    sleep(1)
    print("vill du gå fram till guldkistan?('ja' eller 'nej')")
    guldkista=input(">")
    guldkista=guldkista.lower()
    print(guldkista)
    if guldkista == "ja":
        print("du står nu framför guldkistan.") 
        sleep(1)
        print("vill du öppna guldkistan?")
        öppnakista=input(">")
        öppnakista=öppnakista.lower()
        print(öppnakista)
        if öppnakista == "ja":
            print("i kistan så ligger det några guldmynt och en bok med konstiga symboler på")
            sleep(1)
            print("vill du ta upp boken och guldmynten?")
            kistaitems=input(">")
            kistaitems=kistaitems.lower()
            print(kistaitems)
            if kistaitems == "ja":
                global ryggsäck
                global damage
                print("du tar upp den konstiga boken och 200 guldmynt..")
                sleep(1)
                print("Du bläddrar igenom boken fort..")
                sleep(1)
                print("Plötsligt börjar symbolerna på boken att glänsa och du känner dig starkare...")
                sleep(1)
                print("*Boken du hittat är en rune-bok som gör dig starkare!*")
                sleep(1)
                print("*Genom att ta upp rune-böcker under speletsgång kommer du att göra mer skada med dina vanliga attack*")
                ryggsäck.append("200 guldmynt")
                gåut=input(">")
                gåut=gåut.lower()
                print(gåut)
                print("vill du gå ut ur rummet?")
                if gåut == "ja":
                    guldkorridor()
                if gåut == "nej":
                    print("du står kvar och stirrar på en stängd guldkista..")
                    sleep(1)
                    print("Plötsligt ser du kistan röra på sig...")
                    sleep(1)
                    print("Det är en levande kista!")
                    sleep(1)
                    print("Du genast springer ut ur guldrummet och hör att kistan springer efter dig!")
                    sleep(1)
                    print("Du flyr tillbaks där du började och kan inte längre gå in i guldkorridoren..")
                    sleep(1)
                    print("Nu kan du antingen gå genom trädörren('gå framåt') eller genom dörren med dödsskallen ovan('gå vänster')")
                    dörr = input(">")
                    dörr=dörr.lower()
                    print(dörr)
                    if dörr == "gå framåt":
                        lootrum()
                    elif dörr == "gå vänster":
                        bosskoridor()
                    else:
                        print("Det finns inga andra vägar..")
                        print(dörr)
                damage=damage + 10
                return damage
            elif kistaitems == "nej":
                print("du låter föremålen ligga kvar.")
                sleep(1)
                print("Det verkar inte finnas något annat intressant i rummet, du borde gå ut och testa en annan dörr")
                ut=input(">")
                ut=ut.lower()
                print(ut)
                if ut == "gå ut":
                    förstarummet()
                else:
                    print("Du kan gå ut genom att skriva in 'gå ut'")
                    print(ut)
        if öppnakista == "nej":
            print("du känner att guldkistan kan vara farlig men du känner dig fortfarande säker i rummet..")
            sleep(1)
            print("Det verkar inte finnas något mer intressant i rummet, du borde gå ut och testa en annan dörr")
            goOut=input(">")
            goOut=goOut.lower()
            print(goOut)
            if goOut == "gå ut":
                förstarummet()
            else:
                print("Du kan gå ut genom att skriva in 'gå ut'")
                print(ut)
    if guldkista == "nej":
        print("du känner att guldkistan kan vara farlig men du känner dig fortfarande säker i rummet..")
        print("vill du gå ut ur rummet?")
        gåut=input(">")
        gåut=gåut.lower()
        print(gåut)
        if gåut == "ja":
            guldkorridor()
        if gåut == "nej":
            print("du står kvar och stirrar på en stängd guldkista..")
            sleep(1)
            print("Plötsligt ser du kistan röra på sig...")
            sleep(1)
            print("Det är en levande kista!")
            sleep(1)
            print("Du genast springer ut ur guldrummet och hör att kistan springer efter dig!")
            sleep(1)
            print("Du flyr tillbaks där du började och kan inte längre gå in i guldkorridoren..")
            sleep(1)
            print("Nu kan du antingen gå genom trädörren('gå framåt') eller genom dörren med dödsskallen ovan('gå vänster')")
            dörr = input(">")
            dörr=dörr.lower()
            print(dörr)
            if dörr == "gå framåt":
                lootrum()
            elif dörr == "gå vänster":
                bosskoridor()
            else:
                print("Det finns inga andra vägar..")
                print(dörr)

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

def guldkorridor(): #rum innan guldrumS
    global ryggsäck
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
    if gåiniguldrum == "search":
        print("Du letar igenom den guldiga korridoren...\n")
        sleep(1)
        print("Du hittar en mana elixir!\n")
        ryggsäck.append("Manaelixir")
        sleep(1)
        print("**Mana elixir kan du använda som livselixir, under fightens gång**\n")
        sleep(1)
        print("**Till skillnad från livselixiren, du använder manaelixir genom 'mana' och den återger dig 50 mana")
        sleep(1)
        print("Det verkar inte finnas något mer att göra i korridoren..")
        sleep(1)
        print("Vad vill du göra? 'gå framåt'(genom guldiga dörren) och 'gå bakåt'(tillbaks till gråttöppningen)")
        sleep(1)
        print(gåiniguldrum)
        if gåiniguldrum == "gå framåt":
            guldrum()
        elif gåiniguldrum == "gå bakåt":
            förstarummet()
        else:
            print("Du måste ju välja en av alternativen\n \n'gå framåt' \neller\n'gå bakåt'")


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
    

# själva starten av spelet:
def grottöppning(): 
    print("du står nu i grottöppningen, det är kvavt och du ser inte så mycket..")
    sleep(1)
    print("du går lite längre in och ser ljus, när du kollar närmare ser du 3 dörrar..")
    sleep(1)
    print("en dörr rakt framför dig, en träddörr(*fight-tutorial*), till vänster har ser du en gulddörr och till höger om dig har du en dörr med en dödskalle hängandes över..")
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

def förstarummet():
    print("Du befinner dig nu i första rummet, 'gråttöppningen'")
    sleep(1)
    print("Du kan antingen gå åt höger, genom dörren med dödsskallen ovan \n \n eller till vänster genom gulddörren")
    choice = input(">")
    choice = choice.lower()
    print(choice)
    if choice == "gå vänster":
        guldkorridor()
    elif choice == "gå höger":
        bosskoridor()

#trädörren
def lootrum(): 
    global ryggsäck
    print("Du går in genom den öppna trä dörren")
    sleep(1)
    print("Plötsligt stängs dörren bakom dig och du ser en levande skelett springa mot dig \n")
    sleep(1)
    def fightS():
        global health
        global damage
        global uDamage
        global aDamage
        global mana
        eHealth = 200
        tutorial()
        sleep(2)
        while eHealth > 0:
            if health <= 0:
                print("Du har dött, men ge inte upp!")
                sleep(1)
                print("STARTA OM FIGHTEN")
                fightS()
            if health > 0:
                action = input(f"Du står framför skeletten, döda den!\n \n")
                action=action.lower()
                if action == "attack":
                    eHealth=eHealth - damage
                    if eHealth <= 0:
                        print("skeletten överlevde inte din autoattack!")
                    else:
                        eAttTxt = random.choice(["Dess ben delar flyger omkring i rummet!\n \n", "Skeletten skriker vilt!\n \n", "Skeletten kunde inte försvara sig!\n \n"])
                        print(eAttTxt)
                        print(f"Du attackerade skeletten, den har {eHealth}hp kvar!\n \n")
                        print(f"Skeletten slår tillbaks! Du har {health}hp kvar!")
                        health=health - random.randint(3,6)
                if action == "a" and mana >= 50:
                    if mana < 50:
                        print("Du har inte tillräckligt med mana")
                    eHealth = eHealth - aDamage
                    if eHealth <= 0:
                        print("skeletten överlevde inte din kraftfulla ability!")
                        return mana
                    else:
                        mana = mana - 50
                        eAbTxt = random.choice(["\n \nSkeletten flyger bort mot väggen efter att den har tagit emot din kraftfulla ability!", "Skeletten skriker av ondska då du träffar den med din ability!"])
                        print(eAbTxt)
                        print(f"Du attackerade skeletten med din kraftfulla ability! \n \n den har {eHealth}hp kvar!\n")
                        print(f"Skeletten tar sig upp och attackerar tillbaka! Du har {health}hp kvar!")
                        health=health - random.randint(3,6)
                        return mana
                elif action == "u" and mana >= 100:
                    if mana < 100:
                        print("Du ha inte tillräckligt mana!")
                    eHealth = eHealth - uDamage
                    health=health - random.randint(1,4)
                    mana = mana - 100
                    eAbTxt = random.choice(["\n \nSkeletten flyger bort mot väggen efter att den har tagit emot din kraftfulla ability!", "Skeletten skriker av ondska då du träffar den med din ability!"])
                    print(eAbTxt)
                    if eHealth > 0:
                        print(f"\nSkeletten blir träffad med din ultimate ability! Den tar enorm skada, den har {eHealth}hp kvar!")
                        print("\n \n Skeletten kunde inte ta sig upp i tid för att attackera dig tillbaka, du förlorar ingen hp!")
                        return mana
                    else:
                        print("Skeletten klarade inte av din kraftfulla ability! \n")
                        return mana



    fightS()
    print("**Du har nu dödat din första fiende!** \n")
    sleep(1)
    print("**Du kommer genom spelets gång behöva döda många fler för att gå vidare...**")
    sleep(1)
    print(f"Du har {mana} kvar efter fighten")
    sleep(1)
    print("**Kom ihåg att använda dina abilities och kontrollera din health, lycka till!**\n")
    sleep(1)
    print("Efter att du har dödat skeletten, har dörrarna öppnats")
    sleep(1)
    print("Du ser dig omkring i rummet efter att ha lugnat ned sig..")
    sleep(1)
    print("Du ser inget märkligt förutom några gamla dammiga hyllor, kanske vore det smart att leta igenom dem?..")
    sleep(1)
    leta = input("Vad vill du göra \n \n du kan gå tillbaka till första rummen och testa ett annat dörr genom att skriva 'gå bakåt' \n \n eller leta igenom rummet genom att skriva 'search'")
    leta = leta.lower()
    print(leta)
    if leta == "gå bakåt":
        sleep(2)
        förstarummet()
    if leta == "search":
        ryggsäck.append("Livselixir")
        print("Du söker igenom alla dammiga hyllor och du hittar en livselixir! \n \n *Livs elixir kan du använda under fightens gång genom att skriva 'hp' då du märker att ditt hp är lågt* \n \n")
        sleep(2)
        print("Nu har du letat igenom rummet och det verkar inte finnas något mer du kan göra, gå tillbaka till grottöppningen och välj ett annat dörr!")
        val=input(">")
        val=val.lower()
        if val == "gå bakåt" or "gå tillbaka":
            förstarummet()
        else:
            print("Det finns inget kvar att göra i rummet")
            print(val)
    else:
        print("Det verkar inte finnas något annat du kan göra i rummet, välj en av alternativen!")
        print(leta)


def tutorial():
    print("                                *****Fight tutorial*****\n")
    sleep(2)
    print("                Kom ihåg att använda dina abilities under spelets gång! \n")
    sleep(2)
    print("För att använda de behöver du kontrollera din mana, du kan göra det genom att skriva mana i terminalen \n")
    sleep(2)
    print("Fienden kommer alltid att attackera efter dig, alltså är det möjligt att gå ut ur fighten utan skada \n")
    sleep(2)
    print("      Du måste även kontrollera ditt hp, det kommer att skrivas ut efter varje fiendes attack \n") 
    sleep(2)
    print("Du kan inte använda några föremål under fightens gång, alltså kan du inte använda exempelvis livselixir \n")
    sleep(2)
    print("Du måste tänka strategiskt, dina abilities är värdefulla och väldigt dyra, du måste tänka efter dina steg \n")
    sleep(2)
    print("     Du kan använda dina abilities genom att under fightens gång skriva a och ultimate genom 'u' \n")

start()
grottöppning()
