#!/usr/bin/python3
#coding=utf-8
################################# Credits ##########################################################
# Contact: t.me/Faxelh
# Le credit pour ce code va a Mr Faxel
# Vous pouvez recoder , mais toute fois mentionner le nom de l'auteur merci boss.
####################################################################################################
raw_input = input
####################################################################################################
# -Effacer le systeme en question-#
import os,platform
def _cls():
    if os.name == 'nt':
         os.system('cls')
    else:
         os.system('clear')
####################################################################################################
# -La date du jours courant-#
def horaire():
    os.system('date | lolcat')
    #print("\t\033[38;5;214m \033[1;31m  [\033[1;37m++\033[1;31m]\033[042m \033[1;37m Codé par\033[1;31m : \033[38;5;245m Mr \033[38;5;247mFaxel\033[1;31m [\033[1;37m++\033[1;31m] \033[00m")
####################################################################################################
logo_faxel =("""\033[38;5;247m╭━╮╭━╮╱╱\033[38;5;214m╭━━━╮╱╱╱╱╱╱╱╱╭╮\n\033[38;5;247m┃┃╰╯┃┃╱╱\033[38;5;214m┃╭━━╯╱╱╱╱╱╱╱╱┃┃\n\033[38;5;247m┃╭╮╭╮┣━╮\033[38;5;214m┃╰━━┳━━┳╮╭┳━━┫┃\n\033[38;5;247m┃┃┃┃┃┃╭╯\033[38;5;214m┃╭━━┫╭╮┣╋╋┫┃━┫┃\n\033[38;5;247m┃┃┃┃┃┃┃╱\033[38;5;214m┃┃╱╱┃╭╮┣╋╋┫┃━┫╰╮\n\033[38;5;247m╰╯╰╯╰┻╯╱\033[38;5;214m╰╯╱╱╰╯╰┻╯╰┻━━┻━╯""")
logo_robot =("""\t\033[38;5;214m──\033[38;5;125m▄\033[38;5;214m────\033[38;5;125m▄▄▄▄▄▄▄\033[38;5;214m────\033[38;5;125m▄\033[38;5;214m───\n\t\033[38;5;214m─\033[38;5;125m▀▀▄\033[38;5;214m─\033[38;5;125m▄█████████▄\033[38;5;214m─\033[38;5;125m▄▀▀\033[38;5;214m──\n\t\033[38;5;214m─────\033[38;5;125m██\033[38;5;214m─\033[38;5;125m▀███▀\033[38;5;214m─\033[38;5;125m██\033[38;5;214m──────\n\t\033[38;5;214m───\033[38;5;125m▄\033[38;5;214m─\033[38;5;125m▀████▀████▀\033[38;5;214m─\033[38;5;125m▄\033[38;5;214m────\n\t\033[38;5;214m─\033[38;5;125m▀█\033[38;5;214m────\033[38;5;125m██▀█▀██\033[38;5;214m────\033[38;5;125m█▀\033[38;5;214m──\n\t\033[1;97m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n\t\033[1;97m█\033[1;92m░░\033[38;5;245m╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗\033[1;92m░░\033[1;97m█\n\t\033[1;97m█\033[1;92m░░\033[38;5;245m║║║╠─║─║─║║║║║╠─\033[1;92m░░\033[1;97m█\n\t\033[1;97m█\033[1;92m░░\033[38;5;245m╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝\033[1;92m░░\033[1;97m█\n\t\033[1;97m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█""")
####################################################################################################
# -Importation des modules- #
try:
    import os,time,sys,fileinput,requests,mechanize,datetime
    print("\033[1;92m Exigences disponibles")
    _cls()
except:
    _cls()
    print("\033[1;96m Configuration requise pour l'installation....\033[1;97m\n")
    os.system('pip install requests')
    os.system('pip install mechanize')
    os.system('sudo apt-get install ruby')
    os.system('sudo gem install lolcat')
    os.system('sudo apt-get install toilet')
    os.system('sudo apt-get install figlet')
    os.system('sudo apt-get install cowsay')
    os.system('python3 -m pip install --upgrade pip')
    _cls()
####################################################################################################
# -Automatisation-#
def mael(f):
    for l in f + '\n':
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.009)
        #time.sleep(1e-43)
