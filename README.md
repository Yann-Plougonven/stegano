# Stegano
Ce programme de stéganographie permet de dissimuler une image dans les 2 bits de poids faible des pixels d'une autre, et de réveler l'image dissimulée. 

Il s'agit d'un exercice réalisé en cours de NSI, en octobre 2021, pendant l'année de première. Le fonctionnement ce programme n'est pas optimal.

La création de ce readme et d'autres légers changements ont été effectué en novembre 2022.

## Utilisation du programme stegano.py
* La librairie PIL doit être installée.
* Les images que vous souhaitez utiliser dans ce programme doivent être présentes dans le même dossier que le ficher "stegano.py".
* Les formats d'image .jpg et .bmp sont acceptés. Le format png n'est pas accepté car il possède un canal de couleur supplémentaire, pour la transparence.
* L'image hôte et l'image invitée, utilisées pour la dissimulation, doivent faire la même taille (la même définition).

Des images d'exemples, utiles pour tester le programme, sont présentes dans ce dépôt. Vous pouvez également utiliser vos propres images. 
