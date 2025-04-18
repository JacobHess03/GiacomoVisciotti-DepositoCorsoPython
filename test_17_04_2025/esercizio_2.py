import mysql.connector
from mysql.connector import errorcode

# Configurazione del database
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'la_mia_password',  # Sostituire con la vostra password MySQL
}
DB_NAME = 'rubrica_db'

class DBManager:
    """
    Gestisce la connessione al database e le operazioni CRUD
    per le tabelle Utenti e Contatti.
    """
    def __init__(self, config, db_name):
        self.config = config
        self.db_name = db_name
        self._connect_server()
        self._create_database()
        self._connect_database()
        self._create_tables()

    def _connect_server(self):
        try:
            self.server_conn = mysql.connector.connect(
                host=self.config['host'],
                user=self.config['user'],
                password=self.config['password']
            )
            self.server_cursor = self.server_conn.cursor()
        except mysql.connector.Error as err:
            print(f"Errore di connessione al server: {err}")
            exit(1)

    def _create_database(self):
        try:
            self.server_cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS {self.db_name} DEFAULT CHARACTER SET 'utf8'"
            )
            print(f"Database '{self.db_name}' pronto.")
        except mysql.connector.Error as err:
            print(f"Errore creazione database: {err}")
            exit(1)
    
        self.server_cursor.close()
        self.server_conn.close()

    def _connect_database(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.config['host'],
                user=self.config['user'],
                password=self.config['password'],
                database=self.db_name
            )
            self.cursor = self.conn.cursor()
            print(f"Connesso al database '{self.db_name}'.")
        except mysql.connector.Error as err:
            print(f"Errore di connessione al database: {err}")
            exit(1)

    def _create_tables(self):
        tables = {}
        tables['Utenti'] = (
            "CREATE TABLE IF NOT EXISTS Utenti ("
            "  id INT AUTO_INCREMENT PRIMARY KEY,"
            "  nome VARCHAR(50) NOT NULL,"
            "  password VARCHAR(100) NOT NULL"
            ")"
        )
        tables['Contatti'] = (
            "CREATE TABLE IF NOT EXISTS Contatti ("
            "  id INT AUTO_INCREMENT PRIMARY KEY,"
            "  nome VARCHAR(100) NOT NULL,"
            "  telefono VARCHAR(20),"
            "  email VARCHAR(100),"
            "  utente_id INT"
            ")"
        )
        for table_name, ddl in tables.items():
            try:
                self.cursor.execute(ddl)
            except mysql.connector.Error as err:
                print(f"Errore creazione tabella {table_name}: {err}")
                exit(1)

    def add_user(self, nome, password):
        sql = "INSERT INTO Utenti (nome, password) VALUES (%s, %s)"
        self.cursor.execute(sql, (nome, password))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_user(self, nome, password):
        sql = "SELECT id, nome FROM Utenti WHERE nome=%s AND password=%s"
        self.cursor.execute(sql, (nome, password))
        row = self.cursor.fetchone()
        return {'id': row[0], 'nome': row[1]} if row else None

    def add_contact(self, nome, telefono, email, utente_id):
        sql = "INSERT INTO Contatti (nome, telefono, email, utente_id) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (nome, telefono, email, utente_id))
        self.conn.commit()

    def get_contacts(self, utente_id):
        sql = "SELECT id, nome, telefono, email FROM Contatti WHERE utente_id=%s"
        self.cursor.execute(sql, (utente_id,))
        return self.cursor.fetchall()

    def update_contact(self, contact_id, nome, telefono, email):
        sql = "UPDATE Contatti SET nome=%s, telefono=%s, email=%s WHERE id=%s"
        self.cursor.execute(sql, (nome, telefono, email, contact_id))
        self.conn.commit()

    def delete_contact(self, contact_id):
        sql = "DELETE FROM Contatti WHERE id=%s"
        self.cursor.execute(sql, (contact_id,))
        self.conn.commit()

class Application:
    """
    Gestisce l'interfaccia testuale e il flusso dell'applicazione.
    """
    def __init__(self, db_manager):
        self.db = db_manager
        self.current_user = None

    def run(self):
        self._login()
        while True:
            self._show_menu()

    def _login(self):
        print("=== Login ===")
        nome = input("Nome utente: ")
        pwd = input("Password: ")
        user = self.db.get_user(nome, pwd)
        if user:
            print(f"Login effettuato. Benvenuto, {user['nome']}!")
            self.current_user = user
        else:
            print("Utente non trovato o password errata.")
            choice = input("Vuoi registrarti? (s/n): ")
            if choice.lower() == 's':
                uid = self.db.add_user(nome, pwd)
                print(f"Utente registrato con ID {uid}. Effettua nuovamente il login.")
            self._login()

    def _show_menu(self):
        print("\n=== Menu Rubrica ===")
        print("1. Aggiungi contatto")
        print("2. Visualizza contatti")
        print("3. Modifica contatto")
        print("4. Elimina contatto")
        print("5. Esci")
        choice = input("Seleziona un'opzione: ")
        if choice == '1':
            self._aggiungi_contatto()
        elif choice == '2':
            self._visualizza_contatti()
        elif choice == '3':
            self._modifica_contatto()
        elif choice == '4':
            self._elimina_contatto()
        elif choice == '5':
            print("Logout e uscita...")
            exit(0)
        else:
            print("Opzione non valida. Riprova.")

    def _aggiungi_contatto(self):
        print("--- Aggiungi Contatto ---")
        nome = input("Nome: ")
        telefono = input("Telefono: ")
        email = input("Email: ")
        self.db.add_contact(nome, telefono, email, self.current_user['id'])
        print("Contatto aggiunto con successo.")

    def _visualizza_contatti(self):
        print("--- I Tuoi Contatti ---")
        contacts = self.db.get_contacts(self.current_user['id'])
        if not contacts:
            print("Nessun contatto trovato.")
            return
        for cid, nome, tel, mail in contacts:
            print(f"ID: {cid} | Nome: {nome} | Tel: {tel} | Email: {mail}")

    def _modifica_contatto(self):
        self._visualizza_contatti()
        cid = input("Inserisci ID del contatto da modificare: ")
        nome = input("Nuovo nome: ")
        telefono = input("Nuovo telefono: ")
        email = input("Nuova email: ")
        self.db.update_contact(cid, nome, telefono, email)
        print("Contatto aggiornato.")

    def _elimina_contatto(self):
        self._visualizza_contatti()
        cid = input("Inserisci ID del contatto da eliminare: ")
        self.db.delete_contact(cid)
        print("Contatto eliminato.")


def main():
    db_manager = DBManager(DB_CONFIG, DB_NAME)
    app = Application(db_manager)
    app.run()

if __name__ == '__main__':
    main()