####################################################################################################
# -Animation a ma troisieme methode-#
def periode():
   periodique = ['.','..','...','....','.....']
   for o in periodique:
     print("\r\033[1;91m[●] \033[1;92mChargement en cours\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
####################################################################################################
########## -Au revoir- ##########
def bye():
     sys.exit()
####################################################################################################
########## -Arret animer- ##########
def arret():
    mael("\033[1;97m╔══╗─────╔╗───────────────╔═╗")
    mael("\033[1;97m║╔╗╠╦╦╦╦═╣╚╗╔═╦═╦╗╔═╦═╦╦╦╦╣═╣")
    mael("\033[1;91m║╠╣║╔╣╔╣╩╣╔╣║╩╣║║║║═╣╬║║║╔╬═║")
    mael("\033[1;91m╚╝╚╩╝╚╝╚═╩═╝╚═╩╩═╝╚═╩═╩═╩╝╚═╝")
    mael('\033[1;97m▒▒▒▒▒▒▒▒▒▒')
    print("\033[1;32m0%")
    mael('\033[1;97m█▒▒▒▒▒▒▒▒▒')
    print("\033[1;32m10%")
    mael('\033[1;97m███▒▒▒▒▒▒▒')
    print("\033[1;32m30%")
    mael('\033[1;97m█████▒▒▒▒▒')
    print("\033[1;32m50%")
    mael('\033[1;97m███████▒▒▒')
    print("\033[1;32m80%")
    mael('\033[1;97m██████████')
    print("\033[1;32m100%")
    mael("\n\033[1;97mBye Mec, j\'espere que tu as adorée le script de\033[1;91m Mr \033[1;96mFaxel\033[1;97m.A bientot!!\n")
    bye()
####################################################################################################
# -Chargement a ma deuxieme methode-#
def load(mot):
    chaine = [
     '/', '-', '|']
    for i in range(5):
        for x in range(len(chaine)):
            sys.stdout.write(('\r{}{}').format(str(mot), chaine[x]))
            time.sleep(0.3)
            sys.stdout.flush()
####################################################################################################
# -Chargement a ma premiere methode-#
def charge():
    compteur = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100"]
    print
    for b in compteur:
        sys.stdout.write("\r\033[1;91m[\033[1;93m*\033[1;91m] \033[38;5;245m@\033[38;5;221mFaxel\033[1;92m "+b+" \033[1;97m%")
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1.5)
####################################################################################################
logos =("""\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███████████►\033[38;5;212mWrite by\033[38;5;111m Faxel\033[38;5;214m◄██████████\033[1;97m▓\033[38;5;131m▒░\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███████████►\033[38;5;136m╬╬╬╬╬╬╬╬╬╬╬╬╬╬\033[38;5;214m◄██████████\033[1;97m▓\033[38;5;131m▒░\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███►  \033[38;5;247m╔╗F╦╔═╗╔╗╔╦FF╦╔═╗╔╗╔╦F╦╔═╗\033[38;5;214m  ◄██\033[1;97m▓\033[38;5;131m▒░\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███►  \033[38;5;247m╠╩╗║║╣F║║║╚╗╔╝║╣F║║║║F║║╣F\033[38;5;214m  ◄██\033[1;97m▓\033[38;5;131m▒░\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███►  \033[38;5;247m╚═╝╩╚═╝╝╚╝F╚╝F╚═╝╝╚╝╚═╝╚═╝\033[38;5;214m  ◄██\033[1;97m▓\033[38;5;131m▒░\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███████████►\033[38;5;136m╬╬╬╬╬╬╬╬╬╬╬╬╬╬\033[38;5;214m◄██████████\033[1;97m▓\033[38;5;131m▒░\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███████████►\033[38;5;212mWrite by\033[38;5;111m Faxel\033[38;5;214m◄██████████\033[1;97m▓\033[38;5;131m▒░\n""")
logo =("""\033[38;5;214m●▬▬▬▬▬▬▬▬๑\033[1;97m●▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬●●▬▬▬▬▬\033[1;32m▬▬▬▬๑۩۩๑▬▬▬▬▬▬●            \n\033[38;5;214m•_  _ ____ \033[1;97m _  _ ____ ____ _  _\033[1;32m ____ ____   _  _• \n\033[38;5;214m•|\/| |__/ \033[1;97m |__| |__| |    |_/ \033[1;32m |___ |__/   |_/ • \n\033[38;5;214m•|  | |  \ \033[1;97m |  | |  | |___ | \_\033[1;32m |___ |  \ __| \_•    \n\033[38;5;214m●▬▬▬▬▬▬▬▬๑\033[1;97m●▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬●●▬▬▬▬▬\033[1;32m▬▬▬▬๑۩۩๑▬▬▬▬▬▬●\n\033[1;97m╔═════════════════════════════════════════════╗\n\033[1;97m║\033[1;91m[\033[1;93m**\033[1;91m]\033[38;5;95m      Developpeur \033[1;97m:\033[38;5;214m  Faxel           \033[1;91m[\033[1;93m**\033[1;91m]\033[1;97m║\n\033[1;97m╚═════════════════════════════════════════════╝""")
logo_ndao =("""\x1b[1;32m╔════╗─────\x1b[1;37m╔╗─╔╗─────╔╗\n\x1b[1;32m║╔╗╔╗║─────\x1b[1;37m║║─║║─────║║\n\x1b[1;32m╚╝║║╠╩═╦══╗\x1b[1;37m║╚═╝╠══╦══╣║╔╦╦═╗╔══╗\n\x1b[1;32m──║║║╔╗║╔╗║\x1b[1;37m║╔═╗║╔╗║╔═╣╚╝╬╣╔╗╣╔╗║\n\x1b[1;32m──║║║╚╝║╚╝║\x1b[1;37m║║─║║╔╗║╚═╣╔╗╣║║║║╚╝║\n\x1b[1;32m──╚╝╚══╣╔═╝\x1b[1;37m╚╝─╚╩╝╚╩══╩╝╚╩╩╝╚╩═╗║\n\x1b[1;32m───────║║──\x1b[1;37m─────────────────╔═╝║\n\x1b[1;32m───────╚╝──\x1b[1;37m─────────────────╚══╝ """)
logo_ach =("""\033[38;5;214m╭━━╮╱╱╱╱╱╱╱╱╱╱\033[38;5;136m╭╮╭╮╱╱╱╱╭╮\n\033[38;5;214m╰╮╭┻┳┳┳━━┳┳┳┳╮\033[38;5;136m┃╰╯┣━╮╭━┫┣╮\n\033[38;5;214m╱┃┃┻┫╭┫┃┃┃┃┣┃┫\033[38;5;136m┃╭╮┃╋╰┫━┫━┫\n\033[38;5;214m╱╰┻━┻╯╰┻┻┻━┻┻╯\033[38;5;136m╰╯╰┻━━┻━┻┻╯ """)
logo_youtube =("""\033[38;5;214m╔═══╗─────╔╗─\x1b[1;37m─────╔══\x1b[1;32m═╗─────╔╗\n\033[38;5;214m║╔══╝────╔╝╚╗\x1b[1;37m─────║╔═\x1b[1;32m╗║─────║║\n\033[38;5;214m║╚══╦══╦═╩╗╔╬\x1b[1;37m══╦═╗║║─\x1b[1;32m║╠╗╔╦══╣║\n\033[38;5;214m║╔══╣╔╗║══╣║║\x1b[1;37m║═╣╔╝║╚═\x1b[1;32m╝╠╬╬╣║═╣║\n\033[38;5;214m║║──║╔╗╠══║╚╣\x1b[1;37m║═╣║─║╔═\x1b[1;32m╗╠╬╬╣║═╣╚╗\n\033[38;5;214m╚╝──╚╝╚╩══╩═╩\x1b[1;37m══╩╝─╚╝─\x1b[1;32m╚╩╝╚╩══╩═╝""")
logo_sec =("""\x1b[1;32m╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱\033[38;5;214m ╭━━━╮╱╱╱╱╱╱╱╱╭╮\n\x1b[1;32m┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱\033[38;5;214m ┃╭━━╯╱╱╱╱╱╱╱╱┃┃\n\x1b[1;32m┃╰━━┳━━┳━━┳╮╭┳━╋╮╭╋╮╱╭╮\033[38;5;214m ┃╰━━┳━━┳╮╭┳━━┫┃\n\x1b[1;32m╰━━╮┃┃━┫╭━┫┃┃┃╭╋┫┃┃┃╱┃┃\033[38;5;214m ┃╭━━┫╭╮┣╋╋┫┃━┫┃\n\x1b[1;32m┃╰━╯┃┃━┫╰━┫╰╯┃┃┃┃╰┫╰━╯┃\033[38;5;214m ┃┃╱╱┃╭╮┣╋╋┫┃━┫╰╮\n\x1b[1;32m╰━━━┻━━┻━━┻━━┻╯╰┻━┻━╮╭╯\033[38;5;214m ╰╯╱╱╰╯╰┻╯╰┻━━┻━╯\n\x1b[1;32m╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃\n\x1b[1;32m╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯\n\033[1;97m╔═════════════════════════════════════════════╗\n\033[1;97m║\033[1;91m[\033[1;93m**\033[1;91m]\033[38;5;95m      Developpeur \033[1;97m:\033[38;5;214m  Faxel           \033[1;91m[\033[1;93m**\033[1;91m]\033[1;97m║\n\033[1;97m╚═════════════════════════════════════════════╝""")
logo_kali =("""\033[38;5;214m    ..,;:ccc,.                          \n\033[38;5;214m          ......''';lxO.                        \n\033[38;5;214m.....''''..........,:ld;                        \n\033[38;5;214m           .';;;:::;,,.x,                       \n\033[38;5;214m      ..'''.            0Xxoc:,.  ...           \n\033[38;5;214m  ....                ,ONkc;,;cokOdc',.         \n\033[38;5;214m .                   OMo           ':'o.       \n\033[38;5;214m                    dMc               :OO;      \n\033[38;5;214m                    0M.                 .:o.    \n\033[38;5;214m                    ;Wd                         \n\033[38;5;214m                     ;XO,                       \n\033[38;5;214m                       ,d0Odlc;,..              \n\033[38;5;214m                           ..',;:cdOOd::,.    \033[1;36m ⓥ①.⑦\n\033[38;5;214m                                    .:d;.':;.   \n\033[38;5;214m                                       'd,  .'  \n\033[38;5;214m                                         ;l   ..\n\033[38;5;214m                  \n\033[38;5;247m             🅵🅰🆇🅴🅻                         \033[38;5;214m.o    \n                                            c   \n\033[38;5;214m                                             .' \n\033[38;5;214m                                             .  """)
####################################################################################################
def securite():
    _cls()
    horaire()
    print(logo_sec)
    nom_u = 'Faxel'
    mdp = 'Faxel'
    print("\033[1;97m║")
    user = raw_input("\033[1;97m╬═\033[1;31m▶\033[38;5;245m NOM D'UTILISATEUR \033[1;97m═╬══\033[1;91m► \033[1;92m")
    if user == nom_u:
        pass
    elif not user == nom_u:
        print("\n\033[1;91m[\033[1;93m*\033[1;91m]\033[1;95m Nom d'utilisateur incorrect!")
        os.system('xdg-open https://wa.me/2250555709610')
        securite()
    print("\033[1;97m║")
    mot_passant = raw_input("\033[1;97m╬═\033[1;31m▶\033[38;5;245m MOT DE PASSE      \033[1;97m═╬══\033[1;91m► \033[1;93m")
    print("\033[1;97m╚═════════════════════════════════════════════╝")
    if mot_passant == mdp:
        load("\033[1;97m Chargement en cours\033[1;92m...")
        print("\n\033[1;91m[\033[1;93m!\033[1;91m]\033[1;92m Connexion réussie")
        Menu()
    elif not mot_passant == mdp:
        print("\n\033[1;91m[\033[1;93m*\033[1;91m]\033[1;95m Mot de passe incorrect!")
        os.system('xdg-open https://t.me/Faxelh')
        securite()
