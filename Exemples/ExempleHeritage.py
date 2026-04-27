class Employe:
    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire

    def afficher_infos(self):
        print(f"{self.nom} gagne {self.salaire} €")


class Developpeur(Employe):
    def __init__(self, nom, salaire, langage):
        super().__init__(nom, salaire)
        self.langage = langage

    def afficher_infos(self):
        print(f"{self.nom} est développeur Python et gagne {self.salaire} €")

    def coder(self):
        print(f"{self.nom} code en {self.langage}")


class Manager(Employe):
    def __init__(self, nom, salaire, equipe):
        super().__init__(nom, salaire)
        self.equipe = equipe

    def gerer_equipe(self):
        print(f"{self.nom} gère une équipe de {self.equipe} personnes")