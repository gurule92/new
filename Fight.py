#!/usr/bin/env python3                                                                                         
import subprocess as sp
import time
import sys
import random                                                                                                  
useditem= ''
attack =''
inventory =[]
last = ''
name = input("What is your name? ").upper()
most = int(input("How many enemies are you brave enough to face?\nNote: There is a boss on every 5th level. "))
count = 1
hitpoints = 100                                                                                                
critterlist = ["Mouse","Dragon","Zombie"]                                                                      
critterdict = {"Mouse":25,"Dragon":125,"Zombie":90,"Chuck Norris":200}                                                           
Mouse = {"Scratch":random.randint(3,5),"Bite":random.randint(4,8),"Junta Virus":random.randint(8,15)}                               
Dragon = {"Flame Thrower":random.randint(8,12),"Tail Whip":random.randint(6,8),"Chomp":random.randint(7,9),"Yawn":0,"Sigh":0} 
Zombie = {"Bite":random.randint(6,8),"Brain Chomp":random.randint(7,10),"Scratch":random.randint(3,5)}                                  
Norris = {"Roundhouse Kick to the Face":random.randint(10,20),"Smolder":random.randint(9,15),"Hat Tilt":0,"Thunderpunch":random.randint(7,10)}
print("\nWelcome %s. You have entered a treacherous forest with many weak-ass enemies that are no match for your smoldering stare.\nYou could face Mice, Zombies or even Dragons!" % name)                                                                                   
time.sleep(0.3)
def penemy(bg):
    if bg == 'Mouse':
        global critterhitpoints
        print('                     __') 
        time.sleep(0.032)
        print('                  __/  \\')
        time.sleep(0.032)
        print('                 /  \-./')
        time.sleep(0.032)
        print('                 \_   66\_')
        time.sleep(0.032)
        print('                   \  ____)o')
        time.sleep(0.032)
        print('                    ) (')
        time.sleep(0.032)
        print('           .-.     /   \\___')
        time.sleep(0.032)
        print('        (_/   \   / /   |___)')
        time.sleep(0.032)
        print('               |  \ \   /')
        time.sleep(0.032)
        print('                \  \_) (')
        time.sleep(0.032)
        print('                 \'-\'/ \ \  _')
        time.sleep(0.032)
        print('                   / / \ \/ )')
        time.sleep(0.032)
        print('                  (  \  \  /')   
        time.sleep(0.032)
        print('           jgs     \__)  "`')
        time.sleep(0.25)
    if bg == 'Dragon':
        print('                   __        _      ')
        time.sleep(0.0312)
        print('                 _/  \    _(\(o     ')
        time.sleep(0.0312)
        print('                /     \  /  _  ^^^o ')
        time.sleep(0.0312)
        print('               /   !   \/  ! |!!!v')
        time.sleep(0.0312)
        print('              !  !  \ _| ( \____    ')
        time.sleep(0.0312)
        print('              ! . \ _!\   \===^\)   ')
        time.sleep(0.0312)
        print('Art by         \ \_!  / __!         ')
        time.sleep(0.0312)
        print(' Gunnar Z.      \!   /    \         ')
        time.sleep(0.0312)
        print('          (\_      _/   _\ )        ')
        time.sleep(0.0312)
        print('           \ ^^--^^ __-^ /(__       ')
        time.sleep(0.0312)
        print('            ^^----^^    "^--v|')
        time.sleep(0.0312)
    if bg == 'Zombie':
        print('NUGGGGGH..... BRAAAAINSSSS.....              ')
        time.sleep(0.0312)
        print('                                     \  .....  ')
        time.sleep(0.0312)
        print('                                       C C  /  ')
        time.sleep(0.0312)
        print('                                      /<   /   ')
        time.sleep(0.0312)        
        print('                       ___ __________/_#__=o ')
        time.sleep(0.0312)
        print('                      /(- /(\_\________   \  ')
        time.sleep(0.0312)
        print('                      \ ) \ )_      \o     \  ')
        time.sleep(0.0312)
        print('                      /|\ /|\       |\'    |   ')
        time.sleep(0.0312)
        print('                                    |     _| ')
        time.sleep(0.0312)
        print('                                    /o   __\ ')
        time.sleep(0.0312)
        print('                                   / \'    |')
        time.sleep(0.0312)
        print('                                  / /      | ')
        time.sleep(0.0312)
        print('                                 /_/\______| ')
        time.sleep(0.0312)
        print('                                (   _(    <  ')
        time.sleep(0.0312)
        print('                                 \    \    \ ')
        time.sleep(0.0312)
        print('                                  \    \    | ')
        time.sleep(0.0312)
        print('                                   \____\____\ ')
        time.sleep(0.0312)
        print('                                   ____\_\__\_\ ')
        time.sleep(0.0312)
        print('                                 /`   /`     o\ ')
        time.sleep(0.0312)
        print('                                 |___ |_______|.. . b\'ger')
        time.sleep(0.22)
    if bg =='Norris':
        pnorris()
