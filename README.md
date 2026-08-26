# Gestione di un e-commerce
Applicazione Desktop, sviluppata in Python utilizzando Tkinter, per la gestione di un e-commerce.

## Funzionalità principali
- Gestione anagrafica cliente (inserimento, modifica, eliminazione e ricerca dei dati)
- Gestione anagrafica prodotti (inserimento, modifica, eliminazione e ricerca dei dati)
- Gestione anagrafica degli ordini (inserimento, modifica, eliminazione e ricerca dei dati)
- Visualizzazione grafica dei dati tramite tabelle 
- Analisi KPI con creazione di report Word e grafici
- Salvataggio dei dati nel Database MySQL "ecommerce"
- Salvataggio dei dati in file CSV e JSON
- Esecuzione di backup automatici giornalieri
- Invio automatico di email relative all'esecuzione del backup

## Struttura dei dati 
I dati vengono salvati nel Database ecommerce. 
Successivamente vengono gestiti con DataFrame, file JSON e file CSV.

I Database sono composti come di seguito:
Tabella Clienti  
{id_cliente : nr. identificativo univoco,  
nome : nome,   
cognome : cognome,  
email : email univoca,  
password : password univoca protetta da hash,  
indirizzo_consegna : {via, numero civico, citta, cap, provincia}
}

Tabella Prodotti  
{id_prodotto : nr. identificativo univoco,  
tipo : tipologia,   
categoria : categoria di appartenenza,  
descrizione : caratteristiche specifiche,  
prezzo_unitario : prezzo,  
quantita_magazzino : giacenza in magazzino
}

Tabella Ordini  
{id_ordine : nr. identificativo univoco,  
id_prodotto : identificativo del prodotto,   
id_cliente : identificativo del cliente,
quantita_venduta : quantità,  
importo : prezzo_unitario*quantita_venduta,  
data_ordine : YYYY-MM-DD
}

## Interfaccia principale
La finestra principale (Home) riporta le parti di cui è composto il software, permettendo all'utilizzatore di scegliere la sezione di interesse.  
Sezioni di cui è composto: Clienti, Prodotti, Ordini, Analisi dei dati.

### Sezione Clienti
Permette di:
- Inserire un nuovo cliente
- Modificare i dati di un cliente
- Cancellare un cliente
- Cercare un cliente tramite l'ID
- Visualizzare i dati dei clienti nella tabella
- Esportare i dati in un file CSV 

### Sezione Prodotti
Permette di:
- Inserire un nuovo prodotto
- Modificare i dati di un prodotto
- Esportare i dati in un file CSV 
- Cancellare un prodotto
- Cercare un prodotto tramite l'ID
- Cercare i prodotti di una determinata categoria
- Visualizzare i dati dei prodotti nella tabella

### Sezione Ordini
Permette di:
- Inserire un nuovo ordine
- Modificare i dati di un ordine
- Esportare i dati in un file CSV 
- Cancellare un ordine
- Cercare un ordine tramite l'ID
- Cercare un ordine tramite la data
- Visualizzare gli ordini nella tabella

### Sezione Analisi dati
Permette di:
- Esportare tutti i dati dei clienti, dei prodotti e degli ordini in file CSV
- Visualizzare l'analisi delle vendite e di creare i relativi grafici e il report in word  
- Visualizzare l'analisi dei clienti e di creare i relativi grafici e il report in word  
- Visualizzare l'analisi dei prodotti e di creare i relativi grafici e il report in word
- Creare un report word completo con tutte le analisi
- Calcolare le previsioni di vendita (con il metodo base e il metodo Monte Carlo)

## Regole di business
- Gli ID (clienti, prodotti, ordini) sono sequenziali, univoci e generati automaticamente dal sistema.
Una volta creati non sono modificabili.
- Il prezzo del prodotti non può essere minore di 0.
- La quantità richiesta in ordine non può essere uguale o minore di 0.
- Non è possibile emettere ordini con quantità superiore a quella disponibile a magazzino.
- L'importo totale dell'ordine è calcolato automaticamente dal sistema e non può essere modificato.
- Il magazzino viene aggiornato automaticamente all'emissione di un nuovo ordine o alla modifica di uno esistente.

## Gestione degli errori
#### Connessione a database
In caso di errore di connessione con il database, viene mostrato un messaggio nella GUI. 

#### Clienti
Controllo compilazione dei campi, validazione dell'email e validazione della password (minimo 8 caratteri, almeno un carattere numerico e un carattere speciale).  
Verifica dell'esistenza dell'ID per la modifica, la ricerca e l'eliminazione dei dati.  
Visualizzazione di messaggi specifici in caso di errore.

#### Prodotti
Controllo compilazione dei campi, validazione del prezzo e della quantità.  
Verifica dell'esistenza dell'ID per la modifica, la ricerca e l'eliminazione dei dati.  
Visualizzazione di messaggi specifici in caso di errore.

#### Ordini
Controllo compilazione dei campi, validazione della quantità richiesta e  della relativa disponibilità a magazzino.  
Verifica dell'esistenza dell'ID dei prodotti e dei clienti.   
Verifica dell'esistenza dell'ID dell'ordine per la modifica, la ricerca e l'eliminazione dei dati.  
Visualizzazione di messaggi specifici in caso di errore.

#### Analisi dei dati
Controllo integrità dati e verifica della creazione dei report.   
Visualizzazione di messaggi specifici in caso di errore.

# Requisiti
Utilizzare la seguente versione di Python:
- version 3.13.3

# Avvio applicazione
python main.py oppure py main.py

# Tecnologie utilizzate
- Tkinter
- MySQL
- pathlib
- json, csv, docx
- pandas
- matplotlib
- numpy, sklearn, itertools
- datetime
- schedule
- smtplib
- bcrypt
- dotenv

# Salvataggio dei dati 
- Dati esportati in file csv: verranno salvati nella cartella "report + data di emissione";
- Dati esportati in file json: verranno salvati nella cartella "file_json";
- Elenco clienti, elelnco prodotti e elenco ordini: verranno salvati nelle cartella "dati esportati";
- Report di analisi e grafici: verranno salvati nella cartella "report analisi" e suddivisi in sottocartella in base alla data di creazione.

# File allegati
- Diagramma ER: "e-commerce.drawio"
- Palette colori: "Gestionale e-commerce (palette colori).pdf"
