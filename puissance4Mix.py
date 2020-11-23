# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 12:08:18 2020

@author: Thomas NGO & Quentin GIBON & Salma MAHDOUB
"""


import math

def copy_game_state(s):
    new_state = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
    for i in range(6):
        for j in range(12):
            new_state[i][j] = s[i][j]
    return new_state


def Empty_grid(state):
    empty=False
    for i in range(6):
        for j in range(12):
            if state[i][j]==' ':
                empty=True
    return empty

#affiche la table de jeu
def Print_board(game_state):
    print('-----------------------------------------------------')
    for i in range(6):
        print()
        for j in range(12):
            print(" ",game_state[i][j], end=' ')
    print()
    print('-------------------------------------------------')
    print('| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |')
    print('-------------------------------------------------')
    
#Determine qui doit joueur
def joueur(jeu):
    compteur=0
    for i in range(len(jeu)):
        if(jeu[i]=='X'):
            compteur=compteur+1
        elif(jeu[i]=='O'):
            compteur=compteur-1
    return 'X' if compteur==0 else 'O'

#Determine les colonnes encore jouables
def coupPossible(jeu):
    coups = []
    empty = False
    for i in range(12):
        empty = False
        for j in range(6):
            if(jeu[j][i] is ' '):
                empty = True
        if empty == True:
            coups.append(i)
    
    return coups

#Permet de savoir si un joueur remporte la partie
# 1 si le joueur X gagne
# -1 si le joueur O gagne
# 0 si aucun joeur n'a (encore)gagné
def gagner(jeu):
    tab = jeu #inutile
    cvides = 0
    res = ''
    for i in range(0,6):
        for j in range(0,12):
            if(tab[i][j]!=' '):
                if(i>=3):
                    if(j>=2):
                        #diagonale gauche check
                        if(tab[i][j]==tab[i-1][j-1]==tab[i-2][j-2]==tab[i-3][j-3]):
                            res = tab[i][j]
                    #verticale check
                    if(tab[i][j]==tab[i-1][j]==tab[i-2][j]==tab[i-3][j]):
                        res = tab[i][j]
                        
                if(i<3 and j>2):
                    #digonale droite check
                    if(tab[i][j]==tab[i+1][j-1]==tab[i+2][j-2]==tab[i+3][j-3]):
                            res = tab[i][j]
                
                if(j>2):
                    #horizontale check
                    if(tab[i][j]==tab[i][j-1]==tab[i][j-2]==tab[i][j-3]):
                        res = tab[i][j]
            else:
                cvides+=1
        
    if res == 'O':
        return (10000)
    elif res == 'X':
        return (-10000)
    elif cvides == 0:
        return 10
    return (0)
    # s'il y a une combinaison gagnante, le Terminal_Test() retourne 10 000 pour O ou -10 000 pour X
    # s'il n'y a pas de combinaison gagnante, le Terminal-Test() retourne 0
    #retourne 10 si la grille est pleine

def evaluerAttaque(tab, coup):
    ligne = 5
    alignement = [-1,-1,-1,-1]
    distance = [0,0,0,0]
    distTrouv = [False,False,False,False]
    cases = ['O','O','O','O']
    #On cherche la ligne
    for i in range(0,5):
        if (tab[i][coup] == ' ' and tab[i+1][coup] != ' '):
            ligne = i
    
    for i in range(1,4):
        if(ligne<=5-i):
            if(coup>=i):
                #diagonale gauche check
                if(tab[ligne+i][coup-i]=='O'==cases[0]):
                    alignement[0] += 1
                elif(tab[ligne+i][coup-i]=='O' and cases[0]=='X' and distTrouv[0]==False):
                    distance[0] = i
                    distTrouv[0] = True
                else:
                    cases[0]='X'
            #verticale check
            if(tab[ligne+i][coup]=='O'==cases[1]):
                alignement[1] += 1
            elif(tab[ligne+i][coup]=='O' and cases[0]=='X' and distTrouv[0]==False):
                distance[1] = i
                distTrouv[1] = True
            else:
                cases[1]='X'
                
        if(ligne>=i and coup<=11-i):
            #digonale droite check
            if(tab[ligne-i][coup+i]=='O'==cases[2]):
                alignement[2] += 1
            elif(tab[ligne-i][coup+i]=='O' and cases[0]=='X' and distTrouv[0]==False):
                distance[2] = i
                distTrouv[2] = True
            else:
                cases[2]='X'
        
        if(coup>i):
            #horizontale check
            if(tab[ligne][coup-i]=='O'==cases[3]):
                alignement[3] += 1
            elif(tab[ligne][coup-i]=='O' and cases[0]=='X' and distTrouv[0]==False):
                distance[3] = i
                distTrouv[3] = True
            else:
                cases[3]='X'
        
    score = 10**alignement[0] + 10**alignement[1] + 10**alignement[2] + 10**alignement[3]
    for i in range(0,4):
        if(distance[i]!=0):
            score = score + 40/(2**distance[i]) 
    return score

def evaluerDefense(tab, coup):
    ligne = 5
    alignement = [-1,-1,-1,-1]
    cases = ['X','X','X','X']
    #On cherche la ligne
    for i in range(0,5):
        if (tab[i][coup] == ' ' and tab[i+1][coup] != ' '):
            ligne = i
    
    for i in range(1,4):
        if(ligne<=5-i):
            if(coup>=i):
                #diagonale gauche check
                if(tab[ligne+i][coup-i]=='X'==cases[0]):
                    alignement[0] += 1
                else:
                    cases[0]='O'
            #verticale check
            if(tab[ligne+i][coup]=='X'==cases[1]):
                alignement[1] += 1
            else:
                cases[1]='O'
                
        if(ligne>=i and coup<=11-i):
            #digonale droite check
            if(tab[ligne-i][coup+i]=='X'==cases[2]):
                    alignement[2] += 1
            else:
                cases[2]='O'
        
        if(coup>i):
            #horizontale check
            if(tab[ligne][coup-i]=='X'==cases[3]):
                    alignement[3] += 1
            else:
                cases[3]='O'
        
    score = 5*(10**alignement[0] + 10**alignement[1] + 10**alignement[2] + 10**alignement[3])
    return score

#Place un coup dans le jeu à l'emplacement donné, retourne -1 si impossible
def jouer(jeu, joueur, coup):
    for i in range(5,-1,-1):
        if jeu[i][coup] is ' ':
            jeu[i][coup]=joueur
            return jeu


def Mini_Max_Alpha_Beta(s, player,depth,alpha,beta):  
    winner_loser = gagner(s) #utility
    
    if winner_loser != 0 or depth == 5:
        return winner_loser
    
    empty_cells = coupPossible(s)

    if player == 'O':
        value = -math.inf
        for empty_cell in empty_cells:
            new_state = copy_game_state(s)        
            new_state = jouer(new_state, player, empty_cell) #on simule le fait que l'IA joue dans toutes les cases vides
            #on parcourt les options en profondeur   
            value = max(value,Mini_Max_Alpha_Beta(new_state,'X',depth + 1,alpha,beta))
            if value>=beta:
                return value
            alpha = max(alpha,value)
        return value
    
    if player == 'X':
        value = math.inf
        for empty_cell in empty_cells:
            new_state = copy_game_state(s)        
            new_state = jouer(new_state, player, empty_cell) #on simule le fait que l'humain joue dans toutes les cases vides
            #on parcourt les options en profondeur   
            value = min(value,Mini_Max_Alpha_Beta(new_state, 'O', depth + 1,alpha,beta))
            if value<=alpha:
                return value
            beta = min(beta,value)
        return value


def bestMove(jeu):
    depth = 0
    score = 0;
    bestMove = -1
    bestValue = -math.inf
    empty_cells = coupPossible(jeu)
    for empty_cell in empty_cells:
        new_state = copy_game_state(jeu)  
        score = evaluerDefense(new_state, empty_cell)
        score = score + evaluerAttaque(new_state, empty_cell)
        new_state = jouer(new_state, 'O', empty_cell)
        value = Mini_Max_Alpha_Beta(new_state,'X',depth,-math.inf,math.inf)
        value = value + score
        if value>bestValue:
            bestValue = value
            bestMove = empty_cell
    return bestMove


if __name__=='__main__':
    play_again = 'Oui'
    while play_again == 'Oui' :
        game_state = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
        
        print("\nNouvelle partie !")
        Print_board(game_state)
        player_choice = input("Choisir X ou O: ")
        winner = None
        current_state = 0
        while current_state == 0:
            if player_choice == 'X' : # l'humain joue
                case_choice = int(input("Saisir le numéro de la ligne (1 à 12): "))
                game_state = jouer(game_state ,'X', case_choice-1)
                player_choice = 'O'
            else: #l'IA joue
                #case_choice = Mini_Max_Alpha_Beta(game_state, player,alpha,beta)Mini_Max(game_state,depth, 'O')
                case_choice = bestMove(game_state)
                game_state = jouer(game_state ,'O', case_choice)
                player_choice = 'X'
                print("L'IA a joué à la case : ", (case_choice+1))
            
            Print_board(game_state)
            current_state = gagner(game_state)
            if current_state == 1:
                print("Le joueur O a gagné!")
            elif current_state == -1:
                print("Le joueur X a gagné!")
            elif current_state==10:
                print("Grille complète !")
            
        play_again = input('Voulez-vous recommencer ? Oui / Non : ')
        if play_again == 'Non':
            print('Au revoir !')

