class Personne:
    def _init_(self, cin="", nom="", prenom="", dateNaissance=""):
        self.cin = cin
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance

    def get_cin(self):
        return self.cin

    def set_cin(self, cin):
        self.cin = cin

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def get_dateNaissance(self):
        return self.dateNaissance

    def set_dateNaissance(self, dateNaissance):
        self.dateNaissance = dateNaissance

    def toString(self):
        return f"CIN: {self.cin}, Nom: {self.nom}, Prénom: {self.prenom}, Date de Naissance: {self.dateNaissance}"


class Stagiaire(Personne):
    num_inscription = 0

    def _init_(self, cin="", nom="", prenom="", dateNaissance=""):
        super()._init_(cin, nom, prenom, dateNaissance)
        Stagiaire.num_inscription += 1
        self.numeroInscription = Stagiaire.num_inscription

    def toString(self):
        return f"{super().toString()}, Numéro d'Inscription: {self.numeroInscription}"


# Exemple d'utilisation :
personne1 = Personne("123", "Doe", "John", "01/01/2000")
print(personne1.toString())

stagiaire1 = Stagiaire("456", "Smith", "Alice", "15/06/1999")
print(stagiaire1.toString())