from tkinter import *
from AutocompleteEntry import AutocompleteEntry as AE
from API import API
from Artista import Artista as Art
from Albums import Albums as Alb
from Toplyrics import Toplyrics as TL
import ctypes

class GUI:
    def __init__(self, master):
        self.master = master
        
        
        self.lblArtista = Label(self.master, text = "Artista: ")
        self.lblArtista.grid(row = 0, columnspan = 2)
        
        self.lblInfo = Label(self.master, text = "*Com maiúsculas", font = ("Arial", 8))
        self.lblInfo.grid(row = 1, column = 0, columnspan = 2)
        
        self.lblNomeArtista = Label(self.master, text = "<NOME DO ARTISTA>", font = ("Arial", 20))
        self.lblNomeArtista.grid(row = 10, column = 0, columnspan = 4, sticky = "w")
        self.lblNomeArtista.grid_remove()
        
        self.lblRank = Label(self.master, text = "<RANK DO ARTISTA>", font = ("Arial", 10))
        self.lblRank.grid(row = 11, column = 0, columnspan = 3, sticky = "w")
        self.lblRank.grid_remove()
        
        self.lblUltimaM1 = Label(self.master, text = "Mostrando as", font = ("Arial", 10))
        self.lblUltimaM1.grid(row = 11, column = 4)
        self.lblUltimaM1.grid_remove()
        
        self.lblUltimaM2 = Label(self.master, text = "músicas mais acessadas.", font = ("Arial", 10))
        self.lblUltimaM2.grid(row = 11, column = 6, columnspan = 3)
        self.lblUltimaM2.grid_remove()
        
        self.lblGenero = Label(self.master, text = "<GÊNERO>", font = ("Arial", 10))
        self.lblGenero.grid(row = 12, column = 0, columnspan = 3, sticky = "w")
        self.lblGenero.grid_remove()
        
        self.lblUltimoA = Label(self.master, text = "<ÚLTIMO ÁLBUM>", font = ("Arial", 10))
        self.lblUltimoA.grid(row = 13, column = 0, columnspan = 3, sticky = "w")
        self.lblUltimoA.grid_remove()
        
        self.lblPalavras = Label(self.master, text = "Palavras mais frequentes: ")
        self.lblPalavras.grid(row = 25, column = 4, columnspan = 3)
        self.lblPalavras.grid_remove()

        self.lblPFrequentes = Label(self.master, text = "<PALAVRAS FREQUENTES>")
        self.lblPFrequentes.grid(row = 25, column = 7)
        self.lblPFrequentes.grid_remove()
        
        self.lblESPACO = Label(self.master)
        self.lblESPACO.grid(row = 9, column = 5, rowspan = 3)
        
        self.txtUltimaM = Entry(self.master, width = 5)
        self.txtUltimaM.grid(row = 11, column = 5)
        self.txtUltimaM.bind("<KeyRelease>", self.updateMusicas)
        self.txtUltimaM.grid_remove()
        
        self.lstMusicas = Listbox(self.master, height = 10)
        self.lstMusicas.grid(row = 12, column = 4, columnspan = 3, rowspan = 10)
        self.lstMusicas.grid_remove()
        
        self.btnPesquisar = Button(self.master, text = "Buscar")
        self.btnPesquisar.grid(row = 0, column = 5)
        self.btnPesquisar.bind("<Button-1>", self.carregarArtista)
        
        self.txtArtista = AE(self.master, width = 50)
        self.OPTIONS = []
        self.txtArtista.build(self.OPTIONS, no_results_message = "< No results founds for {} >", case_sensitive = "true")
        self.txtArtista.grid(row = 0, column = 2, columnspan = 3)    
 
        
    def carregarArtista (self, event):
        self.lstMusicas.delete(0, END)
        self.txtUltimaM.delete(0, END)
        if (self.txtArtista.get().strip() == ""):
            ctypes.windll.user32.MessageBoxW(0, "Digite o nome de um artista para pesquisar!", "Atenção", 0)
        else:
            """Informações do Artista: Nome, Rank e Generos (se houver). """
            infoArtista = API.api_artista(self.txtArtista.get())
            print(infoArtista)
            Artista = Art(infoArtista)
            
            self.lblNomeArtista.config(text = Artista.getNome())
            self.lblRank.config(text = "Rank Vagalume: " + Artista.getRank())
            self.lblGenero.config(text = "Estilo(s): " + Artista.getGenero())
            
            self.lblNomeArtista.grid()
            self.lblGenero.grid()
            self.lblRank.grid()
            
            """Informações dos álbums: Nome(se houver) e ano. """
            infoAlbum = API.api_album(self.txtArtista.get())
            Album = Alb(infoAlbum)
            ultimoAlbum = Alb.getNomeAno(Album, 0)
            
            self.lblUltimoA.config(text = "Último álbum: " + ultimoAlbum )
            self.lblUltimoA.grid()
            
            
            infoMusicas = API.api_toplyrics(self.txtArtista.get(), 10)
            toplyrics = TL(infoMusicas)
            i = 0
            while i < 10:
                self.lstMusicas.insert(END, TL.getNome(toplyrics, i))
                i += 1
            self.lstMusicas.grid()
            self.lblUltimaM1.grid()
            self.lblUltimaM2.grid()
            self.txtUltimaM.insert(0, "10")
            self.txtUltimaM.grid()
            
    
    def updateMusicas(self, event):
        artista = Art.getNome(Art)
        if self.txtUltimaM.get() == "" :
            quantidade = 0
        else:
            quantidade = int(self.txtUltimaM.get())
        infoMusicas = API.api_toplyricsUpdate(quantidade)
        toplyrics = TL(infoMusicas)
        self.lstMusicas.delete(0, END)
        i = 0
        while i < int(self.txtUltimaM.get()):
            self.lstMusicas.insert(END, TL.getNome(toplyrics, i))
            i += 1
        
        
        
        
root = Tk()
root.geometry("640x380")
G = GUI(root)
root.mainloop()