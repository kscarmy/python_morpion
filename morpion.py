from random import randint
 
 
lettres=("a","b","c","d","e","f","g","h","i")     #je fais une liste avec des lettres qui correspondront au emplacements où pourra jouer le joueur
 
prochain_coup=[10,10] # calcule le prochain coup de l ordinateur, 10 == valeur neutre
 
prochain_coup_humain=[10,10] # calcule le prochain coup du joueur humain, 10 == valeur neutre
 
clone=[[0,0,0],[0,0,0],[0,0,0]] # copie du plateau etats_partie permettant a l ordinateur de faire ses calculs
 
fin_1=[[1,1,0], [1,0,1], [0,1,1]] # liste de differents etats permetant a la croix de gagner
 
fin_2=[[2,2,0], [2,0,2], [0,2,2]] # liste de differents etats permetant au rond de gagner
 
etat1=[ ["a","b","c"],     #je fais une liste avec des lettres qui correspondront au emplacements où pourra jouer le joueur
        ["d","e","f"],
        ["g","h","i"]]
 
etats_partie=[ [0,0,0], # stocke l etat en cour de la partie
     [0,0,0],
     [0,0,0]]
 
etats_tests=[ [1,2,3], # tableau pour faire des tests unitaires
              [4,5,6],
              [7,8,9]]
 
def main(): # fonction de depart a lancer pour pouvoir jouer
    rotate = -1 # ancienne variable de rotation, permet actuellement de connaitre le retour de la fonction ordinateur
    win_ret=0 # valeur de retour de la fonction is_win qui detecte si la partie est finie avec un gagant
    print("Qui commence ?")
    print("Entres '1' si tu veux commencer, sinon '0'")
    joueur1=int(input()) # input demandant au joueur humain qui commence
    coups_max=0 # variable de stockage des coups maximums
    joueur=-1 # variable permettant de savoir qui commence la partie
    if  joueur1==1:
        plateau_affichage(etats_partie)
    else:
        rotate = ordinateur(etats_partie,joueur1 ,coups_max, rotate) # premier coup de l ordinateur
        plateau_affichage(etats_partie)
        coups_max+=1
    while coups_max <9 and win_ret==0: # boucle de jeux, tant que le nombre de coups maximum n a pas ete atteint et personne n a gagne
 
        saisie_joueur(joueur1) # demande au joueur humain d effectuer son coup
        plateau_affichage(etats_partie)
        win_ret = is_win() # fonction de determination de victoire d un des joueurs
        if coups_max!=9 and win_ret == 0: # si il reste des coups a jouer et que personne n a gagne alors l ordinateur joue
            rotate = ordinateur(etats_partie,joueur1 ,coups_max, rotate) # algo principal de l ordinateur
            plateau_affichage(etats_partie)
            win_ret = is_win()
            coups_max+=1
        coups_max+=1
        if coups_max==9 and win_ret == 0: # verifie si le nombre maximum de coup a ete executer et si personne n a gagne
            win_ret=2
    if win_ret == 2:
        print("Match nul !")
    elif win_ret == 4:
        print("x win")
    elif win_ret == 5:
        print("O win")
    else:
        print("erreur") # Une erreur c est deroule lors de la verification du plateau
 
def saisie_joueur(joueur1): # verifie si la lettre correspondant a une case de la grille est bien vide
    emplacement=verif_lettre()
    if emplacement=="a":
        remplacement_lettre("a", joueur1)
    if emplacement=="b":
        remplacement_lettre("b", joueur1)
    if emplacement=="c":
        remplacement_lettre("c", joueur1)
    if emplacement=="d":
        remplacement_lettre("d", joueur1)
    if emplacement=="e":
        remplacement_lettre("e", joueur1)
    if emplacement=="f":
        remplacement_lettre("f", joueur1)
    if emplacement=="g":
        remplacement_lettre("g", joueur1)
    if emplacement=="h":
        remplacement_lettre("h", joueur1)
    if emplacement=="i":
        remplacement_lettre("i", joueur1)
 
def remplacement_lettre(lettre, joueur1): # verifie si la case est attribue
    for g in range (3):
        for i in range (3):
            if etat1[g][i]==lettre:
                if etats_partie[g][i] == 0:
                    if joueur1 == 0:
                        etats_partie[g][i] = 1
                    else:
                        etats_partie[g][i] = 2
                else:
                    print ("lettre non valide")
                    saisie_joueur(joueur1)
 
