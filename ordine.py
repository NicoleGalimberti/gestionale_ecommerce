class Ordine:
    """
    Questa classe rappresenta l'ordine in un sistema di e-commerce.
    L'Ordine è caratterizzato dagli attributi id ordine, id prodotto, id cliente, quantità venduta, importo, data_ordine. 
    """
    def __init__(self, id_ordine, id_prodotto, id_cliente, quantita_venduta, importo, data_ordine):
        """
        Inizializza un'istanza di un Ordine
        
        Args:
        - id_ordine(int): identificativo univoco dell'ordine
        - id_prodotto(int): identificativo univoco del prodotto venduto
        - id_cliente(int): identificativo univoco del cliente che effettua l'acquisto
         quantita_venduta(int): quantità totale venduta
         importo(float): importo dell'ordine
         data_ordine(str): data dell'ordine, tipo di formato YYYY-MM-DD
        """
        self.__id_ordine = id_ordine
        self.__id_prodotto = id_prodotto
        self.__id_cliente = id_cliente
        self.quantita_venduta = quantita_venduta
        self.importo = importo
        self.data_ordine = data_ordine

    def getid_ordine(self):
        """
        restituisce l'identificativo dell'ordine

        Returns:
        int: id_ordine
        """
        return self.__id_ordine
    
    def getid_prodotto(self):
        """
        restituisce l'identificativo del prodotto

        Returns:
        int: id_prodotto
        """
        return self.__id_prodotto
    
    def getid_cliente(self):
        """
        restituisce l'identificativo del cliente

        Returns:
        int: id_cliente
        """
        return self.__id_cliente
        
    
    def __str__(self):
        return f"{self.__id_ordine}, {self.__id_prodotto}, {self.__id_cliente}, n° {self.quantita_venduta} pezzi venduti, importo € {self.importo}, data {self.data_ordine}"
    def __repr__(self):
        return f"Ordine(id ordine= {self.getid_ordine()}, id prodotto= {self.getid_prodotto()}, id cliente= {self.getid_cliente()}, quantità venduta= {self.quantita_venduta}, importo= {self.importo}, data= {self.data_ordine})"
