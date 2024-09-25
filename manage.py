def deploy():
    """
    Run deployment tasks for database migration. Initializes, stamps, migrates, and upgrades the database schema.
    """
    from app import create_app, db
    from flask_migrate import upgrade, migrate, init, stamp
    from app.user.models.user import User

    app = create_app()
    app.app_context().push()
    db.create_all()

    # Migrate database to the latest revision
    init()
    stamp()
    migrate()
    upgrade()


deploy()