def useitem(choice):
    useditem = choice 
    global attack
    global hitpoints
    global critterhitpoints
    global inventory
    if useditem == 'T':
        useditem = 'Po(T)ion'
    elif useditem == 'B':
        useditem = '(B)omb'
    elif useditem == 'C':
        useditem = '(C)ocaine'
    while useditem not in inventory:
        useditem = input('So you want to use an item I see..... but you dont have any of those!!!!\nHere is you current inventory... Choose one of theses: %s \nIf you want to use an attack type atk ' % inventory).upper()
        if useditem == 'ATK':
            useditem = ''
            break
        if useditem == 'T':
            useditem = 'Po(T)ion'
        elif useditem == 'B':
            useditem = '(B)omb'
        elif useditem == 'C':
            useditem = '(C)ocaine'
    if critterhitpoints > 0:
        tmp = sp.call('clear',shell=True)
        if useditem == 'Po(T)ion':
            tmp = sp.call('clear',shell=True)
            hitpoints += 40
            print('Your HP went up by 40 points! It is now %s.\n' % hitpoints)
            print('                     ____\n                    |    |\n                    |    |\n                    |____|\n                    |    |\n                    (    )\n                    )    (\n                  .`      `.\n                 /          \ \n                |------------|\n                |JACK DANIELS|\n                |    ----    |\n                |   (No.7)   |\n                |    ----    |\n                | Tennessee  |\n                |  WHISKEY   |\n                |  40% Vol.  |\n                |------------|\n                |____________|dp')
        elif useditem == '(B)omb':
            tmp = sp.call('clear',shell=True)
            critterhitpoints -= 50
            penemy(enemy)
            print('          _ ._  _ , _ ._')
            time.sleep(0.12)
            print('        (_ \' ( `  )_  .__)')
            time.sleep(0.12)
            print('      ( (  (    )   `)  ) _)')
            time.sleep(0.12)
            print('     (__ (_   (_ . _) _) ,__)')
            time.sleep(0.12)
            print('         `~~`\ ` . /`~~`')
            time.sleep(0.12)
            print('              ;   ;')
            time.sleep(0.12)
            print('              /   \ ')
            time.sleep(0.12)
            print('_____________/_ __ \_____________')
            time.sleep(0.2)
            print('You hit the %s for 50 HP' % enemy)
        elif useditem == '(C)ocaine':
            critterhitpoints -=15
            print('           /`-._      _, ')
            print('          /      `-._(  \ ')
            print('         /           \\  \ ')
            print('        /             \\  \`- ')
            print('       /           .   \\  \    `-._')
            print('      /           :).   \\  \        `-. ')
            print('     /           ./;.    \\  \         / ')
            print('    /           .;        \\  \       / ')
            print('   /   .        .          \\  \     / ')
            print('  /  .; ):.   __________    \\  \   / ')
            print(' /   . :"    |~~_~__ _  |    \\(_) / ')
            print('/            ) (_=__=_) (     \(.`/ ')
            print('`-._         |-_________|        / ')
            print('     `-._                       / ')
            print('          `-._                 / ')
            print('               `-._           / ')
            print('                    `-._     / ')
            print('                         `-./ ')
            print('You gave cocaine to the %s causing it to overdose and lose 15hp.' % enemy)
        if useditem !='':
            inventory.pop(inventory.index(useditem))
            useditem =''
        attack = 0

def atk():
    global attack
    global inventory
    global critterhitpoints
    if len(inventory)==0:
        while attack != 'P' and attack != 'R' and attack != 'S':
            attack = input("\nYour HP:%s \nEnemy HP:%s\nPlease choose an attack ((P)unch [7-10], (R)oundhouse Kick[8-20], (S)moldering Stare[0-15])! \nUse the First letter of the attack " %(hitpoints, critterhitpoints)).upper()
            
    else:
        attack = input('\nYour HP:%s \nEnemy HP:%s\nPlease choose a move ((P)unch [7-10], (R)oundhouse Kick[8-20], (S)moldering Stare[0-15])!\nYou can also use an Item if you want... \nCurrent inventory: %s '%(hitpoints, critterhitpoints, inventory)).upper()
        if attack == 'B' or attack == 'C' or attack == 'T':
            useitem(attack)
            if critterhitpoints > 0:
                atk()
    return attack 
