

class Artista:
    nome = ""
    rank = ""
    genero = ""
    
    def __init__(self, artistaInfo):
        self.nome = artistaInfo[0]
        self.rank = artistaInfo[1] + "º"
        i = 2
        for entry in artistaInfo:
            while i < len(artistaInfo):
                if i == (len(artistaInfo)-1):
                    self.genero += artistaInfo[i] 
                else:
                    self.genero += artistaInfo[i] + ", "
                i += 1
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
    
    def getGenero(self):
        return self.genero
    
    def setGenero(self, genero):
        contador = 0
        i = 2
        for entry in genero:
            contador += 1
        while (i < contador):
            self.genero += genero[i] + ", "  

        
    #def getTopLyrics(self):
        return self.toplyrics
    
    #def setTopLyrics(self, quantidade):
    
    def getRank(self):
        return self.rank
    
    def setRank(self, rank):
        self.rank = rank
        