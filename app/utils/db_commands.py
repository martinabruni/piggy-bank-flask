from flask import Flask


def add_db_commands(app: Flask):
    from app import db

    @app.cli.command("db_create")
    def db_create():
        db.create_all()
        print("Database created!")

    @app.cli.command("db_drop")
    def db_drop():
        db.drop_all()
        print("Database dropped!")

    @app.cli.command("db_seed")
    def db_seed():
        pass
