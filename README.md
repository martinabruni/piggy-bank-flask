# Piggy Bank

Piggy Bank è un'applicazione di gestione delle spese scritta in Flask. Permette agli utenti di registrarsi, effettuare il login e gestire le proprie transazioni. Al momento, l'app è testabile tramite richieste API inviate a determinati endpoint.

## Prerequisiti

1. **Python** (preferibilmente versione 3.7 o superiore)
2. **pip** per installare le dipendenze
3. **Flask** per il server web
4. **Postman** (o uno strumento simile) per testare le API

## Installazione

1. **Clona il repository:**

   ```bash
   git clone https://github.com/martinabruni/piggy-bank-flask.git
   cd piggy-bank-flask
   ```

2. **Crea un ambiente virtuale:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Su Windows: venv\Scripts\activate
   ```

3. **Installa le dipendenze:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura le variabili d'ambiente:**

   Crea un file `.env` nella root della directory del progetto e aggiungi le seguenti variabili:

   ```plaintext
   KEY=<Una_stringa_a_caso_per_la_segretezza>
   ```

   Per generare una chiave segreta sicura, puoi utilizzare il modulo `secrets` di Python:

   ```python
   import secrets
   secrets.token_hex(16)  # genera una chiave in formato sicuro
   ```

   Ad esempio, il risultato potrebbe essere:

   ```python
   '8f42a73054b1749f8f58848be5e6502c'  # esempio di chiave generata (NON UTILIZZARLA)
   ```

   Copia questa stringa e incollala nel file `.env` sotto la variabile `KEY`.

5. **Avvia l'app:**

   Per avviare il server di sviluppo:

   ```bash
   flask run
   ```

6. **Creazione/Migrazione del Database:**

   Per creare e migrare il database:

   ```bash
   python manage.py
   ```

## Endpoint API

- **POST /register**: Crea un nuovo account utente. Restituisce uno status di successo o errore.
- **POST /login**: Accede all'account utente. Restituisce un token di sessione in caso di successo.
- **POST /logout**: Esci dall'account utente.
- **GET /profile**: Mostra il profilo dell'utente autenticato.

## Struttura del Database

Le seguenti tabelle sono presenti nel database:

1. **user**

   - id (Primary Key)
   - username
   - email
   - password_hash

2. **account**

   - id (Primary Key)
   - name
   - balance (default 0.0)
   - user_id (Foreign Key -> user.id)

3. **category**

   - id (Primary Key)
   - name (unique)

4. **transaction**
   - id (Primary Key)
   - amount
   - date (default UTC)
   - description (optional)
   - user_id (Foreign Key -> user.id)
   - account_id (Foreign Key -> account.id)
   - category_id (Foreign Key -> category.id)

## Test

Puoi testare l'app utilizzando strumenti come **Postman** per inviare richieste agli endpoint API sopra indicati.
