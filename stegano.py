from PIL import Image


def dissimuler(chemin_hote, chemin_invitee):
    """
    chemin_hote (string) : chemin de l'image hôte, dans laquelle sera dissimulée l'image invitee.
    chemin_invitee (string) : chemin de l'image invitée
    L'image hote et l'image invitee doivent avoir la même taille (la même définition)
    Enregistre l'image résultante sous le nom 'image_fusionnee.bmp'
    """
    # On ouvre les images et on load les pixels
    imgh = Image.open(chemin_hote)
    imgi = Image.open(chemin_invitee)
    pixelh = imgh.load()
    pixeli = imgi.load()
    # on récupère les dimensions des images hote (h) et invitee (i)
    largeurh, hauteurh = imgh.size
    largeuri, hauteuri = imgi.size
    # interactions avec l'utilisateur
    print("Dissimulation de l'image en cours...")
    if imgh.size != imgi.size:
        print("Erreur ! L'image hote et l'image invitee ne font pas la même taille.")
        exit()
    # On crée la nouvelle image (on l'enregistrera plus tard) puis on load les pixels de la nouvelle image
    newimage = Image.new("RGB", (largeurh, hauteurh))
    newpixel = newimage.load()

    for y in range(hauteurh):
        for x in range(largeurh):
            # On prend la couleur de chaque pixel de l'hote et de l'invitee
            rh, vh, bh = pixelh[x, y]
            ri, vi, bi = pixeli[x, y]
            # On demande à fusion_composantes de retourner la valeur de nouveaux pixels
            rf = fusion_composantes(rh,ri)
            vf = fusion_composantes(vh,vi)
            bf = fusion_composantes(bh,bi)
            newpixel[x,y] = (rf,vf,bf) # on sauvegarde les nouveaux pixels dans la nouvelle image révélée
    newimage.save("image_fusionnee.bmp") # on enregistre l'image dissimulée
    print("Dissimulation réussie !\nL'image fusionnée a été créée avec le nom \"image_fusionee.bmp\".")
    print("Note : vous pouvez maintenant utiliser le programme pour révéler l'image cachée dans 'image_fusionee.bmp'")


def fusion_composantes(composante_hote, composante_invitee):
    """
    composante_hote (entier) : composante (R, V ou B)
    composante_invitee (entier) : composante (R, V ou B)
    retourne la composante fusionnée sous forme d'entier 
    """
    # On convertit en binaire puis on enlève le 0b au début
    invitee = bin(composante_invitee)[2:]
    hote = bin(composante_hote)[2:]
    # nbz = nombre de 0 manquants (il faut 8 chiffre). On fait en sorte qu'il y ait 8 chiffres.
    nbz = 8 - len(hote)
    hote = nbz*'0' + hote
    nbz = 8 - len(invitee)
    invitee = nbz*'0' + invitee
    # On remplace les 2 derniers caractères de hote par les 2 premiers de invitee
    fusion = hote[:-2]+invitee[:2]
    return int(fusion, 2)  # on retourne la valeur de la couleur du pixel fusionné en base 2


def reveler(chemin_image):
    """
    chemin_image(string) : chemin de l'image hôte
    sauvegarde l'image qui était cachée sous le nom 'image_dissimulee.jpg'
    """
    # On ouvre les images et on load les pixels
    img = Image.open(chemin_image)
    pixel = img.load()
    largeur, hauteur = img.size # on récupère la hauteur et la largeur de l'image
    # On crée la nouvelle image (on l'enregistrera plus tard) puis on load les pixels de la nouvelle image
    newimage = Image.new("RGB", (largeur, hauteur))
    newpixel = newimage.load()

    print("Revelation de l'image en cours...")
    for y in range(hauteur):
        for x in range(largeur):
            r, v, b = pixel[x, y] # on prend la couleur de chaque pixel
            # On demande à la fonction extraction_composante de nous passer les pixels de l'image à révéler
            rf = extraction_composante(r)
            vf = extraction_composante(v)
            bf = extraction_composante(b)
            newpixel[x,y] = (rf,vf,bf) # on sauvegarde les nouveaux pixels dans la nouvelle image révélée
    newimage.save("image_dissimulee.jpg") # on enregistre l'image révélée
    print("Révelation réussie !\nL'image qui était cachée a été créée avec le nom \"image_dissimulee.jpg\".")


def extraction_composante(value):
    """
    Extrait les deux bits de poids faibles de <value>, et les place en bits de poids forts.
    Après test, l'ajout le plus satisfaisant est le suivant:
    On ajoute '100000' (c'est le milieu de 000000 et 111111) après les deux bits de poids fort extraits.
    Retourne un entier.
    """
    value = bin(value)[2:] # on convertit en binaire puis on enlève le 0b au début
    # nbz = nombre de 0 manquants (il faut 8 chiffre). On fait en sorte qu'il y ait 8 chiffres.
    nbz = 8 - len(value)
    value = nbz*'0' + value
    value = value[-2:] # on prend les 2 derniers bits de la valeur de la couleur du pixel hote
    value = value + '100000' # on ajoute 32 (la moité) = 100000
    return int(value, 2) # on retourne la valeur de la couleur du pixel extrait en base 2


def lancer_le_programme():
    """
    Demande à l'utilisateur ce qu'il veut faire, et avec quelle(s) image(s).
    Appelle la fonction associée à la demande de l'utilisateur
    """
    print("\nTapez le chiffre '1' puis appuyez sur la touche 'Entrer' si vous souhaitez dissimuler une image dans une autre.")
    print("Tapez le chiffre '2' puis appuyez sur la touche 'Entrer' si vous souhaitez révéler une image déjà dissimulée dans une autre.")
    choix = input("Que souhaitez vous faire ? :")
    if choix == '1':
        img_hote = input("Saisissez le nom (par exemple 'exemple_hote.jpg') de l'image dans laquelle sera cachée l'image à dissimuler :")
        img_invitee = input("Saisissez le nom (par exemple 'exemple_invitee.jpg') de l'image à dissimuler :")
        dissimuler(img_hote, img_invitee)
    elif choix == '2':
        img_fusionee = input("Saisissez le nom (par exemple 'image_fusionnee.bmp') de l'image dans laquelle se cache une autre :")
        reveler(img_fusionee)
    else:
        print("Erreur ! Relancez le programme puis tapez le chiffre « 1 » ou « 2 », sans les guillemets")


# fusionnee = fusion_composantes(0, 255)  # Appel de test
# extrait = extraction_composante(fusionnee)  # Appel de test
lancer_le_programme()
