candidats = ['albert','emilie','oscar','marine','max']
 
vote = [
   {'nb':3273,'rang':[1,5,4,2,3]},
   {'nb':2182,'rang':[5,1,4,3,2]},
   {'nb':1818,'rang':[5,2,1,4,3]},
   {'nb':1636,'rang':[5,4,2,1,3]},
   {'nb':727,'rang':[5,2,4,3,1]},
   {'nb':364,'rang':[5,4,2,3,1]}
 ]

 
def un_tour(votes):
   scores = [0,0,0,0,0] #initialise les scores des candidats a 0
   for vote in votes:
      nb= vote['nb'] #nombre de votes pour le candidat
      r= vote ['rang'] #classement des votes 
      for i in range ( len ( candidats)): 
         if r[i]==1: # si en parcourant le tableau 
            scores[i]=scores[i]+ nb
   maxi=scores[0]
   ind_gagnant = 0
   for i in range (1,len(scores)):
      if scores [i]>maxi:
         maxi=scores[i]
         ind_gagnant=i
   print("un tour-->gagnant:",candidats[ind_gagnant],"scores:",scores)
   return ind_gagnant, scores 



def condorcet(votes):
   n=len(candidats)
   duels= [[0]*n for i in range (n)] # tableau des duels 
   #on remplit le tableau des duels 
   for vote in votes:
      nb=vote['nb'] # nb électeurs 
      r=vote['rang'] # classement 
      for i in range (n):
         for j in range (n):
            if r[i]<r[j]: # si le candidat i est préféré à j
               duels [i][j]= duels [i][j]+nb
   #on cherche un gagnant
   for i in range (n):
      gagnant=True 
      for j in range (n):
         if i!=j: # on compare pas le même candidat 
            if duels [i][j]<= duels [j][i]:
               gagnant=False 
               break
      if gagnant:
         print ("Condorcet->gagnant:",candidats[i])
         return i
      else :
         print ("Condorcet->pas de vainqueur")
         return None
 

condorcet(vote)
def deux_tour():
   scores = [0,0,0,0,0] #initialise les scores des candidats a 0
   for vote in votes:
      nb= vote['nb'] #nombre de votes pour le candidat
      r= vote ['rang'] #classement des votes 
      for i in range ( len ( candidats)): 
         if r[i]==1: # si en parcourant le tableau 
            scores[i]=scores[i]+ nb
            break
   
   
   
   
   
   
   
   
   return "candidats gagnant"


def lastman_standing():
   return "candidats gagnant"
 



def borda():
   return "candidats gagnant" 

