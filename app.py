import os
import sqlite3
from contextlib import closing

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_talisman import Talisman


def database_path():
    url = os.getenv("DATABASE_URL", "sqlite:///accounts.db")
    return url.removeprefix("sqlite:///")


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        DATABASE=database_path(),
        JSON_SORT_KEYS=False,
        TESTING=False,
    )
    if test_config:
        app.config.update(test_config)

    CORS(app, resources={r"/*": {"origins": os.getenv("CORS_ORIGINS", "*")}})
    Talisman(app, force_https=False, content_security_policy=False)
    initialize_database(app.config["DATABASE"])

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.post("/accounts")
    def create_account():
        data = request.get_json(silent=True) or {}
        error = validate_account(data)
        if error:
            return jsonify({"error": error}), 400
        with connect(app.config["DATABASE"]) as db:
            cursor = db.execute(
                "INSERT INTO accounts (first_name, last_name, email) VALUES (?, ?, ?)",
                (data["first_name"].strip(), data["last_name"].strip(), data["email"].strip()),
            )
            account = get_account(db, cursor.lastrowid)
            db.commit()
        return jsonify(account), 201

    @app.get("/accounts")
    def list_accounts():
        with connect(app.config["DATABASE"]) as db:
            accounts = db.execute(
                "SELECT id, first_name, last_name, email FROM accounts ORDER BY id"
            ).fetchall()
        return jsonify([dict(row) for row in accounts])

    @app.get("/accounts/<int:account_id>")
    def read_account(account_id):
        with connect(app.config["DATABASE"]) as db:
            account = get_account(db, account_id)
        if account is None:
            return jsonify({"error": "Account not found"}), 404
        return jsonify(account)

    @app.route("/accounts/<int:account_id>", methods=["PUT", "PATCH"])
    def update_account(account_id):
        data = request.get_json(silent=True) or {}
        error = validate_account(data)
        if error:
            return jsonify({"error": error}), 400
        with connect(app.config["DATABASE"]) as db:
            if get_account(db, account_id) is None:
                return jsonify({"error": "Account not found"}), 404
            db.execute(
                "UPDATE accounts SET first_name=?, last_name=?, email=? WHERE id=?",
                (data["first_name"].strip(), data["last_name"].strip(),
                 data["email"].strip(), account_id),
            )
            db.commit()
            account = get_account(db, account_id)
        return jsonify(account)

    @app.delete("/accounts/<int:account_id>")
    def delete_account(account_id):
        with connect(app.config["DATABASE"]) as db:
            result = db.execute("DELETE FROM accounts WHERE id=?", (account_id,))
            db.commit()
        if result.rowcount == 0:
            return jsonify({"error": "Account not found"}), 404
        return "", 204

    return app


def connect(path):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    return db


def initialize_database(path):
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with closing(connect(path)) as db:
        db.execute(
            """CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )"""
        )
        db.commit()


def get_account(db, account_id):
    row = db.execute(
        "SELECT id, first_name, last_name, email FROM accounts WHERE id=?",
        (account_id,),
    ).fetchone()
    return dict(row) if row else None


def validate_account(data):
    required = ("first_name", "last_name", "email")
    if any(not isinstance(data.get(field), str) or not data[field].strip() for field in required):
        return "first_name, last_name, and email are required"
    if "@" not in data["email"] or data["email"].count("@") != 1:
        return "email must be valid"
    return None


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
