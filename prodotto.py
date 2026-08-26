class Prodotto:
    """
    Questa classe rappresenta un Prodotto all'interno di un sistema gestionale di un e-commerce.
    Il Prodotto è caratterizzato dagli attributi id prodotto, tipo, categoria, descrizione, prezzo unitario e quantità magazzino.
    """
    def __init__(self, id_prodotto, categoria, tipo, descrizione, prezzo_unitario, quantita_magazzino):
        """
        Inizializza un'istanza di Prodotto
        
        Args:
        - id_prodotto(int): identificativo univoco del prodotto
         categoria(str): categoria di appartenenza del prodotto
         tipo(str): tipo di prodotto
         descrizione(str): caratteristiche del prodotto
         prezzo_unitario(float): prezzo della singola unità
         quantita_magazzino(int): quantità totale del prodotto disponibile a magazzino
        """
        self.__id_prodotto = id_prodotto
        self.tipo = tipo
        self.categoria = categoria
        self.descrizione = descrizione
        self.prezzo_unitario = prezzo_unitario
        self.quantita_magazzino = quantita_magazzino

    def getid_prodotto(self):
        """
        restituisce l'identificativo del prodotto
        """
        return self.__id_prodotto
    
    def descr(self):
        """
        visualizza la descrizione del prodotto registrato a gestionale

        Returns:
        str: id_prodotto, categoria, tipo, descrizione, prezzo_unitario, quatita_magazzino
        """
        return f"{self.getid_prodotto()}, {self.categoria}, {self.tipo}, {self.descrizione}, {self.prezzo_unitario}, {self.quantita_magazzino}"

    def __str__(self):
        return f"{self.__id_prodotto}, {self.categoria}, {self.tipo}, {self.descrizione}, € {self.prezzo_unitario}, n° {self.quantita_magazzino} pezzi"
    def __repr__(self):
        return f"Prodotto(id prodotto= {self.getid_prodotto()}, categoria= {self.categoria}, tipo= {self.tipo}, descrizione= {self.descrizione}, prezzo_unitario= {self.prezzo_unitario}, quantita_magazzino= {self.quantita_magazzino})"