####################################################################################################
def connection(url='http://www.google.com/', timeout=3):
    try:
        _cls()
        verficateur_connexion = requests.get(url, timeout=timeout)
        verficateur_connexion.raise_for_status()
        load("\033[1;91m[\033[1;92m●\033[1;91m]\033[1;97m Verification de la connexion internet\033[1;92m...")
        _cls()
        print(logo_kali)
        mael("\t\t\033[1;92mVous êtes connecté à Internet\n")
        raw_input("\t\t\033[1;91m[[38;5;24mSuivant\033[1;91m]")
        return True
    except requests.HTTPError as e:
        print("\033[1;31m[\033[1;33m+\033[1;31m]\033[1;37m La vérification de la connexion Internet a échoué, code d'état {0}.".format(e.response.status_code))
    except requests.ConnectionError:
        mael("\t\t\033[1;91mVous n'êtes pas connecté à Internet.")
    return False
####################################################################################################
def verifie():
    if connection() == True:
         Menu()
    else:
         arret()
####################################################################################################
####################################################################################################
def Menu():
    _cls()
    horaire()
    print(logo)
    print("\033[1;97m╔"+42*"═"+1*"═╗")
    print("\033[1;97m║ \033[1;91m[\033[1;96m1.\033[1;91m]\033[38;5;136m Generer une bordure avec toilet mono \033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[1;96m2.\033[1;91m]\033[38;5;214m Generer une bordure avec toilet pagga\033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[1;96m3.\033[1;91m]\033[38;5;131m Generer une bordure avec toilet term \033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[1;96m4.\033[1;91m]\033[38;5;245m Generer une bordure avec toilet small\033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[1;96m5.\033[1;91m]\033[38;5;245m Generer une bordure avec figlet pagga\033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[1;96m6.\033[1;91m]\033[38;5;245m Generer une bordure avec figlet small\033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[1;96m7.\033[1;91m]\033[38;5;133m Groupe Telegram N°1                  \033[1;97m║")
    print("\033[1;97m╚"+42*"═"+1*"═╝")
    print("\033[1;97m║")
    choix_menu()
