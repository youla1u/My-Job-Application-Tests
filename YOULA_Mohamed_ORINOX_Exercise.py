# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 16:20:23 2022

@author: YOULA Mohamed
"""

def list_of_Parts_0(EXP, N, SEP):  # cette on retourne une liste initiale à mettre à jour récursivement
    L=[]                                        
    Chars= EXP.split(SEP)
    K, A=Chars[0], Chars[1:]
    l=len(K)
    while A!=[] and l<N:           # tant que la longeur d'une chaine de caractère est strictement        
          K=K+SEP+A[0]             # inférieur à N ajouter les caractères suivantes 
          A.remove(A[0])
          l=len(K)
          
    if SEP in K:                   #############              
       i=K.rindex(SEP)                         #
       C1,C2= K[:i],K[i+1:]                    #
                                               #
       if C1!="":                              #
          L.append(C1)      
       else:                                   #
           L.append(None) 
                                               # ========> Pour obtenir une partie séparée et une nouvelle 
       if A!=[] :
          new_EXP=C2+SEP+SEP.join(A)           #           chaine de charactère à diviser avec le séparateur
       else:
          new_EXP=C2+SEP.join(A)               # 
                                               #
    else:                                      #
        if len(K)<=N:                          #
           L.append(K)                         #
        else:                                  #
           L.append(None)                      #
        new_EXP=SEP.join(A)        #############
        
    L.append(new_EXP)    
    return L                      


def list_of_Parts_1(EXP, N, SEP): # Cette foction permet de mettre à jour la liste retournée précédement 
    M=[]
    D=list_of_Parts_0(EXP, N, SEP)
    if D[1]=="":
       D.remove(D[1]) 
       M.append(D[0])
    else:
        M.append(D[0])
        M.extend(list_of_Parts_1(D[1], N, SEP))
    return M
###################################################################################################################    

def split_into_parts(EXP, N, SEP):     # Enfin, la fonction qui renvoie l'ensemble de l'EXP donné séparé dans une 
    Parts=list_of_Parts_1(EXP, N, SEP) # liste contenant les parties (si possible) ou une liste vide sinon. Elle 
    if None in Parts:                  # dépend des deux fontionts précédentes
       return []
    else: 
        return Parts

