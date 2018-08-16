

class Toplyrics:
    nome = []
    
    def __init__(self, infoMusicas):
        self.nome = infoMusicas

    
    def getNome(self, i):
        return self.nome[i]
    
    def setNome(self, infoMusicas):
        self.nome = infoMusicas