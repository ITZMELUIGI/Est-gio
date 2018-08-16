

class Albums:
    nomeAno = []

    def __init__(self, albumsInfo):
        self.nomeAno = albumsInfo
    
    
    def getNomeAno(self, i):
        return self.nomeAno[i]
    
    def setNomeANO(self, albumsInfo):
        self.nomeAno = []
        self.nomeAno = albumsInfo