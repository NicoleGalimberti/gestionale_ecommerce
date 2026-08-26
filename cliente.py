class Cliente:
    """
    Questa classe rappresenta un cliente all'interno di un sistema di e-commerce.
    Il cliente è caratterizzato dagli attributi ID cliente, nome, cognome, email, password e indirizzo di consegna (via, numero civico, città, CAP e provincia).
    """
    def __init__(self, id_cliente, nome, cognome, email, password, indirizzo_consegna):
        """
        Inizializza un'istanza di Cliente
        
        Args:
        - id_cliente(int): identificativo univoco del cliente
        - nome(str): nome del cliente
        - cognome(str): cognome del cliente
        - email(str): email di registrazione del cliente
        - password(str): password di registrazione del cliente
        - indirizzo_consegna(str): indirizzo del cliente per la consegna del materiale acquistato
        """
        self.__id_cliente = id_cliente
        self.__nome = nome
        self.__cognome = cognome
        self.__email = email
        self.__password = password
        self.__indirizzo_consegna = indirizzo_consegna

    def getid_cliente(self):
        """
        restituisce l'identificativo del cliente
    
        Returns:
        int: id_cliente
        """
        return self.__id_cliente
    
    def getNome(self):
        """
        restituisce il nome del cliente
        
        Returns:
        str: nome
        """
        return self.__nome
    def setNome(self, nome):
        """
        modifica il nome del cliente
        
        Args:
        nome(str): nome del cliente
        """
        self.__nome = nome
    
    def getCognome(self):
        """
        restituisce il cognome del cliente
        
        Returns:
        str: cognome
        """
        return self.__cognome
    def setCognome(self, cognome):
        """
        modifica il cognome del cliente
        
        Args:
        cognome(str): cognome  del cliente
        """
        self.__cognome = cognome

    def getEmail(self):
        """
        restituisce l'email del cliente

        Returns:
        str: email
        """
        return self.__email
    def setEmail(self, email):
        """
        modifica l'email del cliente

        Args:
        email(str): email del cliente
        """
        self.__email = email

    def getPassword(self):
        """
        restituisce la password del cliente

        Returns:
        str: password
        """
        return self.__password
    def setPassword(self, password):
        """
        modifica la password del cliente

        Args:
        password(str): password del cliente
        """
        self.__password = password    

    def getIndirizzo_consegna(self):
        """
        restituisce l'indirizzo di consegna 

        Returns:
        str: indirizzo_consegna
        """
        return self.__indirizzo_consegna 
    def setIndirizzo_consegna(self, indirizzo_consegna):
        """
        modifica l'indirizzo di consegna del cliente

        Args:
        indirizzo_consegna(str): indirizzo di consegna del cliente
        """
        self.__indirizzo_consegna = indirizzo_consegna

    def __str__(self):
        return f"{self.getid_cliente()}, {self.getNome()}, {self.getCognome()}, {self.getEmail()}, {self.getPassword()}, {self.getIndirizzo_consegna()}"
    def __repr__(self):
        return f"Cliente(id cliente= {self.getid_cliente()}, nome='{self.getNome()}', cognome={self.getCognome()}, email={self.getEmail()}, password={self.getPassword()}, indirizzo_consegna={self.getIndirizzo_consegna()})"
    
