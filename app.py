import os
import sqlite3
from contextlib import closing

from flask import Flask, jsonify, request

from accounts import configure_security


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

    configure_security(app)
    initialize_database(app.config["DATABASE"])

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/")
    def service_info():
        return jsonify({"name": "Account REST API Service", "version": "1.0"})

    @app.post("/accounts")
    def create_account():
        data = request.get_json(silent=True) or {}
        normalized, error = normalize_account(data)
        if error:
            return jsonify({"error": error}), 400
        with closing(connect(app.config["DATABASE"])) as db:
            cursor = db.execute(
                """INSERT INTO accounts
                (first_name, last_name, email, name, address, phone_number)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (normalized["first_name"], normalized["last_name"], normalized["email"],
                 normalized["name"], normalized["address"], normalized["phone_number"]),
            )
            account = get_account(db, cursor.lastrowid)
            db.commit()
        return jsonify(account), 201

    @app.get("/accounts")
    def list_accounts():
        with closing(connect(app.config["DATABASE"])) as db:
            accounts = db.execute(
                """SELECT id, first_name, last_name, email, name, address, phone_number
                FROM accounts ORDER BY id"""
            ).fetchall()
        return jsonify([serialize_account(row) for row in accounts])

    @app.get("/accounts/<int:account_id>")
    def read_account(account_id):
        with closing(connect(app.config["DATABASE"])) as db:
            account = get_account(db, account_id)
        if account is None:
            return jsonify({"error": "Account not found"}), 404
        return jsonify(account)

    @app.route("/accounts/<int:account_id>", methods=["PUT", "PATCH"])
    def update_account(account_id):
        data = request.get_json(silent=True) or {}
        normalized, error = normalize_account(data)
        if error:
            return jsonify({"error": error}), 400
        with closing(connect(app.config["DATABASE"])) as db:
            if get_account(db, account_id) is None:
                return jsonify({"error": "Account not found"}), 404
            db.execute(
                """UPDATE accounts SET first_name=?, last_name=?, email=?,
                name=?, address=?, phone_number=? WHERE id=?""",
                (normalized["first_name"], normalized["last_name"], normalized["email"],
                 normalized["name"], normalized["address"], normalized["phone_number"],
                 account_id),
            )
            db.commit()
            account = get_account(db, account_id)
        return jsonify(account)

    @app.delete("/accounts/<int:account_id>")
    def delete_account(account_id):
        with closing(connect(app.config["DATABASE"])) as db:
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
                email TEXT NOT NULL UNIQUE,
                name TEXT,
                address TEXT,
                phone_number TEXT
            )"""
        )
        columns = {row[1] for row in db.execute("PRAGMA table_info(accounts)")}
        for column in ("name", "address", "phone_number"):
            if column not in columns:
                db.execute(f"ALTER TABLE accounts ADD COLUMN {column} TEXT")
        db.commit()


def get_account(db, account_id):
    row = db.execute(
        """SELECT id, first_name, last_name, email, name, address, phone_number
        FROM accounts WHERE id=?""",
        (account_id,),
    ).fetchone()
    return serialize_account(row) if row else None


def serialize_account(row):
    account = dict(row)
    if not account["name"]:
        account["name"] = f'{account["first_name"]} {account["last_name"]}'.strip()
    account["address"] = account["address"] or ""
    account["phone_number"] = account["phone_number"] or ""
    return account


def normalize_account(data):
    if all(isinstance(data.get(field), str) and data[field].strip()
           for field in ("name", "email", "address", "phone_number")):
        name = data["name"].strip()
        parts = name.split(maxsplit=1)
        first_name = parts[0]
        last_name = parts[1] if len(parts) > 1 else ""
        normalized = {
            "first_name": first_name,
            "last_name": last_name,
            "name": name,
            "email": data["email"].strip(),
            "address": data["address"].strip(),
            "phone_number": data["phone_number"].strip(),
        }
    elif all(isinstance(data.get(field), str) and data[field].strip()
             for field in ("first_name", "last_name", "email")):
        normalized = {
            "first_name": data["first_name"].strip(),
            "last_name": data["last_name"].strip(),
            "name": f'{data["first_name"].strip()} {data["last_name"].strip()}',
            "email": data["email"].strip(),
            "address": data.get("address", "").strip(),
            "phone_number": data.get("phone_number", "").strip(),
        }
    else:
        return None, "account name, email, address, and phone_number are required"
    if "@" not in normalized["email"] or normalized["email"].count("@") != 1:
        return None, "email must be valid"
    return normalized, None


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
