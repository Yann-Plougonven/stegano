from PIL import Image

def dissimuler(chemin_hote, chemin_invitee):
    """
    chemin_hote(string) : chemin de l'image hôte
    chemin_invitee(string) : chemin de l'image invitée
    Enregistre l'image résultante sous le nom 'fusion.bmp'
    """
    pass

def fusion_composantes(composante_hote, composante_invitee):
    """
    composante_hote(entier) : composante (R, V ou B)
    composante_invitee(entier) : composante (R, V ou B)
    retourne la composante fusionnée sous forme d'entier 
    """            
    invitee=bin(composante_invitee)[2:] # On enlève 0b
    hote=bin(composante_hote)[2:] # On enlève 0b
    #nbz = nombre de 0 manquants (il faut 8 chiffre)
    nbz = 8 - len(hote) 
    hote = nbz*'0' + hote
    nbz = 8 - len(invitee)
    invitee = nbz*'0' + invitee
    
    fusion = hote[:-2]+invitee[:2] # On remplace les 2 derniers caractères de hote par les 2 premiers de invitee
    return int(fusion,2)
    
    
def reveler(chemin_image):
    """
    chemin_image(string) : chemin de l'image
    sauvegarde l'image sous le nom 'extraction.jpg'
    """
    img = Image.open(chemin_image)
    largeur, hauteur = img.size # on récupère la hauteur et la largeur de l'image
    pixel = img.load()
    newimage = Image.new("RGB", (largeur, hauteur)) #on crée la nouvelle image (on l'enregisre plus tard)
    newpixel = newimage.load() # On load les pixels de la nouvelle image
    
    print("largeur de l'image à réveler =",largeur,"; hauteur =", hauteur)
    for y in range(hauteur):
        for x in range(largeur):
            #print("je suis sur le pixel",x,y)
            r, v, b = pixel[x, y] #on prend la couleur de chaque pixels
            #print(r)
            # On demande à la fonction extraction_composante de nous passer les pixels de l'image à révéler
            r2 = extraction_composante(r)  
            v2 = extraction_composante(v)
            b2 = extraction_composante(b)
            newpixel[x,y]= (r2,b2,b2) # on sauvegarde les nouveux pixels dans la nouvelle image révélée
    newimage.save("extractionhomme.jpg") # on enregiste l'image révélée

def extraction_composante(value):
    """
    Extrait les deux bits de poids faibles de <value>, et les place en bits de poids forts.
    Après test, l'ajout le plus satisfaisant est le suivant:
    On ajoute '100000' (c'est le milieu de 000000 et 111111) après les deux bits de poids fort extraits.
    Retourne un entier.
    """
    value = bin(value)[2:] #on enleve 0b
    #print("1",value)
    nbz = 8 - len(value) #nbz = nombre de 0 manquants (il faut 8 chiffre)
    value = nbz*'0' + value
    #print("2",value)
    value = value[-2:] #on prend les 2 derniers bits
    #print("3",value)
    value = value + '100000' #On ajoute 32 = 100000
    #print("4",value)
    return int(value, 2)

#fusione = fusion_composantes(0, 255)
#extrait = extraction_composante(fusione)
#print(extrait)
reveler("fusionhomme.bmp")