def choix_menu():
    dmd = raw_input("\033[1;97m╚═\033[1;31m▶\033[38;5;245m Mr \033[38;5;221mFaxel \033[1;97m═╬══\033[1;91m► \033[1;96m")
    if dmd =="":
        print("\n\t\033[1;91m[\033[1;93m!\033[1;91m]\033[1;95m Remplissez correctement ")
        Menu()
    elif dmd =="1":
        toilet_mono()
    elif dmd =="2":
        toilet_pagga()
    elif dmd =="3":
        toilet_term()
    elif dmd =="4":
        toilet_small()
    elif dmd =="5":
        figlet_pagga()
    elif dmd =="6":
        figlet_small()
    elif dmd =="7":
        _cls()
        print(logo_ach)
        mael("\033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Groupe Telegram Hack & Security Areas" )
        os.system('xdg-open https://t.me/linux_tor')
        raw_input('\n\033[1;91m [\033[1;93m!\033[1;91m]\033[1;97m Appuyer entrer pour retourner au menu...')
        Menu()
    else:
        print('\n\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m '+dmd+' \x1b[1;91mindisponible')
        raw_input('\n\033[1;91m[\033[1;93m!\033[1;91m]\033[1;97m Appuyer entrer pour retourner au menu...')
        Menu()
