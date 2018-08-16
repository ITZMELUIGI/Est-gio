import requests
import urllib.parse

class API:
    api_vagalume = '60c175766f587c586a7ba82a696b771344cfe274'
    main_url = 'http://www.vagalume.com.br'
    artistaUrl = ""
    art_url = 'http://api.vagalume.com.br/search.art?'
    jsonNomes = []
    jsonLista = []
    jsonData2 = []
    
    def api_request(self, artista_nome):
        if artista_nome != "":  
            self.jsonNomes = []
            url = API.art_url + urllib.parse.urlencode({'q': artista_nome})
            self.contador = 0           
            
            self.json_data = requests.get(url).json() #So this is where you present search results.
            if self.json_data['response']['numFound'] != 0:
                while (self.contador < self.json_data['response']['numFound']):
                    if self.contador > 4:
                        self.contador = self.json_data['response']['numFound'] + 10
                    else:                        
                        self.jsonNomes.append(self.json_data['response']['docs'][self.contador]['band']) #Id of item selected.
                        self.contador += 1 
        return self.jsonNomes
    
    def apiConnect(self, artista_nome):
        self.main_url = 'http://www.vagalume.com.br'
        self.art_url = 'http://api.vagalume.com.br/search.art?'
        
        self.jsonLista = []
        url = API.art_url + urllib.parse.urlencode({'q': artista_nome}) 
            
        
        self.json_data = requests.get(url).json()
        self.artistaUrl = self.main_url + self.json_data['response']['docs'][0]['url'] + "index.js"
        self.json_data2 = requests.get(self.artistaUrl).json()
    
    def api_artista(self, artista_nome):
        API.apiConnect(artista_nome)
        self.contador = 0  
        
        self.jsonLista.append(self.json_data2['artist']['desc'])
        self.jsonLista.append(self.json_data2['artist']['rank']['pos'])
        
        self.listaContador = list(self.json_data2['artist'].keys())
        for entry in self.listaContador:
            if "genre" in entry.strip():
                for entry in self.json_data2['artist']['genre']:
                    self.jsonLista.append(self.json_data2['artist']['genre'][self.contador]['name'])
                    self.contador += 1
        if self.contador == 0:
            self.jsonLista.append("Não possui estilos definidos.")

        return self.jsonLista
    
    def api_album(self, artista_nome):
        API.apiConnect(artista_nome)
        self.contador = 0
        
        self.listaContador = list(self.json_data2['artist'])
        for entry in self.listaContador:
            if "albums" in entry.strip():
                for entry in self.json_data2['artist']['albums']['item']:
                    self.jsonLista.append(self.json_data2['artist']['albums']['item'][self.contador]['desc'] + ", " + self.json_data2['artist']['albums']['item'][self.contador]['year'])
                    self.contador += 1
        if(self.contador == 0):
            self.jsonLista.append("Não possui álbuns.")

        return self.jsonLista
    
    def api_toplyrics(self, artista_nome, quantidade):
        API.apiConnect(artista_nome) 
        self.contador = 0
        
        for entry in self.json_data2['artist']['toplyrics']['item']:             
           self.jsonLista.append(self.json_data2['artist']['toplyrics']['item'][self.contador]['desc'])
           self.contador += 1
           if self.contador == quantidade or self.contador > quantidade:
              return self.jsonLista
          
    def api_toplyricsUpdate(self, quantidade):
        self.json_data2 = requests.get(self.artistaUrl).json() 
        self.contador = 0
        
        for entry in self.json_data2['artist']['toplyrics']['item']:             
           self.jsonLista.append(self.json_data2['artist']['toplyrics']['item'][self.contador]['desc'])
           self.contador += 1
           if self.contador == quantidade:
              return self.jsonLista
        

        

API = API()
API.api_toplyrics("Ed Sheeran",7)