while count <= most:
    if hitpoints <= 0:
        break 
    else:
        enemy = critterlist[random.randint(0,2)]                                        
        critterhitpoints = critterdict[enemy]                                                                   
        if name == 'CHUCK NORRIS': 
            print('I am sorry Mr. Norris but the creatures of the forest are not ready to face you again after last time.... YOU WIN! .... \nAll %d enemies killed themselves. \nGAME OVER.' % count)
            break
        def pnorris():
            tmp = sp.call('clear',shell=True)
            print('                                 MMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                             NMMMMMMMMMMMMMMMMMMMMMMMM')
            time.sleep(0.01)
            print('                           MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN    ')
            time.sleep(0.01)
            print('                          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMD    ')
            time.sleep(0.01)
            print('                        DMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN    ')
            time.sleep(0.01)
            print('                      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN    ')
            time.sleep(0.01)
            print('                     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN    ')
            time.sleep(0.01)
            print('                     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN    ')
            time.sleep(0.01)
            print('NM                  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('MMMMM              MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print(' MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('  MMMMMMMMMMMMMMMMMMMMMMMMMM8MMMMMMMMMIMMMMM8,. ...........OMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('     MMMMMMMMMMMMMMMMMMMMMMM ..N. .....~MMMM...............:MMMMNMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('       NMMMMMMMMMMMMMMMMMMMMM.....:..DMMMMMNZ Z.... .......M$MMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('           MMMMMMMMMMNMMMMMMM....... 7=MMMMMMO....Z .......MM7MMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('              MMMMMMMMMMMMMMMMM  Z...MMMZ .. .,M..,........MMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                  MMMMMM.......DOM ....N7..................MMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                     MMM....... M. ... .  ... ..............M...$MMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                       ........... ........~. ..............M..=....+MMMMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                       ......+.NMI~........ . ..............M.,.I...MMMMMMMMMMMMMMN    ')
            time.sleep(0.01)
            print('                       ......$... ...... O..................,.....$MMMMMMMMMMMMN    ')
            time.sleep(0.01)
            print('                       .....M.......... M M.. .............. 8  .OMMMMMMMMMMMN    ')
            time.sleep(0.01)
            print('                        ..=7I,,.,,IMI...M.................. ..MMMMMMMMMMM ')
            time.sleep(0.01)
            print('                        ....DMMMMMMMMMMMMMMMO..............D...MMMMMMMMM    ')
            time.sleep(0.01)
            print('                         .MMMMMMMMMMMMMMDDMM:,N..............DMMMMMMMMMMM    ')
            time.sleep(0.01)
            print('                         NMMMMMNMM8 . .... ...,~............  MMMMMMMMM    ')
            time.sleep(0.01)
            print('                         MMMMM,:......::~..M8M8MM...............MMMMMM    ')
            time.sleep(0.01)
            print('                         MMMM ... . .........,MM..............MMMMMO$    ')
            time.sleep(0.01)
            print('                         MMMMM... =.=. .. . . MM ....... . ...MMMMMMM    ')
            time.sleep(0.01)
            print('                          NMMMMMMMMMM?  ..O.?NM7 ....... ......MMMMMM    ')
            time.sleep(0.01)
            print('                           NMMMMMMMMMMMMMMMMM........  $ . ...MMMNMMM    ')
            time.sleep(0.01)
            print('                            MMMMMMMMMMMMMMM.........,, ......MMMMMMMM    ')
            time.sleep(0.01)
            print('                             OMMMMMMMM8 , .. .. .,N.... ...:MMMMMMMMMMN    ')
            time.sleep(0.01)
            print('                              MMMMMMMM?N. ...~MD.:MNI8MMMMMMMMMMMMMMMMMN    ')
            time.sleep(0.01)
            print('                         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN    ')
            time.sleep(0.01)
            print('                      NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN    ')
            time.sleep(0.01)
            print('                     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN    ')
            time.sleep(0.01)
            print('                  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ')
            time.sleep(0.01)
        if name == 'FUCK CHUCK NORRIS':
            pnorris()
            print('Chuck Norris does not wear a condom. Because there is no such thing as protection from Chuck Norris. \nYou lose...... \nGAME OVER')
            break
        if count%5 != 0:
            critterhitpoints = critterdict[enemy]                                                                          
            penemy(enemy)
        else:
            pnorris()
            enemy = 'Chuck Norris'
            critterhitpoints = critterdict[enemy]
            moves = Norris
        if enemy == "Mouse":                                                                                           
            moves = Mouse                                                                                              
        elif enemy == "Dragon":                                                                                        
            moves = Dragon                                                                                             
        elif enemy == 'Zombie':                                                                                                          
            moves = Zombie                                                                                             
        print("\nLOOKOUT! THERE'S A %s!\nLevel: %d" % (enemy, count))
        critterhitpoints += count *2 
        while hitpoints > 0 and critterhitpoints > 0:                                                                  
            attack = atk()
            while last == attack:
                if len(inventory) == 0:
                    attack = input("\nYou cannot use the same attack twice in a row. \nPlease choose an attack ((P)unch [7-10], (R)oundhouse Kick[8-20], (S)moldering Stare[0-15])! \n Use the First letter of the attack. ").upper()                    
                    while attack != 'P' and attack != 'R' and attack != 'S':
                        attack = atk()
                else:
                    attack = input('You cannot use the same attack twice in a row!!! \nPlease choose a move ((P)unch [7-10], (R)oundhouse Kick[8-20], (S)moldering Stare[0-15])!\nYou can also use an (I)tem if you want... \nCurrent inventory: %s '% inventory).upper()
                    if attack == 'B' or attack == 'C' or attack == 'T':
                        useitem(attack)
                        if critterhitpoints > 0:
                            attack = input("\nYour HP:%s \nEnemy HP:%s\nChoose your attack! ((P)unch [7-10], (R)oundhouse Kick[8-20], (S)moldering Stare[0-15])! \n Use the First letter of the attack "%(hitpoints, critterhitpoints, inventory)).upper()                    
            while attack != 'P' and attack != 'R' and attack != 'S' and critterhitpoints > 0:
                    attack = atk() 
            tmp = sp.call('clear',shell=True)
            penemy(enemy)
            if attack == 'P':
                last = attack
                attack = random.randint(7,10)
                print('       ,--.--._')
                time.sleep(0.12)
                print('------- _, \___)')
                time.sleep(0.12)
                print('        / _/____)')
                time.sleep(0.12)
                print('        \//(____)')
                time.sleep(0.12)
                print('------\     (__)')
                time.sleep(0.12)
                print('       `------')
                time.sleep(0.12)

            elif attack == 'R':
                last = attack
                attack = random.randint(8,20)
                print('          \|//                       ')        
                time.sleep(0.0312)
                print('        -/_ /            ,-.   *     ')      
                time.sleep(0.0312)
                print('          _\\_           |  \    *  ')       
                time.sleep(0.0312)
                print('          \_  \          x  |   *  ')       
                time.sleep(0.0312)
                print(' /\_,///   >   )         \_  \     ')                
                time.sleep(0.0312)
                print('/ ,/   +\ /   /         _/ )_/     ')                 
                time.sleep(0.0312)
                print('\__|+ O  )  \/        _/ \/       ')                 
                time.sleep(0.0312)
                print('   /\__D/    \      _/    )       ')                  
                time.sleep(0.0312)
                print('    /  _   o  \   _/,   _/         ')                   
                time.sleep(0.0312)
                print('   /   /       ,_/   __/         ')              
                time.sleep(0.0312)
                print('  /   / \    o//    _/           ')             
                time.sleep(0.0312)
                print(' /__o/   \___|    _/             ')             
                time.sleep(0.0312)
                print(' _//       \__ __/\             ')        
                time.sleep(0.0312)
                print(' \  \>       \     \            ')                         
                time.sleep(0.0312)
                print(' // |         \__   \           ')                         
                time.sleep(0.0312)
                print('               /    /')                                          
                time.sleep(0.0312)
                print('               \___(')                                           
                time.sleep(0.0312)
                print('               /_/' )                                            
                time.sleep(0.0312)
                print('              / O |' )                                           
                time.sleep(0.0312)
                print('              |-   \__')                                        
                time.sleep(0.0312)
                print('                \_____)')                                       
                time.sleep(0.2)

            elif attack == 'S':
                if enemy == 'Chuck Norris':
                    while attack == 'S':
                        print('Chuck Norris is unimpressed with your smolder... Try something else!')
                        attack = input("\nYou cannot use the same attack twice in a row. \nPlease choose an attack ((P)unch [7-10], (R)oundhouse Kick[8-20], (S)moldering Stare[0-15])! \n Use the First letter of the attack. ").upper()                    
                        if attack == 'P':
                            pnorris()
                            last = attack
                            attack = random.randint(7,10)
                        elif attack == 'R':
                            pnorris()
                            last = attack
                            attack = random.randint(8,20)
                else:
                    last = attack
                    attack = random.randint(0,15)
                    print('    .-||||||-.\n  .|  -\  /-  |.\n /   O      O  |\n:                :\n|                | smolder \n:       __       :\n \  .-/`  `\-.  /\n  \.          ./\n    --......--\n')

            elif attack == '':
                last = ''
                attack = 0
            critterhitpoints-=attack
            moveslist = []                                                                                             
            if critterhitpoints <=0: 
                print("\nCongratulations! You killed the %s and gained 20 HP! \n" %enemy)
                time.sleep(0.35)
                hitpoints += 20
                items = ['Po(T)ion', '(B)omb', '(C)ocaine']
                gained= items[random.randint(0,2)]
                itemcount = random.randint(1,2)
                loopcount = 0
                while loopcount < itemcount:
                    inventory.append(gained)
                    loopcount+=1
                if count <= most:
                    sys.stdout.write('The %s dropped %d %s(s)! You can use it as your next attack if you want.\n' %(enemy,itemcount, gained))
                    time.sleep(0.4)
                count+=1
                if count <= most:
                    print('Another enemy approaches!')
                    break
                else:
                    print('You Survived the Forest!!! \n... I really didnt think you would. \nYou survived with %d HP' % hitpoints)
                    print('   _____                            _         _       _   _                  __     __          __          ______  _   _ _  ')
                    print('  / ____|                          | |       | |     | | (_)                 \ \   / /          \ \        / / __ \| \ | | | ')
                    print(' | |     ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___   \ \_/ /__  _   _   \ \  /\  / / |  | |  \| | | ')
                    print(' | |    / _ \| \'_ \ / _` | \'__/ _` | __| | | | |/ _` | __| |/ _ \| \'_ \/ __|   \   / _ \| | | |   \ \/  \/ /| |  | | . ` | | ')
                    print(' | |___| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \    | | (_) | |_| |    \  /\  / | |__| | |\  |_| ')
                    print('  \_____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/    |_|\___/ \__,_|     \/  \/   \____/|_| \_(_) ')
                    break
            if attack != 0:
                print("\nYou hit the %s for %d damage and have reduced the enemies HP to %s" % (enemy, attack, critterhitpoints))
            else:
                print('Enemy HP = %d' % critterhitpoints)
            for key in moves:                                                                                          
                moveslist.append(key)                                                                                  
            if enemy == 'Zombie' or enemy =='Mouse':
                enemyhit = moveslist[random.randint(0,2)]                                                                  
                hitpoints -= moves[enemyhit]                                                                               
            elif enemy == 'Dragon':
                enemyhit = moveslist[random.randint(0,4)]                                                                  
                hitpoints -= moves[enemyhit]                                                                               
            elif enemy == 'Chuck Norris':
                enemyhit = moveslist[random.randint(0,3)]                                                                  
                hitpoints -= moves[enemyhit]                                                                               
            print('The %s hit you with %s! You have %d HP left' % (enemy, enemyhit, hitpoints)) 
            if hitpoints <= 0: 
                if enemy == 'Chuck Norris':
                    print('\"You Fought well... You\'ve earned my respect..\" -Chuck Norris')
                print('You are DEAD!!')
                print('  ________    _____      _____  ___________ ')
                print(' /  _____/   /  _  \    /     \ \_   _____/ ')
                print('/   \  ___  /  /_\  \  /  \ /  \ |    __)_  ')
                print('\    \_\  \/    |    \/    Y    \|        \ ')
                print(' \______  /\____|__  /\____|__  /_______  / ')
                print('        \/         \/         \/        \/  ')
                print('____________   _________________________  ')
                print('\_____  \   \ /   /\_   _____/\______   \ ')
                print(' /   |   \   Y   /  |    __)_  |       _/ ')
                print('/    |    \     /   |        \ |    |   \ ')
                print('\_______  /\___/   /_______  / |____|_  / ')
                print('        \/                 \/         \/  ')
                break
