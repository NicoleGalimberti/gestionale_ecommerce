# Gestionale e-commerce
Applicazione Desktop, sviluppata in Python utilizzando Tkinter, per la gestione di un e-commerce.

## Funzionalità principali
- Gestione anagrafica cliente (inserimento, modifica, eliminazione e ricerca dati tramite ID)
- Gestione anagrafica prodotti (inserimento, modifica, eliminazione e ricerca dati tramite ID)
- Gestione anagrafica degli ordini (inserimento, modifica, eliminazione e ricerca dati tramite ID)
- Visualizzazione grafica dei dati tramite tabelle 
- Analisi KPI con creazione di report Word e grafici
- Salvataggio dei dati nel database MySQL "ecommerce"
- Salvataggio dei dati in file CSV e JSON
- Esecuzione di backup automatici giornalieri
- Invio automatico di email relative all'esecuzione del backup

## Struttura dei dati 
I dati vengono salvati nel database ecommerce. 
Successivamente vengono gestiti con DataFrame, file JSON e file CSV.

Il database è composto dalle seguenti tabelle:
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

La tabella Ordini è collegata a quella Clienti e Prodotti tramite i rispettivi identificativi.

## Interfaccia principale
La finestra principale (Home) mostra le sezioni che compongono il software e consente all'utente di scegliere quella di interesse.

Le sezioni disponibili sono: Clienti, Prodotti, Ordini, Analisi dei dati.

### Sezione Clienti
Permette di:
- Inserire un nuovo cliente
- Modificare i dati di un cliente
- Eliminare un cliente
- Cercare un cliente tramite l'ID
- Visualizzare i dati dei clienti nella tabella
- Esportare i dati in un file CSV 

### Sezione Prodotti
Permette di:
- Inserire un nuovo prodotto
- Modificare i dati di un prodotto
- Esportare i dati in un file CSV 
- Eliminare un prodotto
- Cercare un prodotto tramite l'ID
- Cercare i prodotti appartenenti a una determinata categoria
- Visualizzare i dati dei prodotti nella tabella

### Sezione Ordini
Permette di:
- Inserire un nuovo ordine
- Modificare i dati di un ordine
- Esportare i dati in un file CSV 
- Eliminare un ordine
- Cercare un ordine tramite l'ID
- Cercare un ordine tramite la data
- Visualizzare gli ordini nella tabella

### Sezione Analisi dati
Permette di:
- Esportare tutti i dati dei clienti, dei prodotti e degli ordini in file CSV
- Visualizzare l'analisi delle vendite e di creare i relativi grafici e il report word  
- Visualizzare l'analisi dei clienti e di creare i relativi grafici e il report word  
- Visualizzare l'analisi dei prodotti e di creare i relativi grafici e il report word
- Creare un report word completo contenente tutte le analisi
- Calcolare le previsioni di vendita utilizzando il metodo base e il metodo Monte Carlo

## Regole di business
- Gli id clienti, prodotti, ordini sono sequenziali, univoci e generati automaticamente dal sistema, una volta creati non possono essere modificati.
- Il prezzo del prodotto non può essere minore di 0.
- La quantità richiesta in ordine deve essere maggiore di 0.
- Non è possibile emettere ordini con quantità superiore a quella disponibile a magazzino.
- L'importo totale dell'ordine viene calcolato automaticamente dal sistema e non può essere modificato.
- Il magazzino viene aggiornato automaticamente all'emissione di un nuovo ordine o alla modifica di uno esistente.

## Gestione degli errori
#### Connessione a database
In caso di errore di connessione con il database, viene mostrato un messaggio nella GUI. 

#### Clienti
Vengono effettuati:
- controllo della compilazione dei campi;
- validazione dell'indirizzo email;
- validazione della password (minimo 8 caratteri, almeno un carattere numerico e un carattere speciale);
- verifica dell'esistenza dell'ID per le operazioni di modifica, ricerca ed eliminazione;
- visualizzazione di messaggi specifici in caso di errore.


#### Prodotti
Vengono effettuati:
- controllo della compilazione dei campi;
- validazione del prezzo e della quantità;
- verifica dell'esistenza dell'ID per le operazioni di modifica, ricerca ed eliminazione;
- visualizzazione di messaggi specifici in caso di errore.

#### Ordini
Vengono effettuati:
- Controllo compilazione dei campi;
- validazione della quantità richiesta e della relativa disponibilità in magazzino;
- verifica dell'esistenza degli ID dei prodotti e dei clienti;
- verifica dell'esistenza dell'ID dell'ordine per le operazioni di modifica, ricerca ed eliminazione;
- visualizzazione di messaggi specifici in caso di errore.

#### Analisi dei dati
Vengono effettuati:
- controllo dell'integrità dei dati;
- verifica della corretta creazione dei report;
- visualizzazione di messaggi specifici in caso di errore.

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
