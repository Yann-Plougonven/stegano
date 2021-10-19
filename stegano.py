from PIL import Image 

def dissimuler(chemin_hote, chemin_invitee):
    """
    chemin_hote(string) : chemin de l'image hôte
    chemin_invitee(string) : chemin de l'image invitée (les deux images doivent faire la même taille)
    Enregistre l'image résultante sous le nom 'fusion.bmp'
    """
    # On ouvre les images et on load les pixels
    imgh = Image.open(chemin_hote)
    imgi = Image.open(chemin_invitee)
    pixelh = imgh.load()
    pixeli = imgi.load()
    # on récupère les dimentions des images hote et invitee
    largeurh, hauteurh = imgh.size 
    largeuri, hauteuri = imgi.size
    # interactions avec l'utilisateur
    print("Dissimulation de l'image en cours...")
    if imgh.size != imgi.size:
        print("Erreur ! L'image hote et l'image invitee ne font pas la même taille.")
        exit()
    # On crée la nouvelle image (on l'enregisre plus tard) puis on load les pixels de la nouvelle image
    newimage = Image.new("RGB", (largeurh, hauteurh)) 
    newpixel = newimage.load()
    
    for y in range(hauteurh):
        for x in range(largeurh):
            # On prend la couleur de chaque pixels hote et invitee
            rh, vh, bh = pixelh[x, y] 
            ri, vi, bi = pixeli[x, y] 
            # On demande à fusion_composantes de retourner la valeur de nouveaux pixels
            rf = fusion_composantes(rh,ri)
            vf = fusion_composantes(vh,vi)
            bf = fusion_composantes(bh,bi)
            newpixel[x,y] = (rf,vf,bf) # on sauvegarde les nouveux pixels dans la nouvelle image révélée
    newimage.save("dissimulee.bmp") # on enregiste l'image dissimulée
    print("Dissimulation réussie !")

def fusion_composantes(composante_hote, composante_invitee):
    """
    composante_hote(entier) : composante (R, V ou B)
    composante_invitee(entier) : composante (R, V ou B)
    retourne la composante fusionnée sous forme d'entier 
    """
    # On converti en binaire puis on enlève le 0b au début
    invitee = bin(composante_invitee)[2:] 
    hote = bin(composante_hote)[2:] 
    # nbz = nombre de 0 manquants (il faut 8 chiffre). On fait en sorte qu'il y ait 8 chiffres.
    nbz = 8 - len(hote) 
    hote = nbz*'0' + hote
    nbz = 8 - len(invitee)
    invitee = nbz*'0' + invitee
    # On remplace les 2 derniers caractères de hote par les 2 premiers de invitee
    fusion = hote[:-2]+invitee[:2] 
    return int(fusion,2) # on retourne la valeur de la couleur du pixel fusioné en base 2
    
def reveler(chemin_image):
    """
    chemin_image(string) : chemin de l'image
    sauvegarde l'image sous le nom 'extraction.jpg'
    """
    # On ouvre les images et on load les pixels
    img = Image.open(chemin_image)
    pixel = img.load()
    largeur, hauteur = img.size # on récupère la hauteur et la largeur de l'image
    # On crée la nouvelle image (on l'enregisre plus tard) puis on load les pixels de la nouvelle image
    newimage = Image.new("RGB", (largeur, hauteur))
    newpixel = newimage.load()
    
    print("Revelation de l'image en cours... \nDimentions de l'image à réveler =",largeur,"x", hauteur)
    for y in range(hauteur):
        for x in range(largeur):
            r, v, b = pixel[x, y] #on prend la couleur de chaque pixels
            # On demande à la fonction extraction_composante de nous passer les pixels de l'image à révéler
            rf = extraction_composante(r)  
            vf = extraction_composante(v)
            bf = extraction_composante(b)
            newpixel[x,y] = (rf,vf,bf) # on sauvegarde les nouveux pixels dans la nouvelle image révélée
    newimage.save("extractiondissimullee.jpg") # on enregiste l'image révélée
    print("Révelation réussie !")

def extraction_composante(value):
    """
    Extrait les deux bits de poids faibles de <value>, et les place en bits de poids forts.
    Après test, l'ajout le plus satisfaisant est le suivant:
    On ajoute '100000' (c'est le milieu de 000000 et 111111) après les deux bits de poids fort extraits.
    Retourne un entier.
    """
    value = bin(value)[2:] # on converti en binaire puis on enlève le 0b au début
    # nbz = nombre de 0 manquants (il faut 8 chiffre). On fait en sorte qu'il y ait 8 chiffres.
    nbz = 8 - len(value)
    value = nbz*'0' + value
    value = value[-2:] # on prend les 2 derniers bits de la valeur de la couleur du pixel hote
    value = value + '100000' # on ajoute 32 (la moité) = 100000
    return int(value, 2) # on retourne la valeur de la couleur du pixel extrait en base 2

"""
Fonction pouvant être appellées (décommenter la ligne). Les deux premières servent pour les tests).
Utilisation :
reveler("chemin de l'image fusionnée").
dissimuler("chemin de l'image hote", "chemin de l'image invitée de la même taille que l'hote").
Il faut mettre des .png ou .bmp en entrée (pas .jpg, il y a un canal de transparence en plus).
Dans le programme, les "h" correspondent à "hote", et "i" à "invitee".
"""

#fusione = fusion_composantes(0, 255) # Appel de test
#extrait = extraction_composante(fusione) # Appel de test
reveler("dissimulee.bmp")
dissimuler("hote.jpg", "invite.jpg")