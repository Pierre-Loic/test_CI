from math import pi, sqrt
import requests

def exercice_1(a, b):
    """
    Ecrire une fonction qui renvoie le produit des deux élèments
    a et b
    """
    if isinstance(a, int) and isinstance(b, int):
        return a*b
    else:
        raise TypeError

def exercice_2(x, a, b):
    """
    Ecrire une fonction qui renvoie :
        -255 si x<a
        x si a<=x<=b
        255 si x>b
    (A faire en TDD)
    """
    if isinstance(a, int) and isinstance(b, int) and isinstance(x, int):
        if x<a:
            return -255
        elif x>b:
            return 255
        else:
            return x
    else:
        raise TypeError

class Exercice_3:
    """
    Ecrire une classe qui renvoie des informations sur un cercle
    """
    def __init__(self):
        print("Début de l'exercice 3")
    
    def r_num(self, r):
        if isinstance(r, int) or isinstance(r, float):
            if r>=0:
                self.r = r
            else:
                raise ValueError
        else:
            raise TypeError

    def aire(self, r):
        """
        Ecrire une fonction qui renvoie l'aire d'un disque de rayon r
        """
        self.r_num(r)
        return self.r**2 * pi

    def perimetre(self, r):
        """
        Ecrire une fonction qui renvoie le perimètre d'un cercle de rayon r
        """
        self.r_num(r)
        return 2*pi*self.r

    def dans_cercle(self, r, x, y):
        """
        Ecrire une fonction qui renvoie True si le point (x, y) est dans
        le cercle de r et de centre (0, 0)
        """
        self.r_num(r)
        valid = (isinstance(x, int) or isinstance(x, float)) and \
                (isinstance(y, int) or isinstance(y, float))
        if valid:
            if sqrt(x**2+y**2)<self.r:
                return True
            else:
                return False
        else:
            raise TypeError

class Exercice_4:
    """
    Ecrire une classe qui renvoie des informations sur un lieu
    """
    def __init__(self, lieu):
        # Appel API Wikipedia
        self.lieu = lieu
        url = "https://fr.wikipedia.org/w/api.php"
        par = {
                "search": lieu,
                "format": "json",
                "action": "opensearch",
              }
        self.req = requests.get(url, params=par).text
        #self.req = self.req.json()
    
    def loc(self):
        """
        Ecrire une fonction qui renvoie les informations
        """
        return f"Voici ce que je connais de {self.lieu} : {self.req[2][0]}"

if __name__=="__main__":
    ex = Exercice_4("Paris")
    print(ex.loc())