def plateau_affichage(plateau): # affichage du plateau
    print()
    for ligne in range(0,3):
        for colonne in range(0,3):
            if colonne==0:
                print(" ",end='')
            if str(plateau[ligne][colonne])=="0":
                print(" ",end='')
            elif str(plateau[ligne][colonne])=="1":
                print("X",end='')
            elif str(plateau[ligne][colonne])=="2":
                print("O",end='')
            else:
                print(plateau[ligne][colonne],end='')
            if colonne < 2:
                print(end=" | ")
        if ligne==0:
            print("     a | b | c ",end='')
        elif ligne==1:
            print("     d | e | f ",end='')
        else:
            print("     g | h | i ",end='')
        print ("")
        if ligne < 2:
            print ("-----------   -----------")
    print ("")
 
def joueur2(tableau): # mouvements aleatoires du joueur ordinateur partie 1
    move=randint(0,8)
    move=place_libre_aleat(tableau,move)
    tableau[move//3][move%3]=2
 
def place_libre_aleat(tableau,move): # mouvements aleatoires du joueur ordinateur partie 2 et tests permettant de savoir si la place est libre
    while tableau[move//3][move%3]!=0:
        move=randint(0,8)
    return move
 
def verif_lettre(): # demande une lettre au joueur puis verifie si elle peut etre attribue
    while 1:
        i = 0
        lettre=(input("Entre une lettre :"))
        while i < 9 and lettres[i] != lettre:
            i+=1
        if i == 9:
            print("lettre non valide ! ")
        else:
            return lettre
 
def is_win(): # fonction de verification afin de savoir si l un des joueurs a trois prions alignes
    for i in range (3):
        if etats_partie[i][0] == etats_partie[i][1] == etats_partie[i][2] and etats_partie[i][2] != 0:
            if etats_partie[i][0] == 1:
                return 4
            else:
                return 5
    for u in range (3):
        if etats_partie[0][u] == etats_partie[1][u] == etats_partie[2][u] and etats_partie[2][u] != 0:
            if etats_partie[0][u] == 1:
                return 4
            else:
                return 5
    if etats_partie[0][0] == etats_partie[1][1] == etats_partie[2][2] and etats_partie[2][2] != 0:
            if etats_partie[0][0] == 1:
                return 4
            else:
                return 5
    elif etats_partie[0][2] == etats_partie[1][1] == etats_partie[2][0] and etats_partie[2][0] != 0:
            if etats_partie[2][0] == 1:
                return 4
            else:
                return 5
    return 0
 
def convertion(etats_partie, joueur1, coups_max): # conversion du plateau etats_partie : remplace les croix par des rond si le joueur humain commence. ainsi les algo de l ordinateur n ont pas besoin d en tenir compte
    m = 0
    for i in range (3):
        for g in range (3):
            clone[i][g] = etats_partie[i][g]
            if joueur1 == 1:
                if etats_partie[i][g] == 1:
                    clone[i][g] = 2
                    m = 1
                if etats_partie[i][g] == 2 and m == 0:
                    clone[i][g] = 1
                m = 0
 
def reconvertion(joueur1, coups_max): # fais l inverse de la fonction precedente, ce qui permet au joueur de continuer la partie
    m = 0
    for i in range (3):
        for g in range (3):
            etats_partie[i][g] = clone[i][g]
            if joueur1 == 1:
                if clone[i][g] == 1:
                    etats_partie[i][g] = 2
                    m = 1
                elif clone[i][g] == 2 and m == 0:
                    etats_partie[i][g] = 1
                m = 0
 
def ordi_first_coup(clone): # fonction qui positionne le premier coup de l ordinateur de maniere aleatoire sur 5 cases pre definies
    secu = 0
    while secu == 0:
        i = alea(6) # genere un premier coup aleatoire
        if i == 1 and secu == 0:
            if place_libre(clone, 0, 0) == 1:
                clone[0][0]=2
                secu = 1
        if i == 2 and secu == 0:
            if place_libre(clone, 0, 2) == 1:
                clone[0][2]=2
                secu = 1
        if i == 3 and secu == 0:
            if place_libre(clone, 2, 0) == 1:
                clone[2][0]=2
                secu = 1
        if i == 4 and secu == 0:
            if place_libre(clone, 2, 2) == 1:
                clone[2][2]=2
                secu = 1
        if  secu == 0 and (i == 5 or i == 6):
            if place_libre(clone, 1, 1) == 1:
                clone[1][1]=2
                secu = 1
 
def language_lettre(): # permet l affichage en lettre du prochain coup pour gagner
    if prochain_coup[0] != 10:
        return etat1[prochain_coup[0]][prochain_coup[1]]
    if prochain_coup_humain[0] != 10 and prochain_coup == 10:
        return etat1[prochain_coup_humain[0]][prochain_coup_humain[1]]
 
def ordinateur(etats_partie,joueur1 ,coups_max, rotate): # fonction principale du joueur ordinateur, celle ci gere ses coups et predis les coups gagnants
    convertion(etats_partie, joueur1, coups_max) # fonction de convertion permetant a la fonction ordinateur de faire ses calculs
    go_lose(clone) # fonction de verification du prochain coup gagnant pour le joueur humain
    gowin=0 # variable de stockage de la valeur retour de la fonction de verification du prochain coup du joueur ordinateur
    if coups_max == 0 or coups_max == 1:
        gowin=1
        ordi_first_coup(clone)
    else:
        gowin = go_win(clone) # fonction de verification du prochain coup gagnant du joueur ordinateur
        if prochain_coup[0] != 10:
            clone[prochain_coup[0]][prochain_coup[1]]=2 # stocke la valeur du prochain coup gagnant de l ordinateur et le joue
            gowin=1
    if gowin == 0:
        print("ordi joue aleatoire :") # anonce que l ordinateur compte jouer un coup aleatoire
        joueur2(clone)
    reconvertion(joueur1, coups_max) # fonction qui retranscrit tel qu etait de base le plateau pour que le joueur humain puisse jouer
    return rotate # ancienne valeur de retour d ordinateur qui servais a calculer le nombre de rotation effectue par une ancienne fonction supprimee
 
def place_libre(etat, x, y): # fonction qui, celon x et y passe en parametre nous indique si dans etat la case est vide ou non
    if etat[x][y] == 0:
        return 1
    else:
        return 0
 
def retourne_place_libre(etat): # retourne la valeur ou se situe une case libre pour calculer les prochains coups
    x = 0
    while etat[x] != 0:
        x+=1
    return x
 
def go_lose(etat): # fonction du joueur humain, celle ci permet d annoncer ou se situe le prochain coup gagnant, en indiquant coordonnees ainsi que la lettre
    x = 0 # variable des lignes
    y = 0 # variable des colonnes
    u = 0 # variable des diagonales
    while prochain_coup_humain[0]==10 and prochain_coup_humain[1]==10 and x < 2:  # calcul par comparaison avec fin_1 des lignes
        if prochain_coup_humain[0]==10 and etat[0] == fin_1[x]: # premiere ligne
            prochain_coup_humain[0] = 0
            prochain_coup_humain[1] = retourne_place_libre(fin_1[x])
        if prochain_coup_humain[0]==10 and etat[1] == fin_1[x]: # deuxieme ligne
            prochain_coup_humain[0] = 1
            prochain_coup_humain[1] = retourne_place_libre(fin_1[x])
        if prochain_coup_humain[0]==10 and etat[2] == fin_1[x]: # troisieme ligne
            prochain_coup_humain[0] = 2
            prochain_coup_humain[1] = retourne_place_libre(fin_1[x])
        x+=1
    while prochain_coup_humain[0]==10 and prochain_coup_humain[1]==10 and y < 2:   # calcul par comparaison avec fin_1 des colonnes
        if prochain_coup_humain[0]==10 and etat[0][0] == fin_1[y][0] and etat[1][0] == fin_1[y][1] and etat[2][0] == fin_1[y][2]: # premiere colonne
            prochain_coup_humain[0] = retourne_place_libre(fin_1[y])
            prochain_coup_humain[1] = 0
        if prochain_coup_humain[0]==10 and etat[0][1] == fin_1[y][0] and etat[1][1] == fin_1[y][1] and etat[2][1] == fin_1[y][2]: # deuxieme colonne
            prochain_coup_humain[0] = retourne_place_libre(fin_1[y])
            prochain_coup_humain[1] = 1
        if prochain_coup_humain[0]==10 and etat[0][2] == fin_1[y][0] and etat[1][2] == fin_1[y][1] and etat[2][2] == fin_1[y][2]: # troisieme colonne
            prochain_coup_humain[0] = retourne_place_libre(fin_1[y])
            prochain_coup_humain[1] = 2
        y+=1
    while prochain_coup_humain[0]==10 and prochain_coup_humain[1]==10 and u < 3:  # calcul par comparaison avec fin_1 des diagonales
        if prochain_coup_humain[0]==10 and etat[0][0] == fin_1[u][0] and etat[1][1] == fin_1[u][1] and etat[2][2] == fin_1[u][2]: # diagonale haut gauche / bas droite
            if u == 0:
                prochain_coup_humain[0] = 2
                prochain_coup_humain[1] = 2
            if u == 1:
                prochain_coup_humain[0] = 1
                prochain_coup_humain[1] = 1
            if u == 2:
                prochain_coup_humain[0] = 0
                prochain_coup_humain[1] = 0
        if prochain_coup_humain[0]==10 and etat[0][2] == fin_1[u][0] and etat[1][1] == fin_1[u][1] and etat[2][0] == fin_1[u][2]: # diagonale haut droite / bas gauche
            if u == 0:
                prochain_coup_humain[0] = 2
                prochain_coup_humain[1] = 0
            if u == 1:
                prochain_coup_humain[0] = 1
                prochain_coup_humain[1] = 1
            if u == 2:
                prochain_coup_humain[0] = 0
                prochain_coup_humain[1] = 2
        u+=1
    if prochain_coup_humain[0] != 10 and prochain_coup_humain[1] != 10: # annonce le prochain coup gagnant pour le joueur humain si il existe
        print("humain win in :[", prochain_coup_humain[0],";", prochain_coup_humain[1], "] ",end='')
        print("lettre :", language_lettre())
        return 1
    else:
        prochain_coup_humain[0] = 10
        prochain_coup_humain[1] = 10
        return 0
 
def go_win(etat):  # fonction du joueur ordinateur, celle ci permet d annoncer ou se situe le prochain coup gagnant, en indiquant coordonnees ainsi que la lettre et permet directement a ordinateur de jouer ce coup
    x = 0 # idem que fonction precedente sauf comparaisons avec fin_2
    y = 0
    u = 0
    while prochain_coup[0]==10 and prochain_coup[1]==10 and x < 2:  ## lignes
        if prochain_coup[0]==10 and etat[0] == fin_2[x]:
            prochain_coup[0] = 0
            prochain_coup[1] = retourne_place_libre(fin_2[x])
        if prochain_coup[0]==10 and etat[1] == fin_2[x]:
            prochain_coup[0] = 1
            prochain_coup[1] = retourne_place_libre(fin_2[x])
        if prochain_coup[0]==10 and etat[2] == fin_2[x]:
            prochain_coup[0] = 2
            prochain_coup[1] = retourne_place_libre(fin_2[x])
        x+=1
    while prochain_coup[0]==10 and prochain_coup[1]==10 and y < 2:                                      ###colones
        if prochain_coup[0]==10 and etat[0][0] == fin_2[y][0] and etat[1][0] == fin_2[y][1] and etat[2][0] == fin_2[y][2]:
            prochain_coup[0] = retourne_place_libre(fin_2[y])
            prochain_coup[1] = 0
        if prochain_coup[0]==10 and etat[0][1] == fin_2[y][0] and etat[1][1] == fin_2[y][1] and etat[2][1] == fin_2[y][2]:
            prochain_coup[0] = retourne_place_libre(fin_2[y])
            prochain_coup[1] = 1
        if prochain_coup[0]==10 and etat[0][2] == fin_2[y][0] and etat[1][2] == fin_2[y][1] and etat[2][2] == fin_2[y][2]:
            prochain_coup[0] = retourne_place_libre(fin_2[y])
            prochain_coup[1] = 2
        y+=1
    while prochain_coup[0]==10 and prochain_coup[1]==10 and u < 3:
        if prochain_coup[0]==10 and etat[0][0] == fin_2[u][0] and etat[1][1] == fin_2[u][1] and etat[2][2] == fin_2[u][2]:
            if u == 0:
                prochain_coup[0] = 2
                prochain_coup[1] = 2
            if u == 1:
                prochain_coup[0] = 1
                prochain_coup[1] = 1
            if u == 2:
                prochain_coup[0] = 0
                prochain_coup[1] = 0
        if prochain_coup[0]==10 and etat[0][2] == fin_2[u][0] and etat[1][1] == fin_2[u][1] and etat[2][0] == fin_2[u][2]:
            if u == 0:
                prochain_coup[0] = 2
                prochain_coup[1] = 0
            if u == 1:
                prochain_coup[0] = 1
                prochain_coup[1] = 1
            if u == 2:
                prochain_coup[0] = 0
                prochain_coup[1] = 2
        u+=1
    if prochain_coup[0] != 10 and prochain_coup[1] != 10:
        print("ordi win in :[", prochain_coup[0],";", prochain_coup[1],"] ", end='')
        print("lettre :", language_lettre())
        return 1
    else:
        prochain_coup[0] = 10
        prochain_coup[1] = 10
        return 0
 
def alea(nbr): # genere un nombre aleatoire
    nombre=randint(1,nbr)
    return nombre
 