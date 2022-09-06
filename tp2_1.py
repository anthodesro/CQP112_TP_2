print("Anthony Desrochers, Julien Lemieux, Maude Beauregard, Amélie Larcher")
print("\n")
print("-------------------------------------------------------------------")
print("             ** Calcul note d'un étudiant ** ")
print("-------------------------------------------------------------------")
print("Instructions :")
print("Saisir un nombre et taper la touche 'Entrée' pour le suivant.") 
print("À la fin, Tapez le caractère * (et la touche 'Entrée') pour terminer.")
print("Lecture des nombres : ")

# Lecture des entrées et traitement des données : 
lst = []

# Definition de la fonction moyenne
def Moyenne(lst):
        if(len(lst) < 1 ):
            return 0;
        lst.remove(min(lst))
        note_moyenne = sum(lst) / len(lst)
        return note_moyenne

while True:
    string = str(input())
    string = string.replace(",",".")
    try: # On esseye de convertir a un nombre
        nombre = float(string) # string est un nombre 
        if(nombre <0 or nombre >20):
            print(" \nLa valeur doit être comprise entre 0 et 20")
            print("Saisir un nombre ou taper # pour terminer.\n")         
            continue

        lst.append(float(nombre))
 
    except ValueError: # Le texte entré n'est pas un nombre
        if(len(lst) <= 1 ): # Évite les division par zero
             print("Il doit y avoir plus que 1 notes d'entrer")
             print("Entrer une note:\n")
             continue
        else:
             break
        
             
note_moyenne = Moyenne(lst)
if(note_moyenne >=10):
    print("\nRéussite, vous avez une moyenne de", note_moyenne)      
else:
    print("\nÉchec, vous avez une moyenne de", note_moyenne)