####################################################################################################
def toilet_mono() :
     _cls()
     print(logo_robot)
     print("\033[1;97m╔════════════════════════════════════╗")
     print("\033[1;97m║      \033[1;91m[\033[1;93m*\033[1;91m]\033[1;97m Write by \033[38;5;221mFaxel \033[1;91m[\033[1;93m*\033[1;91m]        \033[1;97m║\033[38;5;245m")
     print("\033[1;97m╚════════════════════════════════════╝")
     print("\033[1;97m║")
     _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \033[1;91m[\033[1;93m▶\033[1;91m]\033[38;5;245m Entrer votre nom \033[1;97m═╬══\033[1;91m► \033[38;5;221m")
     _cls()
     print("\n")
     os.system("toilet -f mono12 -F border " +_dmd+" | lolcat")
     raw_input('\n\n\n\n\n\033[1;91m[\033[1;93m+\033[1;91m]\033[1;97m Appuyer entrer pour retourner au menu...')
     Menu()
####################################################################################################
def toilet_pagga():
     _cls()
     print(logo_robot)
     print("\033[1;97m╔════════════════════════════════════╗")
     print("\033[1;97m║      \033[1;91m[\033[1;93m*\033[1;91m]\033[1;97m Write by \033[38;5;221mFaxel \033[1;91m[\033[1;93m*\033[1;91m]        \033[1;97m║\033[38;5;245m")
     print("\033[1;97m╚════════════════════════════════════╝")
     print("\033[1;97m║")
     _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \033[1;91m[\033[1;93m▶\033[1;91m]\033[38;5;245m Entrer votre nom \033[1;97m═╬══\033[1;91m► \033[38;5;221m")
     _cls()
     print("\n")
     os.system("toilet -f pagga " +_dmd+" | lolcat")
     raw_input('\n\n\n\n\n\033[1;91m[\033[1;93m+\033[1;91m]\033[1;97m Appuyer entrer pour retourner au menu...')
     Menu()
####################################################################################################
def toilet_term():
     _cls()
     print(logo_robot)
     print("\033[1;97m╔════════════════════════════════════╗")
     print("\033[1;97m║      \033[1;91m[\033[1;93m*\033[1;91m]\033[1;97m Write by \033[38;5;221mFaxel \033[1;91m[\033[1;93m*\033[1;91m]        \033[1;97m║\033[38;5;245m")
     print("\033[1;97m╚════════════════════════════════════╝")
     print("\033[1;97m║")
     _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \033[1;91m[\033[1;93m▶\033[1;91m]\033[38;5;245m Entrer votre nom \033[1;97m═╬══\033[1;91m► \033[38;5;221m")
     _cls()
     print("\n")
     os.system("toilet -f term -F border " +_dmd+" | lolcat")
     raw_input('\n\n\n\n\n\033[1;91m[\033[1;93m+\033[1;91m]\033[1;97m Appuyer entrer pour retourner au menu...')
     Menu()
####################################################################################################
def toilet_small():
     _cls()
     print(logo_robot)
     print("\033[1;97m╔════════════════════════════════════╗")
     print("\033[1;97m║      \033[1;91m[\033[1;93m*\033[1;91m]\033[1;97m Write by \033[38;5;221mFaxel \033[1;91m[\033[1;93m*\033[1;91m]        \033[1;97m║\033[38;5;245m")
     print("\033[1;97m╚════════════════════════════════════╝")
     print("\033[1;97m║")
     _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \033[1;91m[\033[1;93m▶\033[1;91m]\033[38;5;245m Entrer votre nom \033[1;97m═╬══\033[1;91m► \033[38;5;221m")
     _cls()
     print("\n")
     os.system("toilet -f small " +_dmd+" | lolcat")
     raw_input('\n\n\n\n\n\033[1;91m[\033[1;93m+\033[1;91m]\033[1;97m Appuyer entrer pour retourner au menu...')
     Menu()
####################################################################################################
def figlet_pagga():
     _cls()
     print(logo_robot)
     print("\033[1;97m╔════════════════════════════════════╗")
     print("\033[1;97m║      \033[1;91m[\033[1;93m*\033[1;91m]\033[1;97m Write by \033[38;5;221mFaxel \033[1;91m[\033[1;93m*\033[1;91m]        \033[1;97m║\033[38;5;245m")
     print("\033[1;97m╚════════════════════════════════════╝")
     print("\033[1;97m║")
     _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \033[1;91m[\033[1;93m▶\033[1;91m]\033[38;5;245m Entrer votre nom \033[1;97m═╬══\033[1;91m► \033[38;5;221m")
     _cls()
     print("\n")
     os.system("figlet -f small " +_dmd+" | lolcat")
     raw_input('\n\n\n\n\n\033[1;91m[\033[1;93m+\033[1;91m]\033[1;97m Appuyer entrer pour retourner au menu...')
     Menu()
####################################################################################################
def figlet_small():
     _cls()
     print(logo_robot)
     print("\033[1;97m╔════════════════════════════════════╗")
     print("\033[1;97m║      \033[1;91m[\033[1;93m*\033[1;91m]\033[1;97m Write by \033[38;5;221mFaxel \033[1;91m[\033[1;93m*\033[1;91m]        \033[1;97m║\033[38;5;245m")
     print("\033[1;97m╚════════════════════════════════════╝")
     print("\033[1;97m║")
     _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \033[1;91m[\033[1;93m▶\033[1;91m]\033[38;5;245m Entrer votre nom \033[1;97m═╬══\033[1;91m► \033[38;5;221m")
     _cls()
     print("\n")
     os.system("figlet -f pagga " +_dmd+" | lolcat")
     raw_input('\n\n\n\n\n\033[1;91m[\033[1;93m+\033[1;91m]\033[1;97m Appuyer entrer pour retourner au menu...')
     Menu()
####################################################################################################
#load("\033[1;91m[\033[1;92m@\033[1;91m]\033[38;5;245m Server\033[38;5;214m Faxel\033[38;5;241m...\033[48;5;0;38;5;192m")
####################################################################################################
####################################################################################################
if __name__ == "__main__":
     verifie()
####################################################################################################