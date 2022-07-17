# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:59:27 2022

@author: YOULA Mohamed
"""
# 1) Ccette fonction retourne le maximum entre deux nombres
def maximum_numbers(a,b):
   if a < b :
      return b
   else:
      return a 
  
    
# 2)  Cette fonction affiche un message selon qu'un nombre est divible par 3 et/ou 5 ou non
def fozz_bezz(N):
    
    if (N % 3==0 and N % 5==0):
       return("FozzBezz")
       
    elif N % 3==0 :
       return("Fozz")
       
    elif  N % 5==0:
       return("Bezz")
    
    else:
        return N
    
    
# 3) Cette fonction verifie si une vitesse est valide ou non
def check_speed(speed):
    if speed < 80:
        print('Ok')
    else:
        points = (speed + 8 - 80)// 4
        print(str(points))
        if points > 12:
            print('License suspended')
       
        
# 4) Cette fonction montre si un nombre inférieur ou égale à une limite est pair ou impair 
def showNumbers(limit):
    for n in range(limit+1):
        if n % 2 == 0:
           print(str(n)+' '+"EVEN")
        else:
           print(str(n)+' '+"ODD")  
     

#5) S'ils existent au moins un multiple de 3 qui est <=  à limit et
#   au moins un multiple de 5 qui est <=  à limit cette fonction 
#   retoune la somme de ces multiples <= à limit.   
def sum_multiples_3_5(limit):
    a=3
    b=5
    l=[]
    if a <= limit and b <= limit:
       m=min(a,b)        
       for n in range(m,limit+1):
           if n % a ==0 or n % b ==0:
             l.append(n)
       return sum(l)         
    else:
        if a > limit and b > limit: 
           print(str(a)+' and '+str(b)+" have no multiple less than "+str(limit)) 
        elif a > limit:
           print(str(a)+" have no multiple less than "+str(limit))
           
        elif b > limit:
           print(str(b)+" have no multiple less than "+str(limit))
        
                  
#6) Cette fonction affiche une suite '*' selon le numéro de ligne inférieur ou égale à 'rows'                     
def show_stars(rows):
    for r in range(1,rows+1):
        print('*'*r)
        

        
#7) Cette fonction retoune la liste des dess nombres premiers <= à une limite         
def prime_numbers(limit):
    L=[]
    for x in range(limit+1):
        l=[]
        for i in range(2, x-1):
            if x % i == 0:
               l.append(i)
               break 
        if len(l)==0:
           L.append(x)
           P=L[2:]
    print(P)       
               
        

         


     
        
        
        
        
        
        
        
        
        
        
        
        
        