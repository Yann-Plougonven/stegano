import unittest
import stegano

class SteganoTest(unittest.TestCase):
    """
    A class to test the stegano module
    """
    # (hote, invite, fusion)
    
    def test_fusion_composantes(self):
        """
        Vérifie si la fusion de deux composantes fonctionne
        """
        datas = ( (0, 0, 0),
                  (255, 0, 252), 
                  (0, 255, 3), 
                  (255, 255, 255), 
                  (4, 192, 7), 
            )
        for data in datas:
            composante_hote, composante_invitee,  result_attendu = data
            result = stegano.fusion_composantes(composante_hote, composante_invitee)
            self.assertEqual(result, result_attendu, f"Le résultat de la fusion {composante_invitee} dans {composante_hote} devrait être {result_attendu} mais c'est {result}.")

    def test_extraction_composante(self):
        """
        Vérifie si l'extraction fonctionne
        """
        datas = (
                 (129, 96),
                 (131, 224),
                 (0, 32),
                 (1, 96),
                 )
        for data in datas:
            valeur, resultat_attentu = data
            result = stegano.extraction_composante(valeur)
            self.assertEqual(result, resultat_attentu, f"Le résultat de l'extraction {valeur} devrait être {resultat_attentu} mais c'est {result}.")        
        


if __name__ == '__main__':
    unittest.main()        