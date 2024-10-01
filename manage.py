import os


def deploy():
    """
    Run deployment tasks for database migration. Initializes, stamps, migrates, and upgrades the database schema.
    """
    from app import create_app, db
    from flask_migrate import upgrade, migrate, init, stamp
    from app.user.user_model import User

    app = create_app()
    app.app_context().push()
    db.create_all()

    # Controlla se la cartella 'migrations' esiste
    if not os.path.exists("migrations"):
        # Se non esiste, esegui init()
        init()
        stamp()  # Stampa lo stato attuale delle migrazioni
    else:
        print("La cartella 'migrations' esiste già, salto l'inizializzazione.")

    migrate()  # Crea una nuova migrazione, se necessario
    upgrade()  # Aggiorna il database all'ultima migrazione


deploy()
